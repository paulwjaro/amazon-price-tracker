from tkinter import *


class Popup:
    def __init__(self, item, price):
        self.window = Tk()
        self.window.title("Price Adjustment")
        self.window.config(padx=160, pady=144)

        self.message = Label(text=f"Amazon has made a price adjustment to your item. \n\n Item: {item} \n\n Current Price: "
                                  f"{price}")
        self.message.pack()

    def fail_message(self):
        self.window = Tk()
        self.window.title("Full Price")
        self.window.config(padx=160, pady=144)

        self.message = Label(
            text="Item currently above your searched price.")
        self.message.pack()


