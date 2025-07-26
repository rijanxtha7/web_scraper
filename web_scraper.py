import sys
import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        print(f"Page title: {title}")
        a_tags = soup.find_all('a')
        p_tags = soup.find_all('p')
        div_tags = soup.find_all('div')
        print(f"Found {len(a_tags)} <a> links, {len(p_tags)} <p> tags, {len(div_tags)} <div> blocks")
        links = {a['href'] for a in a_tags if 'href' in a.attrs}
        for link in links:
            print(f"- {link}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scrape(sys.argv[1])
    else:
        print("Usage: python web_scraper.py <URL>")
