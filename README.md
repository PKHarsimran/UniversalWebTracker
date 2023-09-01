# CortexVerSiteTracker
🔍 Keep track of Cortex agent version updates effortlessly with our Python script designed to monitor the official Cortex agent version site. Receive timely alerts whenever a new version is released, ensuring you're always up-to-date with the latest changes.

| Task | Status | Notes |
|---|---|---|
| Create a Python script to track a website for changes | In progress | The script is currently able to get the hash of a website and save it to a file. I need to add code to check the hash file and compare it to the current hash of the website. The script is using the `requests` and `hashlib` modules. The `requests` module is used to make HTTP requests to the website, and the `hashlib` module is used to create a hash of the website's content. |
| Create a function to save the hash of a website to a file | Completed | The `save_hash()` function is now able to save the hash of a website to a file. The function takes the URL of the website and the hash of the website as input, and it saves the hash to a file called `hash.txt`. |
| Create a loop to continuously check the website for changes | In progress | I have created a loop that will continuously check the website for changes. The loop uses the `while True:` statement to keep running until the script is stopped. The loop gets the current hash of the website and compares it to the hash file. If the hashes are different, then the website has changed. The script then prints a message to the console and updates the hash file. |
| Notify about website changes using Jira | To be done | I will add code to the script to notify about website changes using Jira. |


