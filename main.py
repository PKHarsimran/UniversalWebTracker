import requests
import hashlib
import logging
import sys

from logging.handlers import RotatingFileHandler

# Set the URL to monitor and file for storing the hash
URL = "https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Agent-Releases/Cortex-XDR-Agent-Releases"
HASH_FILE = "hash.txt"
LOG_FILE = "monitor.log"

# Configure dual logging to both file and stdout
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1024*1024*5, backupCount=2)  # 5MB per file, keeping 2 backups
file_handler.setFormatter(log_formatter)

logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])


def fetch_content(url):
    """Fetch the webpage content from the URL."""
    logging.info(f"Fetching content from URL: {url}")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        logging.info("Successfully fetched content.")
        return response.content
    except requests.RequestException as error:
        logging.error(f"Error fetching {url}: {error}")
        return None

def compute_hash(content):
    """Compute the SHA-256 hash of the webpage content."""
    if content:
        logging.info("Computing SHA-256 hash of the content.")
        return hashlib.sha256(content).hexdigest()
    else:
        logging.warning("No content to compute hash.")
        return None

def file_operations(file_name, mode, content=None):
    """Read from or write to a file."""
    operation = "Reading from" if mode == "r" else "Writing to"
    logging.info(f"{operation} file: {file_name}")
    try:
        with open(file_name, mode) as file:
            if mode == "r":
                return file.read().strip()
            elif mode == "w":
                file.write(content)
    except FileNotFoundError:
        logging.error(f"File not found: {file_name}")
        return None if mode == "r" else None
    except Exception as error:
        logging.error(f"File operation error on {file_name}: {error}")

def monitor_website():
    """Check for changes in the website content."""
    logging.info("Starting website monitoring process.")
    original_hash = file_operations(HASH_FILE, "r")
    content = fetch_content(URL)
    current_hash = compute_hash(content)

    if not current_hash:
        logging.warning("Unable to generate current hash.")
        return

    if not original_hash or current_hash != original_hash:
        message = "Website content has changed!" if original_hash else "Initial hash not found, saving current hash."
        logging.info(message)
        file_operations(HASH_FILE, "w", current_hash)
    else:
        logging.info("No changes detected in the website content.")

if __name__ == "__main__":
    logging.info("Executing website monitoring script.")
    monitor_website()
