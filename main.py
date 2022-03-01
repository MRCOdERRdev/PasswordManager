#-----------------------------Find Password----------------------------#
def find_password():
    website_name=website_entry.get()
    with open("C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\myfile.json","r") as search_file:
        data= json.load(search_file)
    try:
     if website_name in data: 
          
               website_name=data.get(website_name)
               password=website_name["password"]

               messagebox.showinfo(title="password",message=f"the password is {password}")
     else:
               messagebox.showerror(message="This website is not valid, please try again")
               
    except KeyError:      
          pass
        


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json
from tkinter.ttk import Style
import pyperclip
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password= "".join(password_list)
    password_entry.insert(END,string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #




default_email= "tanmay12ta@gmail.com"
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\myfile.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            with open("C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\myfile.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\myfile.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            email_entry.delete(0,END)
            email_entry.insert(END,default_email)
                    
            messagebox.showinfo(title="Task Successful", message="The credentials are saved in a highly protective file\nAlso we have copied the password into your clipboard")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import messagebox
from tkinter import *
from tkinter import font
bg_color="white"
window = Tk()
window.title("Password Manager")
window.config(padx=60,pady=60, bg="white")

canvas= Canvas(width=200,height=200, bg="white",highlightthickness=0 )
logo_img=PhotoImage(file="C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
#---------------------------Text Label---------------------------------#
website_label=Label(text="Website:", font=(20), bg=bg_color)
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:", font=(20), bg=bg_color)
email_label.grid(row=2,column=0)

password_label=Label(text="Password:", font=(20), bg=bg_color)
password_label.grid(row=3,column=0)

#---------------------------Entry-------------------------------#

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,ipadx=15)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2, ipadx=90)
email_entry.insert(END,string=default_email)
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1, ipadx=54)

#--------------------------Buttons------------------------------#
from tkinter.ttk import*
style= Style()
style.configure('W.TButton', font=('calibri',10,'bold'), foreground='black',background="blue")
generate_password_button=Button(style='W.TButton',text="Generate Password", command=gen_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(width=36,text="Add", style='W.TButton',command=save)
add_button.grid(row=4,column=1, columnspan=2)

def browsefile():
    from subprocess import call
    call("notepad C:\\Users\\tanma\\.vscode\\100DAYSOFCODE\\Password Manager\\myfile.json",shell=False)
show_file_button=Button(style='W.TButton',text="Show my Passwords",command=browsefile)
show_file_button.grid(row=0,column=0)

search_button= Button(style='W.TButton',text="SEARCH", command=find_password)
search_button.grid(row=1, column=2, ipadx=30)


window.mainloop()