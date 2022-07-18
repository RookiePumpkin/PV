import tkinter as tk

main = tk.Tk()
main.title("PumpkinVending")
main.geometry("350x400")
main.configure(background="Thistle")

class Selection:
    def increase():
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value + 1}"

    def decrease():
        value = int(lbl_value["text"])
        if value > 0:
            lbl_value["text"] = f"{value - 1}"

    def pick(name= ""):
        x= name
        l.config(text= x +" ürünü seçildi.")

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


btn_decrease = tk.Button(master=main, background="BlueViolet", foreground="White",  text="-", command=Selection.decrease)
btn_decrease.grid(row=3, column=0, sticky="nwse", pady=80)

lbl_value = tk.Label(master=main, background="DarkOrchid", foreground="White", text="0")
lbl_value.grid(row=3, column=1, sticky="nwse", pady=80)

btn_increase = tk.Button(master=main, background="BlueViolet", foreground="White", text="+", command=Selection.increase)
btn_increase.grid(row=3, column=2, sticky="nwse", pady=80)

l= tk.Label( text="abcd", background="DarkOrchid", foreground="White", highlightthickness=1)
l.place(x=0, y=350)

main.rowconfigure(0, minsize=20, weight=0)
main.columnconfigure([0, 1, 2, 3, 4], minsize=20, weight=0)

button1 = tk.Button(
    text= "Peynirli Crax",
    width=15,
    height=5,
    background="RoyalBlue",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Peynirli Crax")
)
button1.grid(row=0, column=0)

button2 = tk.Button(
    text="Labneli Galeta",
    width=15,
    height=5,
    background="Bisque",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Labneli Galeta")
)
button2.grid(row=0, column=1)

button3 = tk.Button(
    text="Fıstık Ezmeli Burçak",
    width=15,
    height=5,
    background="Peru",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Fıstık Ezmeli Burçak")
)
button3.grid(row=0, column=2)

button4 = tk.Button(
    text="Çikolatalı Burçak",
    width=15,
    height=5,
    background="SaddleBrown",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Çikolatalı Burçak")
)
button4.grid(row=1, column=0)

button5 = tk.Button(
    text="Bergamotlu Didi",
    width=15,
    height=5,
    background="Fuchsia",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Bergamotlu Didi")
)
button5.grid(row=1, column=1)

button6 = tk.Button(
    text="Sütlü Filtre Kahve",
    width=15,
    height=5,
    background="Tan",
    foreground="DarkSlateGray",
    command= Selection.pick(name="Sütlü Filtre Kahve")
)
button6.grid(row=1,column=2)


label = tk.Label(master=main, text="    Önce ürünü, ardından satın almak istediğiniz miktarı seçin.     ",
                  background="DarkOrchid", foreground="White", highlightthickness=1)
label.place(x=0, y=200)


main.mainloop()
