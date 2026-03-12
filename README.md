# Cloud Infrastructure Observability System

## Overview

This project demonstrates a **Cloud Infrastructure Observability System** designed to monitor internet network performance and detect connectivity issues automatically.

The system collects key infrastructure metrics such as latency, download speed, upload speed, and packet loss, stores them in the cloud, and triggers alerts when performance thresholds are exceeded.

This project simulates a real-world monitoring solution that could be used in environments where network reliability is critical.

---

# Problem Statement

In many environments, especially in developing regions, network performance can fluctuate due to infrastructure limitations.

Without proper monitoring systems, it becomes difficult to detect issues such as:

* High latency
* Slow download speeds
* Packet loss
* Network instability

Infrastructure observability helps engineers monitor system health and respond quickly to performance degradation.

---

# Solution

This project builds a lightweight **cloud-based observability pipeline** that:

1. Collects network performance metrics.
2. Stores monitoring data in the cloud.
3. Analyzes metrics automatically.
4. Sends alerts when anomalies are detected.

---

# Architecture

```
Monitoring Agent (Python)
        ↓
Internet Metrics Collection
        ↓
Amazon S3 (Metrics Storage)
        ↓
AWS Lambda (Metrics Analysis)
        ↓
Amazon SNS (Alert Notification)
```

---

# Technologies Used

* Python
* AWS Cloud Services

Cloud services used in this project:

* **Amazon S3** – stores monitoring metrics
* **AWS Lambda** – processes monitoring data
* **Amazon SNS** – sends alert notifications

---

# Project Structure

```
cloud-infrastructure-observability/

README.md

monitoring-agent/
    monitor.py
    requirements.txt

lambda-function/
    lambda_function.py

sample-data/
    metrics_sample.json
```

---

# How It Works

### Step 1: Monitoring Agent

A Python monitoring script collects network performance metrics including:

* Latency
* Download speed
* Upload speed
* Packet loss

The metrics are stored as JSON files.

Example output:

```json
{
  "timestamp": "2026-03-10 12:10:45",
  "latency_ms": 82.3,
  "download_mbps": 4.5,
  "upload_mbps": 2.1,
  "packet_loss_percent": 0.2
}
```

---

### Step 2: Cloud Storage

The metrics file is uploaded to **Amazon S3**, which acts as a central data store for monitoring logs.

---

### Step 3: Automated Analysis

When a new metrics file is uploaded, **AWS Lambda** is triggered automatically.

The Lambda function checks if the metrics exceed predefined thresholds such as:

* Latency greater than 100 ms
* Download speed below 5 Mbps
* Packet loss above 1%

---

### Step 4: Alerting

If an anomaly is detected, the system sends a notification using **Amazon SNS**.

The alert is delivered via email to notify engineers of potential network issues.

---

# Skills Demonstrated

This project demonstrates practical experience in:

* Cloud infrastructure monitoring
* Serverless architecture
* Observability systems
* Infrastructure automation
* Cloud-based alerting systems

---

# Future Improvements

Potential improvements for this project include:

* Real-time dashboards
* Historical performance analysis
* Machine learning anomaly detection
* Integration with monitoring tools like Prometheus or Grafana

---

# Author

Daniel Afeamenyo

Cloud & Infrastructure Engineer interested in building scalable cloud solutions and improving infrastructure reliability.

---

If you want, I can also help you **add a professional architecture diagram to the README** that makes the GitHub project look **10× more impressive to recruiters**.
