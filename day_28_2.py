from tkinter import *

def button_clicked():
    my_lable["text"] = input.get()
    print("I got clicked")

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=200)     # отступ

my_lable = Label(text="I Am a lable", font=("Arial", 20, "bold"))
my_lable["text"] = "New Text"      # меняем свойства
my_lable.config(text="New Text")     # меняем свойства
# my_lable.pack()
# my_lable.place(x=100, y=200)
my_lable.grid(column=0, row=0)


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

input = Entry(width=10)
input.get()
# input.pack()
input.grid(column=3, row=2)

new_button = Button(text="New Buttom")
# button.pack()
new_button.grid(column=2, row=0)


window.mainloop()

