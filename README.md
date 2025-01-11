# Malicious Payload Detection API

A Flask-based REST API that uses machine learning to detect malicious payloads in HTTP requests. This API is designed to work with web applications to provide real-time detection of potentially harmful request content.

## Features

- Real-time payload analysis
- Support for multiple payload strings in a single request
- Machine learning-based detection
- Simple JSON API interface
- Easy integration with web applications

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Model ML
```bash
https://huggingface.co/Sulthonul/malicious-payload-detection/tree/main
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sulthonmb/api-detect-malicious-payload
cd api-detect-malitious-payload

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```

2. Run the application:
```bash
python3 app.py
```
