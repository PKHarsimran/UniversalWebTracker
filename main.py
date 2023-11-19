import requests
import hashlib
import logging

# Set the URL to monitor and file for storing the hash
URL = "https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Agent-Releases/Cortex-XDR-Agent-Releases"
HASH_FILE = "hash.txt"

# Configure logging
logging.basicConfig(filename="monitor.log", level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def fetch_content(url):
    """Fetch the webpage content from the URL."""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.RequestException as error:
        logging.error(f"Error fetching {url}: {error}")
        return None

def compute_hash(content):
    """Compute the SHA-256 hash of the webpage content."""
    return hashlib.sha256(content).hexdigest() if content else None

def file_operations(file_name, mode, content=None):
    """Read from or write to a file."""
    try:
        with open(file_name, mode) as file:
            if mode == "r":
                return file.read().strip()
            elif mode == "w":
                file.write(content)
    except FileNotFoundError:
        return None if mode == "r" else logging.error("File not found for writing.")
    except Exception as error:
        logging.error(f"File operation error: {error}")

def monitor_website():
    """Check for changes in the website content."""
    original_hash = file_operations(HASH_FILE, "r")
    content = fetch_content(URL)
    current_hash = compute_hash(content)

    if not current_hash:
        logging.warning("Unable to generate current hash.")
        return

    if not original_hash or current_hash != original_hash:
        message = "Website changed!" if original_hash else "Saving initial hash."
        logging.info(message)
        file_operations(HASH_FILE, "w", current_hash)
    else:
        logging.info("No changes detected.")

if __name__ == "__main__":
    logging.info("Starting website monitoring.")
    monitor_website()
