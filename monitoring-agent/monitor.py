import speedtest
from ping3 import ping
import pandas as pd
from datetime import datetime, timezone
import json
import boto3
import os

# -----------------------------
# AWS S3 Configuration
# -----------------------------
UPLOAD_TO_S3 = True
BUCKET_NAME = "kafui-network-monitor-storage"
S3_FOLDER = "network_metrics/"

s3_client = boto3.client(
    "s3",
    aws_access_key_id="YOUR_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY",
    region_name="us-east-1"
)

# -----------------------------
# Metrics Functions
# -----------------------------
def get_latency(host="8.8.8.8"):
    try:
        latency = ping(host, unit="ms")
        return round(latency, 2) if latency else None
    except:
        return None

def get_speed():
    try:
        st = speedtest.Speedtest()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        return download, upload
    except:
        return None, None

def get_packet_loss(host="8.8.8.8", count=4):
    lost = 0
    for _ in range(count):
        if ping(host, timeout=2) is None:
            lost += 1
    packet_loss = (lost / count) * 100
    return round(packet_loss, 2)

def collect_metrics():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    latency = get_latency()
    download, upload = get_speed()
    packet_loss = get_packet_loss()

    data = {
        "timestamp": timestamp,
        "latency_ms": latency,
        "download_mbps": download,
        "upload_mbps": upload,
        "packet_loss_percent": packet_loss
    }
    return data

# -----------------------------
# Main
# -----------------------------
metrics = collect_metrics()
print("Collected Metrics:", metrics)

# Save locally as CSV
df = pd.DataFrame([metrics])
local_file = "network_metrics.csv"
if not os.path.exists(local_file):
    df.to_csv(local_file, mode='w', index=False, header=True)
else:
    df.to_csv(local_file, mode='a', index=False, header=False)
print(f"Saved locally: {local_file}")

# Upload to S3
if UPLOAD_TO_S3:
    file_name = f"{S3_FOLDER}network_metrics_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.json"
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(metrics)
    )
    print(f"Uploaded to S3: s3://{BUCKET_NAME}/{file_name}")