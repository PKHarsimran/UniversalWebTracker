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

1. **Setting the Target URL**
   - The script is configured to monitor a specific URL. Originally designed for Cortex agent version updates, it can be easily adjusted to track any website.

2. **Fetching Website Content**
   - At regular intervals, the script sends an HTTP request to the targeted URL to fetch the current content of the webpage.

3. **Computing the Content Hash**
   - The script computes a hash (SHA-256) of the fetched content. This hash serves as a fingerprint of the content at that specific time.

4. **Detecting Changes**
   - The current hash is compared with the previously stored hash (from the last check). If there's a difference, it indicates that the content of the webpage has changed.

5. **Logging and Alerts**
   - Upon detecting a change, the script logs this information and can be configured to send alerts or notifications, keeping the user informed about the updates.

6. **Docker Integration**
   - The script is containerized using Docker. This ensures that it runs in an isolated environment, with consistent settings, regardless of where it is deployed.
   - Inside the Docker container, the script is executed periodically as a cron job, automating the monitoring process.

7. **Resource Efficiency**
   - The script is designed to be light on system resources, making it an efficient solution for continuous monitoring.

## Usage

- To use the script, simply configure the target URL in the script settings.
- Deploy the script using Docker to ensure a consistent and isolated environment.
- The script will regularly check the specified website and notify you of any changes detected.

With UniversalWebTracker, stay up-to-date effortlessly with the latest changes on your favorite websites.
