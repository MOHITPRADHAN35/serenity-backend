HEAD
# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


FROM python:3.10-slim

4ff517b7ccda6bb4efb315fd5c12bf8a8f73c239
# Set working directory
WORKDIR /app

# Install system dependencies
HEAD
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port Cloud Run expects
EXPOSE 8080

# Start Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-distutils \
    python3-dev \
    gcc \
    g++ \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel early
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip setuptools wheel

# Copy all project files
COPY . /app

# Create and activate venv, install requirements
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip setuptools wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Use virtual environment by default
ENV PATH="/opt/venv/bin:$PATH"

# Make start.sh executable
RUN chmod +x start.sh

# Expose port
EXPOSE 8000

# Start command
CMD ["bash", "start.sh"]
4ff517b7ccda6bb4efb315fd5c12bf8a8f73c239
