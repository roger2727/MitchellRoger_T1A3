
from ascii import yoda, vadar
from rich.console import Console
from rich import print
from rich.padding import Padding
console =Console()

class Question:

    def __init__(self, quiz_text, quiz_answers, wrong_answers):
          
        self.text = quiz_text
        self.answer = quiz_answers
        self.wrong = wrong_answers  
     

class Questionaire:
     
    
    
    def __init__(self, question_data):
           
        
        
      
        self.question_number = 0
        self.counter = 0
        self.question_list = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            wrong_answers = question["incorrect_answers"]    
            new_question = Question(question_text, question_answer, wrong_answers)
        
            self.question_list.append(new_question)
        
    
    def check_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        
        while True:
            user_answer = console.input(f"\n[blue]Q:{self.question_number}/10[/]\n{current_question.text}   \n[blue]Enter [[/]A[blue]] or [[/]B[blue]][/]:\n")
            console.rule("")
            user_answer =user_answer.upper()
            if user_answer != "A" and user_answer != "B":
                    console.print(f"[red][{user_answer}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
                    continue
            else:
                break
                       
        self.check_answer(user_answer, current_question.answer, current_question.wrong)
        
    def check_answer(self, user_answer, correct_answer, wrong_answers):
        
        pass
            
   
    def final(self):
        
        print(f"not implemented")
        
    def run(self):
       while self.check_questions():
                     
        self.next_question()
        
        self.final()
        
class Quiz(Questionaire):     
        

    def check_answer(self, user_answer, correct_answer,wrong_answers):
        
        
        if user_answer == correct_answer:
            self.counter += 1
        #     print(f"{self.counter}")
            
   
    def final(self):
        
        
        if self.question_number == 10:
            if self.counter>6:
                
                print(Padding(f"***You have completed the quiz  you are a [i]JEDI[i]***", (2, 50), style="bold on green", expand=True,))
                yoda()
                
                while True:
                    
                    replay_quiz =console.input("[yellow]Do you want to continue or rerty the quiz \nA.[/] continue\n[yellow]B.[/] Retry\n")
                    replay_quiz =replay_quiz.upper()
                    if replay_quiz != "A" and replay_quiz != "B":
                        console.print(f"[red][{replay_quiz}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
                        continue
                    else:
                      break
                if replay_quiz == "a":
                    self.counter = 0
                    self.question_number = 0
                    return self.question_number
                    
                
            else:
                print(Padding(f"***You have completed the quiz  The darks side it strong with you, you are a SITH***", (2, 30), style="bold on red", expand=True,))
                vadar()
                while True:
                    
                    start_again =console.input("[yellow]Do you want to continue or rerty the quiz \nA.[/] continue\n[yellow]B.[/] Retry\n")
                    start_again =start_again.upper()
                    if start_again != "A" and start_again != "B":
                        console.print(f"[red][{start_again}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
                        continue
                    else:
                      break
                if start_again == "B":
                 self.counter = 0
                 self.question_number = 0
                 return self.question_number
                    
            
                
class Story(Questionaire):
      
    def check_answer(self, user_answer, correct_answer, wrong_answers):
        
            if user_answer == correct_answer:
                
                print(Padding("correct", (1,1), style="white on green", expand=False))
            else:
                print(Padding(f"[black]☠︎ ☠︎ ☠︎ ☠︎[/]{wrong_answers}[black]☠︎ ☠︎ ☠︎ ☠︎[/]", (2, 40), style="bold black on red", expand=True,))    
               
                
                while True:
                    
                    player_dies =input("\n[yellow]Start Quest again?:[/]\n\nA. Yes\nB. No i quit")
                    player_dies =player_dies.upper()
                    if player_dies != "A" and player_dies != "B":
                        console.print(f"[red][{player_dies}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
                        continue
                     
                    self.question_number =0
                    if player_dies=="A":
                        return self.question_number
                    if player_dies=="B":
                        self.question_number =5
                        return self.question_number

                        
            
            
            
                 
                
              
                
                    
                 
                      
                
    def final(self):
        
       pass
            
            
        
      
                  
                
         
                


            
