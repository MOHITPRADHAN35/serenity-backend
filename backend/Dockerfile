FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    python3-distutils \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pip first separately
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip setuptools wheel

# Copy project files
COPY . /app

# Create and activate venv, install dependencies
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip setuptools wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set PATH to use virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# Make start.sh executable
RUN chmod +x start.sh

# Expose port
EXPOSE 8000

# Default command
CMD ["bash", "start.sh"]
