import requests
from bs4 import BeautifulSoup

def MetroMag_scrapper(url):
    sample_url = url
    page = requests.get(sample_url)

    soup = BeautifulSoup(page.content, "html.parser")

    #content = soup.find('div', class_="content-body")

    text = []
    
    for content in soup:
        text_data = soup.text.strip()
        text.append(text_data)

    return text

#print(MetroMag_scrapper("https://www.metrotransit.org/aira-navigation"))