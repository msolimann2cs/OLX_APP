import csv
import json
from bs4 import BeautifulSoup

with open("car_ads.json", "r", encoding="utf-8") as jsonfile:
    car_ads = [BeautifulSoup(ad, "html.parser") for ad in json.load(jsonfile)]

#print(car_ads)

with open("car_prices.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Car Name", "Price"])

    for ad in car_ads:
        title = ad.find("div", {"aria-label": "Title"})
        if title is not None:
            name = title.text.strip()
        else:
            name = ""

        price_parent = ad.find("div", {"aria-label": "Price"}) #.text.strip()
        if price_parent is not None:
            price = price_parent.find("span").text.strip()
        #print(price_parent)

        writer.writerow([name, price])
