import time
import requests
import hashlib
import logging

# Configuration
URL = "https://www.google.com/"
FILENAME = "hash.txt"
SLEEP_INTERVAL_SECONDS = 3600  # 1 hour

# Configure logging
logging.basicConfig(filename="website_monitor.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

def get_hash(url):
    try:
        response = requests.get(url)
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

def check_website_for_changes():
    initial_hash = get_hash(URL)
    if initial_hash is None:
        return

    while True:
        current_hash = get_hash(URL)

        if current_hash is None:
            return

        if current_hash != initial_hash:
            logging.info("The website has changed!")
            save_hash(current_hash, FILENAME)
            initial_hash = current_hash

        time.sleep(SLEEP_INTERVAL_SECONDS)

def main():
    logging.info("Website monitoring started.")
    check_website_for_changes()

if __name__ == "__main__":
    main()
