import tkinter as tk

def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1+s2))
def cikar():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1-s2))
def carpma():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1*s2))
def bolme():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1/s2))

pencere = tk.Tk()
pencere.title('Zeky Hesap Makinesi')
ekrangenis=pencere.winfo_screenwidth()//2-160
ekranyuksek=pencere.winfo_screenheight()//2-150
pencere.geometry("320x300+{}+{}".format(ekrangenis, ekranyuksek))

sonuc = tk.Label(pencere, text="Sonuc",font="Courier 16 bold", width=30, justify="center")
sonuc.place(x=-50, y=20)
sayi1 = tk.Entry(pencere, font="Courier 14 bold", width=15, justify="right")
sayi1.place(x=70, y=50)
sayi2 = tk.Entry(pencere, font="Courier 14 bold", width=15, justify="right")
sayi2.place(x=70, y=80)

tus1 = tk.Button(pencere, text="+", font="Courier 14 bold", width=10, command=topla)
tus1.place(x=90, y=110)
tus2 = tk.Button(pencere, text="-", font="Courier 14 bold", width=10, command=cikar)
tus2.place(x=90, y=150)
tus3 = tk.Button(pencere, text="*", font="Courier 14 bold", width=10, command=carpma)
tus3.place(x=90, y=190)
tus4 = tk.Button(pencere, text="/", font="Courier 14 bold", width=10, command=bolme)
tus4.place(x=90, y=230)

sayi1.focus()

pencere.mainloop()