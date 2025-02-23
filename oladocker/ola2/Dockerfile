# Dockerfile
# Base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy application files
COPY . .

# Copy requirements.txt
COPY requirements.txt .

# Install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Expose Gradio app default port
EXPOSE 7860

# Set environment variable for the Google API Key securely

# Command to run the application
CMD ["python", "app.py", "--host=0.0.0.0", "--port=7860"]