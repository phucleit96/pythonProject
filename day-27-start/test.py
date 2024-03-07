from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Phuc's GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# Create a label, then decide how that component will be laid out on screen --> pack()
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text", padx=50, pady=50)
# my_label.pack()
# my_label.place(x=100, y=200)
# my_label["text"] = True
my_label.grid(column=0, row=0)
# import turtle
# tim = turtle.Turtle()
# tim.write()

# the name of the function, not calling the function, so don't need parentheses


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
#Entry

input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop() # at the very end