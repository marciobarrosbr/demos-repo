quiz = {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
    "question": "What is the capital of Germany",
    "answer": "Berlin"
    },
}
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")
    
    if answer.lower() == value[ 'answer'] .lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print('The answer is :' + value[ 'answer'])
        print("Your score is: "+ str(score))
        print("")

print("You got " + str(score) + "out of 2 question correctly")

print("Your percentage is " + str(int(score/7 * 100)) +"%")

# teste no novo branch feature_27-01
