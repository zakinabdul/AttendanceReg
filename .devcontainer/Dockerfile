# .devcontainer/Dockerfile
FROM python:3.11-slim

# System tools needed for dev
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set working directory (matches your workspace root)
WORKDIR /workspace/backend


# Install Python deps early (optional)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running indefinitely
CMD ["sleep", "infinity"]