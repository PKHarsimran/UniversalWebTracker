# CortexVerSiteTracker
🔍 Keep track of Cortex agent version updates effortlessly with our Python script designed to monitor the official Cortex agent version site. Receive timely alerts whenever a new version is released, ensuring you're always up-to-date with the latest 
changes.

## Rationale for Using File Modification Time

In this script, we've chosen to monitor website changes by utilizing the file modification time of the hash file (`hash.txt`) rather than relying solely on a while loop with a fixed sleep interval. Here's why we made this decision:

### Improved Resource Efficiency

- A while loop with a fixed sleep interval can consume system resources, even when there are no changes detected. By checking the file modification time, we can reduce resource usage and make the script more efficient.

### Immediate Response to Changes

- Monitoring the hash file's modification time allows us to immediately respond to changes. When the hash file is updated, it indicates a change in the website, and the script can react accordingly.

### Flexibility in Check Frequency

- With the file modification time approach, we can dynamically adjust the frequency of checks by modifying the sleep interval. This flexibility allows us to balance between timely detection of changes and resource efficiency.

By using this approach, we aim to create a more resource-friendly and responsive website monitoring script.




## Project Tasks

| Task                                           | Status        | Description                                                                                                                                                                                             | Details                                           |
| ---------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Create a Python script to track website changes | In progress   | Develop a Python script that can retrieve and store the hash of a website. Add functionality to compare the stored hash with the current website hash to detect changes.                     | Using `requests` and `hashlib` modules.           |
| Implement a function to save website hashes     | Completed     | Create the `save_hash()` function capable of saving website hashes to a file named `hash.txt`.                                                                                                          | Accepts website URL and hash as input.            |
| Establish a continuous website monitoring loop  | In progress   | Design a system that periodically checks the website for changes. When a discrepancy between the current hash and the stored hash is detected, the script will trigger a change notification.    | Using `cron` jobs for periodic monitoring.         |
| Notify of website changes via Jira             | To be done    | Integrate Jira for change notifications. Develop code to automatically create Jira tickets or updates when website changes are detected.                                                              | Specify Jira project and issue details.           |



