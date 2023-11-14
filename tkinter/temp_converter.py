import tkinter as tk

def to_fah():
    deg = float(ent.get())
    deg = round((deg*9/5)+32, 2)
    answer["text"] = f"{deg}" + " F"

def to_cel():
    deg = float(ent.get())
    deg = round((deg-32)*5/9, 2)
    answer["text"] = f"{deg}" + " C"

windows = tk.Tk()
windows.title("Temperature Converter")
windows.rowconfigure([0,1,2], minsize=50, weight=1)
windows.columnconfigure([0,1], minsize=100, weight=1)

lbl = tk.Label(master=windows, text="Enter Temperature: ")
lbl.grid(row=0, column=0, sticky="e")

ent = tk.Entry(master=windows)
ent.grid(row=0, column=1)

result = tk.Label(master=windows, text="Result: ")
result.grid(row=1, column=0, sticky="e")

answer = tk.Label(master=windows, text="")
answer.grid(row=1, column=1)

btn_cel = tk.Button(master=windows, text="To Celsius", command=to_cel)
btn_cel.grid(row=2, column=0)

btn_fah = tk.Button(master=windows, text="To Fahrenheit", command=to_fah)
btn_fah.grid(row=2, column=1)

windows.mainloop()
