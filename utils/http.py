import requests
from config import DEFAULT_HEADERS

def get_html(url: str) -> str:
    response = requests.get(url, headers=DEFAULT_HEADERS)
    response.raise_for_status()
    return response.text