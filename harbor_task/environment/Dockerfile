# Dockerfile for the task environment
# Builds a container with Python and the unsolved repo inside.

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    patch \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the repo into the container (unsolved state)
COPY repo/ /app/repo/

# Install the package in editable mode and test dependencies
RUN pip install --no-cache-dir pytest

# Make sure pytest can find the tests
ENV PYTHONPATH=/app/repo/src

# Default command
CMD ["bash"]
