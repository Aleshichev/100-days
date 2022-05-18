from tkinter import *

def button_clicked():
    convert = round(float(input.get()) * 1.609)
    new_label.config(text=f"{convert}")
    print(convert)

window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(200, 100)
window.config(padx=10, pady=10)     # отступ

my_lable = Label(text="is equal to")
my_lable.grid(column=0, row=1)

miles_lable = Label(text="Miles")
miles_lable.grid(column=2, row=0)

new_label = Label(text="0")
new_label.grid(column=1, row=1)

km_lable = Label(text="Km")
km_lable.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

input = Entry(width=10)
input.insert(END, string="0")
input.get()
# input.pack()
input.grid(column=1, row=0)



window.mainloop()

