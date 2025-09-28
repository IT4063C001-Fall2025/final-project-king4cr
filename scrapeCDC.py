import requests
from bs4 import BeautifulSoup

def scrape_cdc_screen_time(url="https://www.cdc.gov/nchs/products/databriefs/db513.htm"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cdc_text = soup.get_text()
    print("CDC screen time page scraped.\n")
    return cdc_text

cdc_text = scrape_cdc_screen_time()

print(cdc_text)  