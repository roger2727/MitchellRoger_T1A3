from ascii import yoda, vadar, starwars
starwars()
player=input("\nHello there! please enter you name: ")
class Question:
    
    def __init__(self, quiz_text, quiz_answers):
        self.text = quiz_text
        self.answer = quiz_answers

class Player():
    def __init__(self):
       
        self.name = player
        print(f"\nwelcome {player} complete this quiz to find out if you are a jedi or sith")
       
class Quiz:  
        
    def __init__(self, question_list):
        self.question_number = 0
        self.counter = 0
        self.question_list = question_list
    
    def check_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        
        while True:
            user_answer = input(f"\nQ.{self.question_number}/10: {current_question.text}   \nEnter A or B: ")
            user_answer =user_answer.upper()
            if user_answer != "A" and user_answer != "B":
                    print("you on drugs")
                    continue
            else:
                break
                       
        self.check_answer(user_answer, current_question.answer)
        
        

    def check_answer(self, user_answer, correct_answer,):
        
        if user_answer == correct_answer:
            self.counter += 1
            print(f"{self.counter}")
            
   
    def final(self):
        
        if self.question_number == 10:
            if self.counter>6:
                print("\nYou've completed the quiz")
                print(f"\n Goodness i sense in you {player}, Jedi story you begin")
                yoda()
            else:
                print("\nYou've completed the quiz")
                print(f"\nThe darks side it strong with you {player}, you are a sith  ")
                vadar()
            
            
                    