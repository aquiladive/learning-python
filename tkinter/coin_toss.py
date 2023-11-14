import tkinter as tk
import random

def toss():
    n = random.randint(0,1)
    if n == 0:
        lbl["text"] = "Heads"
    else:
        lbl["text"] = "Tails"

windows = tk.Tk()
windows.title("Coin Toss")
windows.rowconfigure([0,1], weight=1, minsize=50)
windows.columnconfigure(0, weight=1, minsize=50)

btn_roll = tk.Button(master=windows, text="Toss the Coin", command=toss)
btn_roll.grid(row=0, column=0)

lbl = tk.Label(text="")
lbl.grid(row=1, column=0)

windows.mainloop()
