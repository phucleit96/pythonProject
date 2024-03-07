from tkinter import *


def calculate():
    miles_num = float(input.get())
    km_num = miles_num * 1.609344
    value.config(text=str("{:.2f}".format(km_num)))

# FONT = ("Arial", 18, "normal")
window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")


miles = Label(text="Miles")
miles.grid(row=0, column=2)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)


input = Entry(width=7)
input.grid(row=0, column=1)
input.insert(END, string="0")

km = Label(text="Km")
km.grid(row=1, column=2)


value = Label(text="0")
value.grid(row=1, column=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)
window.mainloop()