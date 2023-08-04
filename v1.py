import pandas as pd
import requests
from bs4 import BeautifulSoup
print("Hey")
def scrape_app_info(url):
    try:
        # Send a GET request to the URL and fetch the HTML content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the main content element containing the app information
            main_content = soup.find('div', {'class': 'main-content'})  # Adjust class name accordingly

            # Extract the text from the main content
            app_info = main_content.get_text()

            return app_info
        else:
            print(f"Failed to fetch content for URL: {url}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching content for URL: {url}\n{e}")
        return None
    
    
sample_url = "https://www.metro-magazine.com/10032975/pilot-program-brings-cap-metro-bus-info-to-blind-visually-impaired"  # Replace this with the actual URL from your Excel sheet

app_info = scrape_app_info(sample_url)

if app_info:
    print(app_info)
else:
    print("Failed to retrieve app information.")