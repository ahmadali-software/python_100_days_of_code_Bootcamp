from tkinter import *

window =Tk()
window.title("NOT MY FIRST GUI")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

lable_miles = Label(text="Miles")
lable_miles.grid(row=1,column=3)

equal_text_lable = Label(text="is equal to ")
equal_text_lable.grid(row=2, column=1)

lable_km = Label(text="Km")
lable_km.grid(row=2, column=3)

output_lable = Label(text="0")
output_lable.grid(row=2, column=2)


def button_clicked():
    user_input = input.get()
    km = round((float(user_input) * 1.609), 2)
    output_lable.config(text=km)


button1 = Button(text="Calculate", command=button_clicked)
button1.grid(row=3, column=2)


input = Entry(width=10)
input.grid(row=1, column=2)
user_input = input.get()






window.mainloop()