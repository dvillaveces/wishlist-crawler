import time
#import urllib
import bs4
import requests

# Initialize starting url
url = "https://www.amazon.com/gp/registry/wishlist/28Q24IH2QSNHU/"

# load url into soup object
def load_soup(url):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        time.sleep(1.5)
        html = response.content
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup
    else:
        return load_soup(url)

def get_next_url(soup):
    # Scrape lek from current website
    try:
        lek = soup.find(id="sort-by-price-next-batch-lek")["value"]
    except KeyError:
        lek = ""

    # Compose next url using lek
    next_url = "https://www.amazon.com/hz/wishlist/ls/28Q24IH2QSNHU?filter=DEFAULT&lek="+lek+"&sort=default&type=wishlist&ajax=true"
    return next_url

# Scrape items and prices
def get_data(soup):
    items = soup.select("a[id^='itemName']")
    prices = soup.select("span[id^='itemPrice'] > .a-offscreen")
    return items, prices

# Print item title and price
def print_data(items, prices):
    for item, price in zip(items, prices):
        print(item.attrs["title"], end=" - ")
        print(price.text)

end = None
while not end:
    soup = load_soup(url)
    url = get_next_url(soup)
    items, prices = get_data(soup)
    print_data(items, prices)
    end = soup.find(id="endOfListMarker")
