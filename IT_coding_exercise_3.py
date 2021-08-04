#Author: Izabela
#Quiz name: BestQuiz 
#Version: 3.7.9
#© 2021 Izabela. All rights reserved.

#This is a program for the demo of a multiple-choice Quiz,
#which will be presented at an event. The aim is
#to make it interactive and user-friendly.

import sys
print(sys.version)



name = input("Please enter your name; ")
print( "Welcome to the world of BestQuiz",name)

print(name, "Im here to tell you the ruls of the game: ")



user = input("Type yes to see the rules: ")
 

     
       
print("""BestQuiz is a multiple-choice quiz that is fully interactive.
To complete  the game, you'll have to answer a series of questions correctly.
So your aim should be to score as many points as possible.
There's no timer during the quiz.
The rules of BestQuiz:
Once a question is posed, you'll be given three options: a, b and c.
You have to select the correct answer. You can only choose a, b or c.
When entering your answer, ensure that you use a lowercase letter.""")

# the user inputs that they don't want to continue this game this
#code will exit it in an if statement inside a while loop.

while True:
   answer = input('Do you want to continue?:')
   if answer.lower().startswith("yes"):
      print("ok, carry on then")
      break
   elif answer.lower().startswith("no"):
      print("Sad to see you go, We hope to see you next time !" )
      exit()

# import question class
from question import question

#array call questions contain questions objects
questions = [
            "Q1. What is the capital city of Italy?",
            "Q2. What is the capital city of Poland?",
            "Q3. What is the capital city of Spain? ",
            "Q4   What is the capital city of Germany?",
            "Q5 What is the capital city of Switzerland?"
            
            ];

#array call choices contain choices objects 
choices  = [
            "\na. Bulgaria \nb. Rome \nc. Madrid",
            "\na. Athens \nb. Berlin \nc. Warsaw",
            "\na. Madrid \nb. Paris \nc. Budapest",
            "\na. Berlin \nb. Bratislava \nc. Vienna",
            "\na. Lisbon \nb. Bern \nc. London"
            ];

#array call prompt_questions contain choices + questions objects 
prompt_questions = [
                    questions[0] + choices[0],
                    questions[1] + choices[1],
                    questions[2] + choices[2],
                    questions[3] + choices[3],
                    questions[4] + choices[4]
                    ];

#array call Ques_Ans  contain import class question pass+ questions objects  
Ques_Ans = [
                  question(prompt_questions[0], "b"),
                  question(prompt_questions[1], "c"),
                  question(prompt_questions[2], "a"),
                  question(prompt_questions[3], "a"),
                  question(prompt_questions[4], "b")
                  ];

# loop fanction call launch_quiz with one parameter Ques_Ans. The loop go throuth all the question counting correct answer.
def launch_quiz(Ques_Ans):
     score = 0
     for q in Ques_Ans:
          user_in = input(q.q_prompt + "\n\nEnter your answer: ")
          print()
          if user_in == q.q_answer:
               score += 10
     print("\nYou got " + str(score) + "/" + str(len(Ques_Ans)) + " questions correct.")

launch_quiz(Ques_Ans)


#questions class will be able to store the qestion and also be able to store the question answer
class question:
     def __init__(self, q_prompt, q_answer):
          self.q_prompt = q_prompt;
          self.q_answer= q_answer;

