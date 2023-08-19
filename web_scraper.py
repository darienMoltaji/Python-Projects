import json
import requests
from bs4 import BeautifulSoup

def scrape_hyperlinks():
    url = 'https://static.nytimes.com/email-content/RD_sample.html?action=click&module=nl-index-see-the-latest'
    response = requests.get(url)
    results = {"hyperlinks": []}
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        hyperlinks = soup.find_all('a')

        for hyperlink in hyperlinks:
            hyperlinks_text = hyperlink.attrs['href']
            results['hyperlinks'].append(hyperlinks_text)
            # print(f"{hyperlinks_text}\n")
        with open("hyperlinks.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(results))
    else:
        print("Failed to retrieve data from the website.")

if __name__ == "__main__":
    scrape_hyperlinks()