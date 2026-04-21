# I am organizing my code in a certain way. Don't fuck with my code
import requests
from bs4 import BeautifulSoup

class App():
    def __init__(self):
        # Start application
        self.load_bookscrape()

    def interface(self):
        print("Load interface")

    def load_bookscrape(self):
        URL = "https://books.toscrape.com/"
        response = requests.get(URL)
        
        if response.status_code == 200:
            print("Request to Bookscrape successful")
        else:
            print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    application = App()
    # main loop