import time
#import urllib
import bs4
import requests

# Initialize starting url
wish_list_url = "https://www.amazon.com/gp/registry/wishlist/28Q24IH2QSNHU/"

# load url into soup object
response = requests.get(wish_list_url)
time.sleep(1)
html = response.content
soup = bs4.BeautifulSoup(html, "html.parser")

# Scrape lek from current website
lek = soup.find(id="sort-by-price-next-batch-lek")['value']
