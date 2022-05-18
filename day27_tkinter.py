import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

my_lable = tkinter.Label(text="I Am a lable", font=("Arial", 20, "bold"))
my_lable.pack()

window.mainloop()


