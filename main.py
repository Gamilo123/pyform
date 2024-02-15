frase1 = "gamilo es el mejor"
print(type(frase1))
#when I find a frase i trust you
numero = 15
print(type(numero))
#comentamos
flotante = 3.1416
print(type(flotante))
#buleano owo
buleano = False
print(type(buleano))


def pr_and_ty(object):
    print(object)
    print(type(object))


#actions
pr_and_ty('owowo')
pr_and_ty('15')
pr_and_ty('3.14')
pr_and_ty(True)

#5 datos formulario tarea mañana
#do something with os library
number1 = input('enter the first number:')
number2 = input('enter the second number')
int_number1 = int(number1)
int_number2 = int(number2)

def menu():
    print("Choose an option:")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print(int_number1 + int_number2)

        elif choice == "2":
            print(int_number1 - int_number2)


        elif choice == "3":
            print(int_number1 * int_number2)


        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break


main()



