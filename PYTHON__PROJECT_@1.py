

print('''

              ||QURTZ||
             ============
hello participants, welome! to the "QURTZ" platform.

[instruction: you have total 5 question. Read each statement carefuly and  place  " True " for right answer & " False " for wrong answer. Every question giveS you 1 mark .]
let's start!
''')
import random
questions = {"MS Word is a hardware": "False",
          "Octal number system contains digits from 0-7": "True",
          "Python supports for dynamic typing": "True",
          "python is case sensitive": "True",
          "Is a,b=6 statement will return an error": "True",
          "Writing comments is mandatory in python programs": "False", 
          "CPU controls only input data of computer": "False",
          "The language that the computer can understand is called Machine Language": "True",
          "Linix is a open source operating system": "False",
          "Twitter is a online social networking and blogging service.": "False"}
name = str(input("Enter your name to proceed: "))


def ask_questions():
    score = 0
    temp = 1
    while temp <=5:
        rand_q = random.choice(list(questions.keys()))

        rand_q_answer = str(questions[rand_q])
        print( "\n", rand_q)
        user_input = input("your answer: ")   

        if user_input.capitalize() == rand_q_answer:
            print ("Correct Answer!")
            score +=1
        else:
            print("Incorrect Answer!")
        temp +=1
        
    if score < 3:
        print("\nTry again! %s, your score is:" %(name), score)
    else:
        print("\nCongrats! %s, your score is:" %(name), score)
ask_questions()


    
