FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
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
