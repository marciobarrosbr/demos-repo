import random

exit = False
user_input = 0
computer_input = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choise rock, paper, scissors or exit: ")
    computer_input = random.choise(option)

    if user_inout == "exit":
        print("gamer ended")
        print("you won a total score of " +str(user_points)+" and the computer total score is " +str(computer_points))
        exit = True

        if user_input == "rock":
            if computer_input == "rock":
                print("your input is rock")
                print("computer input is rock")
                print("it is a tie!")
            elif computer_input == "paper":
                print("your input ios rock")
                print("computer input is paper")
                print ("computer win")
                computer_points += 1
            elif computer_input == 'scissors':
                print("your input is rock")
                print("computer input is scissors")
                print("you win")
                user_input += 1

            elif user_input == "paper":
                if computer_input == "rock":
                    print("ypur input id paper")
                    print("computer input is rock")
                    print("you win!")
                    user_input  +=1
                elif computer_input == "paper":
                    print("your input is paper")
                    print("computer input is paper")
                    print("it is a tie!")
                elif computer_input  == "scissors":
                    print("your input is paper")
                    print("computer input is scissors")
                    print("computer win")
                    computer_input += 1

            elif user_input == "scissors":
                if computer_input == "rock":
                    print("your input is scissors")
                    print("computer input is paper")
                    print("computer win")
                    computer_input += 1
                elif computer_input == "paper":
                    print("ypur input is scissors")
                    print("computer in scissors")
                    print("you win!")
                    user_input += 1
                elif computer_input == "scissors":
                    print("your input scissors")
                    print("computer input is scissors")
                    print("its is a tie!")
                elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
                    print("invalid Input")