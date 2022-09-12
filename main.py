from bs4 import BeautifulSoup
import requests
from datetime import datetime


response = requests.get("https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273")
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.select("div.search-item")


for item in items:
    images = item.select("picture > img")
    if len(images) == 0:
        image_link = item.select("img")[0].get('src')
    else:
        image_link = images[0].get('data-src')
    title = item.select("a.title")[0].get_text().strip()
    date_posted_text = item.select("span.date-posted")[0].get_text().strip()
    try:
        date_posted = datetime.strptime(date_posted_text, "%d/%m/%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(f"Unable to parse '{date_posted_text}' in '%d/%m/%Y' format")
        date_posted = date_posted_text
    location = item.select("div.location > span")[0].get_text().strip()
    number_of_beds = item.select("div.rental-info > span.bedrooms")[0].get_text().strip().split("\n")[-1].strip()
    description = item.select("div.description")[0].get_text().strip()
    price_text = item.select("div.price")[0].get_text().strip()
    try:
        currency, price = price_text[:1], float(price_text[1:].replace(",", ""))
    except ValueError:
        print(f"Unable to parse '{price_text}' in format for number")
        currency, price = "Unknown", price_text
