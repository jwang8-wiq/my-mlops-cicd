# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the dependency list and install it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY . .

# Specify the command to run the training script
ENTRYPOINT ["python", "train.py"]