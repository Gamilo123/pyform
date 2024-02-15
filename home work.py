import re

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


def questionary():
    global name, last_name, age, email, phone
    name = input('Enter your name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    while True:
        if age.isdigit():
            break
        elif age.isalpha():
            print('Age is not a number')
            age = input('Enter your age: ')
        else:
            print('Age is not a integer, please enter a valid')
            age = input('Enter your age: ')
    while True:
        if validate_email_syntax(email):
            break
        else:
            print('Email is not valid')
            email = input('Enter your email: ')
    while True:
        if validate_phone_syntax(phone):
            break
        else:
            print('Phone is not valid')
            phone = input('Enter your phone: ')


def print_data():
    print('Name: ', name)
    print('Last name: ', last_name)
    print('Age: ', age)
    print('Email: ', email)
    print('Phone: ', phone)


def main():
    questionary()
    print_data()
    print('Thank you for your time')


if __name__ == "__main__":
    main()
