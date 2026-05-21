import tkinter as tk
from tkinter import ttk
import math

# fungsi perhitungan
def present_value():
    try:
        FV = float(entry1.get())
        i = float(entry2.get()) / 100
        n = float(entry3.get())

        PV = FV / ((1 + i) ** n)

        hasil.config(text=f"Present Value = {PV:.2f}")
    except:
        hasil.config(text="Input salah")

def future_value():
    try:
        PV = float(entry1.get())
        i = float(entry2.get()) / 100
        n = float(entry3.get())

        FV = PV * ((1 + i) ** n)

        hasil.config(text=f"Future Value = {FV:.2f}")
    except:
        hasil.config(text="Input salah")

def annuity():
    try:
        P = float(entry1.get())
        i = float(entry2.get()) / 100
        n = float(entry3.get())

        A = P * ((1 - (1+i)**(-n))/i)

        hasil.config(text=f"Nilai Anuitas = {A:.2f}")
    except:
        hasil.config(text="Input salah")


# GUI
root = tk.Tk()
root.title("Kalkulator Matematika Aktuaria")
root.geometry("400x400")

judul = tk.Label(root, text="Aplikasi Aktuaria", font=("Arial",16))
judul.pack(pady=10)

tk.Label(root, text="Nilai / Premi").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Suku bunga (%)").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Periode (n)").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(root, text="Present Value", command=present_value).pack(pady=5)
tk.Button(root, text="Future Value", command=future_value).pack(pady=5)
tk.Button(root, text="Anuitas", command=annuity).pack(pady=5)

hasil = tk.Label(root, text="", font=("Arial",12))
hasil.pack(pady=20)

root.mainloop()