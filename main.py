from ascii import  starwars
from quiz import Question, Quiz, Story
from data import question_data, quest_data

while True:
   
   
    
    
      
    question_list = []
    quiz = Quiz(question_data)
    quiz.run()           
    print(f"Your final counter was: {quiz.counter}/{quiz.question_number}")
            
    
    new_question_list = []
    quest = Story(quest_data)
    quest.run()
    playagain=input("play again y n")
    if playagain == "n":
        break
       