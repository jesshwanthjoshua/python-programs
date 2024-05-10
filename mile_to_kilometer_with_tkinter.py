from tkinter import *

window = Tk()
window.minsize(height=100, width=200)
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

def calculate():
    mile = int(input_1.get())
    kilometer = round((mile * 1.609),2)
    label_3.config(text = kilometer)

input_1 = Entry(width = 10)
input_1.insert(END, 0)
input_1.grid(column= 1, row = 0)

label_1 = Label(text="Miles")
label_1.grid(column= 2, row = 0)

label_2 = Label(text="is equal to")
label_2.grid(column= 0, row = 1)

label_3 = Label(text= "0")
label_3.grid(column= 1, row = 1)

label_4 = Label(text="Km")
label_4.grid(column= 2, row = 1)

button = Button(text= "Calculate", width=8, command= calculate)
button.grid(column = 1, row = 2)

window.mainloop()