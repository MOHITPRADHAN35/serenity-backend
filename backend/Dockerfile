FROM python:3.10-slim

WORKDIR /app

# Install system packages (added python3-distutils!)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3-dev \
    python3-distutils \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy all code
COPY . /app

# Create venv and install requirements
RUN python -m venv /opt/venv \
 && /opt/venv/bin/pip install --upgrade pip \
 && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set PATH to use venv by default
ENV PATH="/opt/venv/bin:$PATH"

# Give permissions
RUN chmod +x start.sh

# Expose port (edit if needed)
EXPOSE 8000

# Default command
CMD ["bash", "start.sh"]
