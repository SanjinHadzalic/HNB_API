import tkinter
import datetime as dt


class Window:

    def __init__(self):
        self.kup_tecaj = "kup_tecaj"
        self.sred_tecaj = "sred_tecaj"
        self.prod_tecaj = "prod_tecaj"

        self.window = tkinter.Tk()
        self.window.title("HNB API")
        self.window.geometry("400x450")

        self.date = tkinter.Label(text="Date (YYYY-MM-DD): ", pady=10, padx=10)  # ISO 8601 standard
        self.date.grid(row=0, column=0)

        self.date_entry = tkinter.Entry()
        self.date_entry.grid(row=0, column=1)
        self.date_entry.focus()

        self.local = ""
        self.currency_local = ""

        def add_date():
            self.local = self.date_entry.get()

        self.date_user_button = tkinter.Button(text="Add", command=add_date)
        self.date_user_button.grid(row=0, column=2)

        def set_today():
            self.date_entry.insert(0, f"{dt.datetime.now():%Y-%m-%d}")
            self.local = self.date_entry.get()

        self.date_today_button = tkinter.Button(text="Today", command=set_today)
        self.date_today_button.grid(row=0, column=3)

        self.currency = tkinter.Label(text="Currency: ")
        self.currency.grid(row=1, column=0)

        def show():
            self.label.config(text=self.clicked.get())
            self.currency_local = self.label.cget("text")

        self.options = [
            "AUD",
            "CAD",
            "CZK",
            "DKK",
            "HUF",
            "JPY",
            "NOK",
            "SEK",
            "CHF",
            "GBP",
            "USD",
            "XDR",
            "BAM",
            "EUR",
            "PLN"
        ]

        self.clicked = tkinter.StringVar()
        self.clicked.set("Choose")

        self.drop = tkinter.OptionMenu(self.window, self.clicked, *self.options)
        self.drop.grid(row=2, column=0)

        self.button = tkinter.Button(self.window, text="Set Currency", command=show)
        self.button.grid(row=2, column=1)

        self.label = tkinter.Label(self.window, text="")
        self.label.grid(row=2, column=2)

        self.window.mainloop()
