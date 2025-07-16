FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install system packages: git (needed for pip install from GitHub)
RUN apt update -y && apt install -y gcc g++ libglib2.0-0 libsm6 libxext6 libxrender-dev

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
