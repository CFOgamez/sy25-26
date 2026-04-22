<<<<<<< HEAD
# ------------------------------------------------------ #
=======
import requests
import time
>>>>>>> main
import sys
from util import fetch_bookscrape # *\util\fetch_bookscrape.py
# from util import interface # *\util\interface.py
# ------------------------------------------------------ #

def app():
    html = fetch_bookscrape.load_bookscrape()
    if html is None:
        print("sowwy failed to load")
        sys.exit(1)

    print(html.prettify()[:500])

if __name__ == "__main__":
<<<<<<< HEAD
    app()
    # main loop
=======
    application = App()
    # main loop
>>>>>>> main
