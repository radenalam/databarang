from tkinter import *
from tkinter import Label
from tkinter import Text
from tkinter import ttk
from tkinter import messagebox


window = Tk()

# defining variables
Product_id = StringVar()
Product_name = StringVar()
Selling_price = StringVar()
Quantity = StringVar()

window.geometry("600x400")
window.title("Inventory Management")


def insert():

    productid = Product_id.get()
    productname = Product_name.get()
    sellingprice = Selling_price.get()
    quantity = Quantity.get()
    file = open("list.txt", 'a')
    file = open("list.txt", "a")
    file.write(productid + "\t" +productname + "\t" + "\t"+sellingprice + "\t" + "\t"+quantity + "\n")
    messagebox.showinfo('successfull', "successfully")
 

def show():
    file = open("list.txt", 'r')
    read = file.read()
    for a in read[::-1]:
        display.insert(0.0, a)
        
def clear():
    display.delete(1.0, END)

# label entities
IM = Label(master=window, text="Data Barang\t", fg="black", bg="white", relief=RAISED, font=("calibry", 12))
IM.place(x=10, y=1)

Product_list = Label(master=window, text="Daftar Barang\t", fg="black", bg="white", relief=RAISED,
                     font=("arial", 12))
Product_list.place(x=360, y=1)

prod_id = Label(master=window, text="kode produk:", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
prod_id.place(x=10, y=40)
id = Entry(window, textvar=Product_id)
id.place(x=2, y=70)

prod_name = Label(master=window, text="Nama Barang:", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
prod_name.place(x=10, y=110)
pro_name = Entry(window, textvar=Product_name)
pro_name.place(x=2, y=140)

sell_price = Label(master=window, text="Harga Barang:", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
sell_price.place(x=10, y=180)
sp = Entry(window, textvar=Selling_price)
sp.place(x=2, y=210)
quant = Label(master=window, text="Jumlah:", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
quant.place(x=10, y=250)
quan = Entry(window, textvar=Quantity)
quan.place(x=2, y=280)

itemno = Label(master=window, text="Kode Produk:\t", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
itemno.place(x=230, y=40)

prdid = Label(master=window, text="Nama Barang:\t", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
prdid.place(x=300, y=40)

nameid = Label(master=window, text="Harga Barang:\t", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
nameid.place(x=410, y=40)

spid = Label(master=window, text="Jumlah:\t", fg="white", bg="grey", relief=FLAT, font=("calibry", 8))
spid.place(x=490, y=40)

Insert = ttk.Button(window, text='Insert', command=insert)
Insert.place(x=2, y=320)

Clear = ttk.Button(window, text='Clear', command=clear)
Clear.place(x=360, y=340)

shw = ttk.Button(window, text="Show", command=show)
shw.place(x=100, y=320)

display = Text(window, width=43, height=20, bg='light grey')
display.place(x=230, y=70)


window.mainloop()