# ------------------------------------------------------ #
import sys
from util import fetch_bookscrape # *\util\fetch_bookscrape.py
from util import interface # *\util\interface.py
# ------------------------------------------------------ #

def app():
    html = fetch_bookscrape.load_bookscrape()
    if html is None:
        print("Failed to load html! Application will close...")
        sys.exit(1)

    interface.build_interface(html)

if __name__ == "__main__":
    app()
