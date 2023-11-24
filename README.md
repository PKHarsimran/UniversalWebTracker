# UniversalWebTracker
🌐 Monitor any website with ease using the UniversalWebTracker. Initially designed to track Cortex agent version updates, this versatile Python script is now equipped to monitor any website of your choice. Stay informed with timely alerts whenever there are changes, keeping you ahead with the latest updates.

## Key Features

### Versatile Website Monitoring
- **Broaden Your Horizons:** Originally crafted for Cortex agent versions, this script is adaptable to monitor changes on any website. Simply configure the target URL to switch between different websites seamlessly.

### Docker Integration
- **Containerized for Flexibility:** The script is encapsulated within Docker, ensuring a consistent environment and easy deployment, irrespective of the target website.
- **Automated Checks with Cron:** Deployed as a Docker container, the script utilizes cron for scheduled and automated monitoring, reducing the need for manual oversight.

### User-Friendly and Efficient
- **Resource-Efficient Operation:** Designed to be light on resources, the script smartly checks for updates, ensuring efficient operation without compromising responsiveness.
- **Easy to Configure and Use:** With straightforward configuration steps, the script can be set up quickly to start monitoring your website of choice.

Embrace the power of automation and versatility with UniversalWebTracker – your go-to solution for keeping tabs on any website efficiently and effortlessly.

## How It Works

### 1. **Target URL Configuration**
   - Users configure the script to monitor a specific URL. This flexibility allows tracking of virtually any website.

### 2. **Fetching and Analyzing Content**
   - The script periodically sends an HTTP request to the targeted URL to fetch the current webpage content.
   - It computes a SHA-256 hash of this content, providing a unique fingerprint for the current state of the webpage.

### 3. **Change Detection Mechanism**
   - The script compares the newly computed hash with a previously stored hash (from the last check).
   - A difference in hashes indicates a change in the webpage content.

### 4. **Notifications and Logging**
   - When a change is detected, the script logs this event.
   - It can be configured to send notifications or alerts to inform users about these changes.

## Advanced Features

### Cron Job Scheduling
- The script is integrated with a cron job within a Docker container. This setup automates the process, with the script running at regular intervals defined in the cron schedule.

### Docker Integration
- **Dockerfile Creation:** A Dockerfile is created to define the script's running environment. This file includes instructions for setting up Python, installing necessary dependencies, and configuring the cron job.
- **Isolated Environment:** Running the script inside a Docker container ensures an isolated and consistent environment, regardless of the deployment platform.
- **Cron Setup in Docker:** The Dockerfile includes steps to set up a cron job that regularly triggers the script. This approach automates the monitoring process, making it more reliable and efficient.

## Usage

- **Configure the URL:** Set the target website URL in the script.
- **Deploy with Docker:** Build the Docker container using the provided Dockerfile. This container includes everything needed to run the script.
- **Automated Monitoring:** Once deployed, the script will automatically check the specified website at intervals defined in the cron job.

