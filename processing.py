import pandas as pd
from scraper import MetroMag_scrapper

data = pd.read_excel(r"C:\Users\akobe\OneDrive - McGill University\Navigation Apps by City (1).xlsx")

scraped_texts = []

# Iterate through the DataFrame rows to extract and scrape URLs
for index, row in data.iterrows():
    url = row['Link']
    text = MetroMag_scrapper(url)
    scraped_texts.append(text)

# Add the scraped text as a new column in the DataFrame
data['scraped_text'] = scraped_texts

data.to_excel(fr".\output\data.xlsx", index=False)


print(data.isna().sum())