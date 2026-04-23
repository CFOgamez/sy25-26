# ------------------------------------------------------ #
import select
import PySimpleGUI as psg
# ------------------------------------------------------ #

def display_book_details(book):
    details_layout = [
        [psg.Text(f"Title: {book['title']}")],
        [psg.Text(f"Rating: {book['rating']}")],
        [psg.Text(f"Price: {book['price']}")],
        [psg.Button("Close")]
    ]
    details_window = psg.Window("Book Details", details_layout)
    while True:
        event, _ = details_window.read()
        if event == psg.WINDOW_CLOSED or event == "Close":
            break
    details_window.close()

def build_interface(html):
    books = []
    for book in html.select(".product_pod"):
        title = book.h3.a["title"]
        rating = book.p["class"][1]
        price = book.select_one(".price_color").text.strip()
        books.append({"title": title, "rating": rating, "price": price})


    layout = [
        [psg.Text("Bookscrape Application")],
        [psg.Listbox(values=[book["title"] for book in books], size=(50,20), key="-BOOKS-", enable_events=True)],
        [psg.Button("Close")]
    ]
    window = psg.Window("My Window", layout)
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == "Close":
            break
        if event == "-BOOKS-":
            selected_book = values["-BOOKS-"][0] if values["-BOOKS-"] else None
            if selected_book:
                selected_book = next(book for book in books if book["title"] == selected_book)
                window.hide()
                display_book_details(selected_book)
                window.un_hide()

    window.close()