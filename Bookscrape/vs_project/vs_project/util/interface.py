# ------------------------------------------------------ #
import select
import requests
import io
from PIL import Image
from util import fetch_bookscrape
import PySimpleGUI as psg
# ------------------------------------------------------ #

def text_to_number(text):
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    return number_map.get(text.lower(), None)

def display_book_details(book):
    image_data = None
    if book.get("img_url"):
        try:
            response = requests.get(book["img_url"])
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                image_data = io.BytesIO()
                image.save(image_data, format="PNG")
                image_data.seek(0)
        except Exception:
            image_data = None

    details_layout = [
        [psg.Text(f"Title: {book['title']}")],
        [psg.Text(f"Rating: {text_to_number(book['rating'])}/5 Stars")],
        [psg.Text(f"Price: {book['price']}")],
    ]
    if image_data:
        details_layout.append([psg.Image(data=image_data.getvalue())])
    details_layout.append([psg.Button("Close")])

    details_window = psg.Window("Book Details", details_layout)
    while True:
        event, _ = details_window.read()
        if event == psg.WINDOW_CLOSED or event == "Close":
            break
    details_window.close()

def build_interface(html,curr_page = 1):
    books = []
    for book in html.select(".product_pod"):
        title = book.h3.a["title"]
        rating = book.p["class"][1]
        price = book.select_one(".price_color").text.strip()
        img_tag = book.select_one(".image_container")
        img_url = img_tag.img["src"] if img_tag else ""
        if img_url and img_url.startswith("../"):
            img_url = "https://books.toscrape.com/" + img_url.replace("../", "")
        books.append({"title": title, "rating": rating, "price": price, "img_url": img_url})


    layout = [
        [psg.Text("Books to Scrape!")],
        [psg.Listbox(values=[book["title"] for book in books], size=(50,20), key="-BOOKS-", enable_events=True)],
        [psg.Button("Previous Page"), psg.Text(f"Pg {curr_page}"), psg.Button("Next Page")],
        [psg.Input(default_text=str(curr_page), size=(5,1), key='-INPUT-'), psg.Button("GO")],
        [psg.Button("Close")]
    ]
    window = psg.Window("My Window", layout)
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == "Close":
            break
        if event == "Next Page" or event == "Previous Page":
            if event == "Previous Page" and curr_page > 1:
                curr_page-=1
            elif event == "Next Page" and curr_page <= 50:
                curr_page+=1
            
            new_page = fetch_bookscrape.load_page(curr_page)
            if new_page:
                window.close()
                build_interface(new_page, curr_page)
                return
            else:
                psg.popup_error("Failed to load page! Please try again :(")
        if event == "GO":
            try:
                page_num = int(values['-INPUT-'])
                if 1 <= page_num <= 50:
                    new_page = fetch_bookscrape.load_page(page_num)
                    if new_page:
                        window.close()
                        build_interface(new_page, page_num)
                        return
                    else:
                        psg.popup_error("failed to load page! please try again :(")
                else:
                    psg.popup_error("please enter a valid page number between 1 and 50.")
            except ValueError:
                psg.popup_error("please enter a valid integer for the page number.")

        if event == "-BOOKS-":
            selected_book = values["-BOOKS-"][0] if values["-BOOKS-"] else None
            if selected_book:
                selected_book = next(book for book in books if book["title"] == selected_book)
                window.hide()
                display_book_details(selected_book)
                window.un_hide()

    window.close()