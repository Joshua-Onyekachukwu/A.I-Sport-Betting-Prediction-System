# data/scrape.py
import requests
from bs4 import BeautifulSoup

def scrape_injury_reports():
    url = "https://example.com/injury-reports"  # Replace with actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract and return injury data
    injuries = []
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 1:
            injuries.append({"player": cells[0].text, "injury": cells[1].text})
    return injuries