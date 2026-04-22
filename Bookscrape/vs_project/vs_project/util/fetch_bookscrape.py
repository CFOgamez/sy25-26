# ------------------------------------------------------ #
import requests
from bs4 import BeautifulSoup
# ------------------------------------------------------ #

def load_bookscrape():
    URL = "https://books.toscrape.com/"
    MAX_RETRY = 3

    for attempt in range(MAX_RETRY):
        print(f"attempting to fetch site ({attempt+1}/{MAX_RETRY})")
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                print("request to bookscrape successful")
                return BeautifulSoup(response.text, "html.parser")
                
            # if unexpected status code, retry
            print(f"err while requesting site, status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"request failed, {e}")

    return None