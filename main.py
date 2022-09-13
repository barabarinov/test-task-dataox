from bs4 import BeautifulSoup
import requests
from datetime import datetime
import concurrent.futures
import json

MAX_NUMBER_OF_PAGES = 100
CONNECTIONS = 10
TIMEOUT = 10


def parse_page(page_number):
    print(f"Doing request to page {page_number}")
    response = requests.get(
        f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_number + 1}/c37l1700273",
        allow_redirects=page_number == 0,
        timeout=TIMEOUT,
    )
    print(f"Got request from page {page_number} with status", response.status_code)
    if response.status_code == 302:
        print("Reached the end of pages")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("div.search-item")
    out = []
    for item in items:
        images = item.select("picture > img")
        if len(images) == 0:
            image_link = item.select("img")[0].get("src")
        else:
            image_link = images[0].get("data-src")
        title = item.select("a.title")[0].get_text().strip()
        date_posted_text = item.select("span.date-posted")[0].get_text().strip()
        try:
            date_posted = datetime.strptime(date_posted_text, "%d/%m/%Y").strftime(
                "%d-%m-%Y"
            )
        except ValueError:
            # print(f"Unable to parse '{date_posted_text}' in '%d/%m/%Y' format")
            date_posted = date_posted_text
        location = item.select("div.location > span")[0].get_text().strip()
        number_of_beds = (
            item.select("div.rental-info > span.bedrooms")[0]
            .get_text()
            .strip()
            .split("\n")[-1]
            .strip()
        )
        description = item.select("div.description")[0].get_text().strip()
        price_text = item.select("div.price")[0].get_text().strip()
        try:
            currency, price = price_text[:1], float(price_text[1:].replace(",", ""))
        except ValueError:
            # print(f"Unable to parse '{price_text}' in format for number")
            currency, price = None, price_text
        out.append((image_link, title, date_posted, location, number_of_beds, description, currency, price))
    return json.dumps(out)


def main():
    out = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(parse_page, page) for page in range(MAX_NUMBER_OF_PAGES))
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                print(f"Got error from future: {exc}")
            else:
                out.append(json.loads(data))

    print(out)


if __name__ == "__main__":
    main()
