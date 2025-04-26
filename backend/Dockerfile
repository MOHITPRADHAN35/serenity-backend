# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Create virtual environment
RUN python -m venv /opt/venv

# Activate virtual environment and install Python dependencies
RUN . /opt/venv/bin/activate && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Make sure venv is active for all future RUN/CMD
ENV PATH="/opt/venv/bin:$PATH"

# Give permission to start.sh (if you have it)
RUN chmod +x start.sh

# Expose app port (optional, depends on your app)
EXPOSE 8000

# Command to run your app
CMD ["bash", "start.sh"]
