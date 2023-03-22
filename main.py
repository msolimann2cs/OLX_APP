import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.olx.com.eg/en/ads/q-car/?sorting=desc-price")

OLX_webpage = response.text

soup = BeautifulSoup(OLX_webpage, "html.parser")

# car_tag = soup.find(name = "div", class_ = "a5112ca8")
# t = car_tag.get_text()

all_listings = soup.find_all(name = "li", attrs={"aria-label": True})
for tag in all_listings:
    print(tag.text.strip())
#print(all_listings)