# Use Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from your current project into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=RasaFlask/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port for Flask (default is 5000)
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
