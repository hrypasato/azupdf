from bs4 import BeautifulSoup
import re
from utils.http import get_html

def extract_pdf_url(page_url: str) -> str:
    html = get_html(page_url)
    soup = BeautifulSoup(html, "html.parser")

    iframe = soup.find("iframe")
    if not iframe:
        raise ValueError("No se encontró iframe")

    src = iframe.get("src")

    match = re.search(r'file=(https?://[^&]+\.pdf)', src)
    if not match:
        raise ValueError("No se encontró URL del PDF")

    return match.group(1)