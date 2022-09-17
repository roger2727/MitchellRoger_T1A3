from ascii import starwars
from rich.console import Console
from rich.padding import Padding
from rich import print
from quiz import Quiz, Story
from data import question_data, quest_data
console = Console()

while True:
    starwars()     
    name= console.input("\n[i]Hello there[i]! what is your name?: ")
    print(Padding(f"Welcome {name} complete the quiz to find out if you are a SITH or JEDI", (2, 40), style="bold on green", expand=True,))    
    question_list = []
    quiz = Quiz(question_data)
    quiz.run()
                     
    new_question_list = []
    quest = Story(quest_data)
    quest.run()
    redoquest =input(" redo quest y n")
    if redoquest == "n":
        break
         
    
    
    
       