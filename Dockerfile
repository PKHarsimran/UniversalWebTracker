# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install cron
RUN apt-get update && apt-get -y install cron

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the crontab file to the cron.d directory
COPY crontab /etc/cron.d/simple-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/simple-cron

# Apply cron job
RUN crontab /etc/cron.d/simple-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Install any needed packages from requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script into the container
COPY . .

# Run the cron command on container startup
CMD cron && tail -f /var/log/cron.log
