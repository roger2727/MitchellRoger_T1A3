from quiz import Quiz, Story
from data import question_data, quest_data
question_list = []
quiz = Quiz(question_data)
quiz.run()           
print(f"Your final counter was: {quiz.counter}/{quiz.question_number}")
         

new_question_list = []
side = Story(quest_data)
side.run()
    