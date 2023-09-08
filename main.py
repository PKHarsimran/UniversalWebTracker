import requests
import hashlib
import logging
import os

# Configuration
URL = "https://www.google.com/"
FILENAME = "hash.txt"

# Configure logging
logging.basicConfig(filename="website_monitor.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

def get_hash(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return hashlib.sha256(response.content).hexdigest()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while fetching {url}: {e}")
        return None

def save_hash(hash_value, filename):
    try:
        with open(filename, "w") as f:
            f.write(hash_value)
    except Exception as e:
        logging.error(f"Error while saving hash to {filename}: {e}")

def read_initial_hash(filename):
    try:
        with open(filename, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def check_website_for_changes():
    initial_hash = read_initial_hash(FILENAME)

    current_hash = get_hash(URL)
    if current_hash is None:
        logging.warning("Current hash could not be generated. Exiting.")
        return

    if initial_hash is None:
        logging.info("Initial hash not found, saving current hash.")
        save_hash(current_hash, FILENAME)
        return

    if current_hash != initial_hash:
        logging.info("The website has changed!")
        save_hash(current_hash, FILENAME)
    else:
        logging.info("No change detected.")

def main():
    logging.info("Website monitoring started.")
    check_website_for_changes()

if __name__ == "__main__":
    main()
