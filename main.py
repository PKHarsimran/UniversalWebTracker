import requests
import hashlib
import logging
import os

# Configuration section: URL to monitor and filename to save hash values
URL = "https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Agent-Releases/Cortex-XDR-Agent-Releases"
FILENAME = "hash.txt"

# Configure logging to write logs to a file with a certain format
logging.basicConfig(filename="website_monitor.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

# Function to get the hash of a website's content
def get_hash(url):
    try:
        # Set a User-Agent header to act like a web browser
        headers = {"User-Agent": "Mozilla/5.0"}
        # Make an HTTP GET request and set a timeout
        response = requests.get(url, headers=headers, timeout=10)
        # Raise an exception if an HTTP error occurs
        response.raise_for_status()
        # Calculate and return the SHA-256 hash of the content
        return hashlib.sha256(response.content).hexdigest()
    except requests.exceptions.RequestException as e:
        # Log any request exceptions and return None
        logging.error(f"Error while fetching {url}: {e}")
        return None

# Function to save a hash value to a file
def save_hash(hash_value, filename):
    try:
        with open(filename, "w") as f:
            f.write(hash_value)
    except Exception as e:
        # Log any file-related exceptions
        logging.error(f"Error while saving hash to {filename}: {e}")

# Function to read the initial hash value from a file
def read_initial_hash(filename):
    try:
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None

# Function to check a website for changes based on its content hash
def check_website_for_changes():
    # Read the initial hash value from the file
    initial_hash = read_initial_hash(FILENAME)

    # Fetch the current hash value of the website
    current_hash = get_hash(URL)
    if current_hash is None:
        logging.warning("Current hash could not be generated. Exiting.")
        return

    # If no initial hash was found, save the current hash
    if initial_hash is None:
        logging.info("Initial hash not found, saving current hash.")
        save_hash(current_hash, FILENAME)
        return

    # Compare the current hash with the initial hash and log any changes
    if current_hash != initial_hash:
        logging.info("The website has changed!")
        save_hash(current_hash, FILENAME)
    else:
        logging.info("No change detected.")

# Main function to execute the script
def main():
    logging.info("Website monitoring started.")
    check_website_for_changes()

# If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
