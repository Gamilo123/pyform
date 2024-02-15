import re
import tkinter
import customtkinter

name = 'guest'
last_name = 'guest'
age = 0
email = 'guest'
phone = 0


def validate_email_syntax(email_1):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email_1) is not None


def validate_phone_syntax(phone_1):
    pattern = r"^[0-9]{9}$"
    return re.match(pattern, phone_1) is not None



def validate():
    try:
        age = age_tkinter.get()
        if age.isdigit():
            pop_invalid.configure(text='')
            pass
        elif age.isalpha():
            pop_invalid.configure(text='Age is not a number', text_color='red')
            return
        else:
            pop_invalid.configure(text='Age is not a integer, please enter a valid', text_color='red')
            return
    except ValueError:
        pop_invalid.configure(text='Age is not a integer, please enter a valid', text_color='red')
        return
    try:
        email = email_tkinter.get()
        if validate_email_syntax(email):
            pop_invalid.configure(text='')
            pass
        else:
            pop_invalid.configure(text='Email is not valid', text_color='red')
            return
    except ValueError:
        pop_invalid.configure(text='Email is not valid', text_color='red')
        return
    try:
        phone = phone_tkinter.get()
        if validate_phone_syntax(phone):
            pop_invalid.configure(text='')
            pass
        else:
            pop_invalid.configure(text='Phone is not valid', text_color='red')
            return
    except ValueError:
        pop_invalid.configure(text='Phone is not valid', text_color='red')
        return
    pop_invalid.configure(text='thanks for your data', text_color='green')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x650')
app.title('Questionary')

pop_invalid = customtkinter.CTkLabel(app, text='')
pop_invalid.pack()

title = customtkinter.CTkLabel(app, text='Questionary', font=('Arial', 20))
title.pack(padx=10, pady=10)

name_title = customtkinter.CTkLabel(app, text='Name:', font=('Arial', 15))
name_title.pack(padx=1, pady=1)
name_var = tkinter.StringVar()
name_tkinter = customtkinter.CTkEntry(app, width=200, height=30, textvariable=name_var, font=('Arial', 15))
name_tkinter.pack(padx=10, pady=10)

last_name_title = customtkinter.CTkLabel(app, text='Last name:', font=('Arial', 15))
last_name_title.pack(padx=1, pady=1)
last_name_var = tkinter.StringVar()
last_name_tkinter = customtkinter.CTkEntry(app, width=200, height=30, textvariable=last_name_var, font=('Arial', 15))
last_name_tkinter.pack(padx=10, pady=10)

age_title = customtkinter.CTkLabel(app, text='Age:', font=('Arial', 15))
age_title.pack(padx=1, pady=1)
age_var = tkinter.StringVar()
age_tkinter = customtkinter.CTkEntry(app, width=200, height=30, textvariable=age_var, font=('Arial', 15))
age_tkinter.pack(padx=10, pady=10)

email_title = customtkinter.CTkLabel(app, text='Email:', font=('Arial', 15))
email_title.pack(padx=1, pady=1)
email_var = tkinter.StringVar()
email_tkinter = customtkinter.CTkEntry(app, width=200, height=30, textvariable=email_var, font=('Arial', 15))
email_tkinter.pack(padx=10, pady=10)

phone_title = customtkinter.CTkLabel(app, text='Phone:', font=('Arial', 15))
phone_title.pack(padx=1, pady=1)
phone_var = tkinter.StringVar()
phone_tkinter = customtkinter.CTkEntry(app, width=200, height=30, textvariable=phone_var, font=('Arial', 15))
phone_tkinter.pack(padx=10, pady=10)

validation = customtkinter.CTkButton(app, text='Validate', font=('Arial', 15), command=validate)
validation.pack(padx=10, pady=10)

app.mainloop()
