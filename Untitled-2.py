def add(a, b):
    answer = a + b
    print(str(a) + " + "  + str(b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b)  + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b)  + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Subtration")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("input ypur choice: ")
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input fist number: "))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input firs number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("progran ended")
        quit()