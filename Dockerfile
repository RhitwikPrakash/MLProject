FROM python:3.9-slim

WORKDIR /app

# Install system dependencies only once
RUN apt update -y && apt install -y \
    gcc g++ \
    libglib2.0-0 libsm6 libxext6 libxrender-dev

# Only copy requirements.txt early to cache pip install
COPY requirements.txt .

# Install Python dependencies — this is the slowest step
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
