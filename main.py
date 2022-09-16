from typing import Final
from ascii import starwars
from data import question_data
from quiz import Question,Quiz,Player


starwars()
new = Player()
question_list = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
        
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz = Quiz(question_list)

while quiz.check_questions():
        quiz.next_question()
        end =quiz.final()       
print("You've completed the quiz")
print(f"Your final counter was: {quiz.counter}/{quiz.question_number}")
        


    