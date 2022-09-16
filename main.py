
from rich.console import Console

from data import question_data,quest_data
from quiz import Player, Question,Quiz,Story,Quest
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
        
   
new_question_list = []
for question in quest_data:
                
    quest_text = question["question"]
    quest_answers = question["correct_answer"]
    wrong_answers = question["incorrect_answers"]
    quest_question = Quest(quest_text, quest_answers,wrong_answers)
    new_question_list.append(quest_question)
            
    side = Story(new_question_list)
        
    while side.check_questions():
                
            side.next_question()
            
        
    

    