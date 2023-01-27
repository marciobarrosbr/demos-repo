import random

exit = False
user_input = 0
compuer_input = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choise rosh, paper, scissores or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("game ended")
        print("you won a total score of " +str(user_points)+" and the computer total score is" +str(computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("computer_input is rock")
            print("it is a tie!")
        elif computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer win")
            computer_points += 1
        elif computer_input == "scissors":
            print("your input is rock")
            print("computer input is scissors")
            print("you win")
            user_input += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input is paper")
            print("you win!")
            user_input += 1
        elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("it is a tie!")
        elif computer_input  == "scissors":
            print("your input is paper")
            print("computer input is scissors")
            print("computer wins!")
            computer_input += 1
    
    elif user_input == "scissors":
        if computer_input == "rock":
            print("your input is scissors")
            print("computer input is rock")
            print("computer win!")
            computer_points += 1
        elif computer_input == "paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you win")
            user_input += 1
        elif computer_input == "scissosr":
            print("your input is scissors")
            print("copmputer input is scissors")
            print("its a tie!")
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalif Input")