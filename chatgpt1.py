import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

base_url = "https://www.olx.com.eg/en/ads/q-car/"
page = 1
car_ads = []

while True:
    url = urljoin(base_url, f"?page={page}")
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.content, "html.parser")
    ads = soup.find_all("li", {"aria-label": "Listing"})

    if not ads:
        break

    car_ads.extend(ads)
    page += 1


with open("car_ads.json", "w", encoding="utf-8") as jsonfile:
    json.dump([str(ad) for ad in car_ads], jsonfile)


with open("car_prices.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Car Name", "Price"])

    for ad in car_ads:
        title = ad.find("div", {"aria-label": "Title"})
        if title is not None:
            name = title.text.strip()
        else:
            name = ""

        price = ad.find("div", {"aria-label": "Price"}).text.strip()
        writer.writerow([name, price])
