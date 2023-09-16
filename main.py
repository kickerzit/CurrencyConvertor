from tkinter import *

# Okno
window = Tk()
window.title("Převod měn z CZK na Eura")
window.minsize(200, 200)
window.resizable(False, False)
window.config(bg="#be4d05")
window.iconbitmap("icon.ico")

# 1 Euro = 24,55 CZK
# Funkce
def count_currency():
    amount_eur = float(amount_input.get()) / 24.55
    result_label["text"] = round(amount_eur, 2)


# Vstup od uživatele
amount_input = Entry(width="10", font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

# Label
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#be4d05", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Helvetica", 15), bg="#be4d05", fg="white")
result_label.grid(row=1, column=0)

eur_label = Label(text="EUR", font=("Helvetica", 15), bg="#be4d05", fg="white")
eur_label.grid(row=1, column=1)

# Tlačítko
count_button = Button(text="Převést", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)

# Hlavní cyklus
window.mainloop()

# pro převod do exe nainstalovat 'pip install auto-py-to-exe' (je nutné mít Visual Studio 14 a vyšší)
# spustíme auto-py-to-exe