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

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    
    while(start<=end):
        print("Step", steps, ":" ,str(list[start:end+1]))
        steps = steps+1
        middle = (start + end // 2)

        if element == list[middle]  :
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            star = middle +1

    return -1


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12

binary_search(my_list, target)