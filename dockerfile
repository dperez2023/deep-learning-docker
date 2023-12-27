# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Clone or copy the ultralytics library into your container
RUN git clone https://github.com/ultralytics/yolov5.git /app/ultralytics

# Copy the rest of your project files
COPY . /app

# Install other dependencies
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python", "main.py"]
