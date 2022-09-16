
from rich.console import Console

from data import question_data
from quiz import Player, Question,Quiz
console =Console()


Player()
question_list = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
        
    new_question = Question(question_text, question_answer)
    
    question_list.append(new_question)
  

quiz = Quiz(question_list)

while quiz.check_questions():
        console.rule("")  
        quiz.next_question()
        quiz.final()
        
             

print(f"Your final counter was: {quiz.counter}/{quiz.question_number}")
        


    