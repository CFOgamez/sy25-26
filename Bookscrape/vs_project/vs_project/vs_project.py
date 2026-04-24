# ------------------------------------------------------ #
import sys
from util import fetch_bookscrape # *\util\fetch_bookscrape.py
from util import interface # *\util\interface.py
# ------------------------------------------------------ #

def app():
    html = fetch_bookscrape.load_page(1)
    if html is None:
        print("Failed to load page! Application will close...")
        sys.exit(1)

    interface.build_interface(html,1)

if __name__ == "__main__":
    app()
