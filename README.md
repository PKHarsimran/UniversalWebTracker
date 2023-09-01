# CortexVerSiteTracker
🔍 Keep track of Cortex agent version updates effortlessly with our Python script designed to monitor the official Cortex agent version site. Receive timely alerts whenever a new version is released, ensuring you're always up-to-date with the latest changes.
| Task                                           | Status        | Description                                                                                                                                                                                             | Details                                           |
| ---------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Create a Python script to track website changes | In progress   | Develop a Python script that can retrieve and store the hash of a website. Add functionality to compare the stored hash with the current website hash to detect changes.                     | Using `requests` and `hashlib` modules.           |
| Implement a function to save website hashes     | Completed     | Create the `save_hash()` function capable of saving website hashes to a file named `hash.txt`.                                                                                                          | Accepts website URL and hash as input.            |
| Establish a continuous website monitoring loop  | In progress   | Design a loop that continuously checks the website for changes. When a discrepancy between the current hash and the stored hash is detected, the script will trigger a change notification. | Uses a `while True` loop for continuous monitoring. |
| Notify of website changes via Jira             | To be done    | Integrate Jira for change notifications. Develop code to automatically create Jira tickets or updates when website changes are detected.                                                              | Specify Jira project and issue details.           |



