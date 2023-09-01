import time
import requests
import hashlib

def get_hash(url):
  response = requests.get(url)
  return hashlib.sha256(response.content).hexdigest()

def save_hash(hash_value, filename):
  with open(filename, "w") as f:
    f.write(hash_value)

def main():
  url = "https://www.google.com/"
  filename = "hash.txt"

  # Get the initial hash of the website and save it to a file
  initial_hash = get_hash(url)
  save_hash(initial_hash, filename)

  previous_hash = None

  while True:
    current_hash = get_hash(url)

    if previous_hash is None or current_hash != previous_hash:
      # The website has changed!
      print("The website has changed!")
      save_hash(current_hash, filename)

    previous_hash = current_hash

    time.sleep(60 * 60)  # Check every hour

if __name__ == "__main__":
  main()

