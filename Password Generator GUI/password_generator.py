from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2,4))]

password_list = password_letters + password_symbols + password_numbers
shuffle(password_list)

password = "".join(password_list)


def generate_password() :
    password_input.insert(0,password)

# Add Data Button
def add_data() :
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website : {
        "email" : email,
        "password" : password
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password)== 0 :
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty. ")
    else :
        try :
            with open("data.json","r") as data_file :
                # Reading old data
                data = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):  # Handle missing or empty file
            data = {}
        
            # Updating old data with new data
        data.update(new_data)

        with open("data.json","w") as data_file :
                # Saving updated data
                json.dump(data, data_file, indent=4)
       
        website_input.delete(0,END)
        email_input.delete(0,END)
        password_input.delete(0,END)



def find_password() :
    website = website_input.get()
    try : 
         with open("data.json") as data_file :
            data = json.load(data_file)
    except FileNotFoundError :
        messagebox.showinfo(title="Error",message="No Data File Found")
    else :
        if website in data :
            email = data[website]["email"] 
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else :
            messagebox.showinfo(title="Error", message=f"No details for {website} exists. ")
        


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_input = Entry(width=35)
website_input.grid(row=1,column=1)
website_input.focus()

search_button = Button(text="Search",command=find_password)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_input = Entry(width=35)
email_input.grid(column=1,row=2)


password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_input = Entry(width=21)
password_input.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=add_data)
add_button.grid(column=1,row=4,columnspan=2)

canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="Tkinter/logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1, row=0)

window.mainloop()
