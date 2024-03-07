from tkinter import *
# another module of code, not classes or constant
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found Yet")
    else:
        website = website_input.get()
        if website in data.keys():
            is_ok = messagebox.showinfo(title=website, message=f"These are the details entered: "
                                                         f"\nEmail: {data[website].get('email')} \nPassword: "
                                                         f"{data[website].get('password')} \n")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_in = website_input.get()
    email_in = email_input.get()
    password_in = password_input.get()
    # initialize the new data dictionary
    new_data = {
       website_in: {
            "email": email_in,
            "password": password_in,
       }
    }
    if len(website_in) == 0 or len(password_in) == 0:
        null_box = messagebox.showinfo(title="Oops", message=f"Please dont leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=website_in, message=f"These are the details entered: "
        #                                              f"\nEmail: {email_in} \nPassword: "
        #                                              f"{password_in} \nIs it ok to save?")
        # if is_ok: #check with the assumption that it is ok
        try:
            with open("data.json", mode="r") as f:
                # Reading old data file
                data = json.load(f)
            # using json so don't need to write the below line:
            # f.write(f"{website_in}  |  {email_in}  |  {password_in}\n")
            # json.dump(new_data, f, indent=4)
            # data = json.load(f)
            # print(data)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            # Saving updated data
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            email_input.insert(0, "phuc.le.it96@gmail.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Protector")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "phuc.le.it96@gmail.com")
password_input = Entry(width=17)
password_input.grid(column=1, row=3)
# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()