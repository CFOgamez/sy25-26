"""
 ____  ____  _      _____    _____ _     ____  _  __   _      _ _____ _       _     ___  _   ____  ____  ____  _____
/  _ \/  _ \/ \  /|/__ __\  /    // \ /\/   _\/ |/ /  / \  /|/ Y__ __Y \ /|  / \__/|\  \//  /   _\/  _ \/  _ \/  __/
| | \|| / \|| |\ ||  / \    |  __\| | |||  /  |   /   | |  ||| | / \ | |_||  | |\/|| \  /   |  /  | / \|| | \||  \  
| |_/|| \_/|| | \||  | |    | |   | \_/||  \__|   \   | |/\||| | | | | | ||  | |  || / /    |  \__| \_/|| |_/||  /_ 
\____/\____/\_/  \|  \_/    \_/   \____/\____/\_|\_\  \_/  \|\_/ \_/ \_/ \|  \_/  \|/_/     \____/\____/\____/\_____
"""
import requests
import time
import sys
from bs4 import BeautifulSoup

class App():
    def __init__(self):
        # Start application
        self.interface()

    def interface(self):
        site = self.load_bookscrape()
        if site:
            print("site loaded")
            print("page title:", site.title.string)
        else:
            print("\nFAILED TO LOAD SITE! PROGRAM WILL CLOSE!!! sowwy :3")
            sys.exit()

    def load_bookscrape(self):
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

if __name__ == "__main__":
    application = App()
    # main loop