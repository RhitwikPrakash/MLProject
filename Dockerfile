FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install system packages: git (needed for pip install from GitHub)
RUN apt update -y && apt install awscli -y

# Upgrade pip and install Python dependencies
RUN pip install -r requirements.txt

# Run your app
CMD ["python", "app.py"]
