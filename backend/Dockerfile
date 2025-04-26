# Install system dependencies needed to build Python packages
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
