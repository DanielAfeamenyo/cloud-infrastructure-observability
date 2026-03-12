import json
import boto3

SNS_TOPIC_ARN = ""
sns_client = boto3.client("sns")

def lambda_handler(event, context):
    # Get file info from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket, Key=key)
    data = json.loads(response['Body'].read())

    # Extract metrics
    latency = data.get("latency_ms")
    download = data.get("download_mbps")
    upload = data.get("upload_mbps")
    packet_loss = data.get("packet_loss_percent")

    # Check for anomalies
    anomalies = []
    if latency and latency > 100:
        anomalies.append(f"High latency: {latency} ms")
    if download and download < 5:
        anomalies.append(f"Low download: {download} Mbps")
    if upload and upload < 1:
        anomalies.append(f"Low upload: {upload} Mbps")
    if packet_loss and packet_loss > 5:
        anomalies.append(f"High packet loss: {packet_loss}%")

    # Send alert if anomalies detected
    if anomalies:
        message = f"🚨 Network Alert in {key}:\n" + "\n".join(anomalies)
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Network Alert",
            Message=message
        )
        print(message)
    else:
        print(f"No anomalies in {key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }