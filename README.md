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



## Project Progress

📌 **Create a Python script to track website changes**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Implement a function to save website hashes**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Implement a function to read initial hash**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Run script using cron**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Notify of website changes via Jira**  
⌛ To be done  
▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ 0%

📌 **Implement logging**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Set User-Agent in HTTP requests**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%

📌 **Implement request timeout**  
✅ Completed  
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%


