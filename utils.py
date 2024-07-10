import requests
import time
import logging


def read_components_from_file(filename):
    components = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                components.append(tuple(parts))
    return components


def check_component(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=5)
            return response.status_code, True
        except requests.exceptions.RequestException as e:
            logging.error(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
                logging.info(f"Retrying in {delay} seconds...")
            return e, False