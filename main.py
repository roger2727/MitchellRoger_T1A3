from ascii import finishdo, starwars
from rich.console import Console
from rich.padding import Padding
from rich import print
from quiz import Quiz, Story
from data import question_data, quest_data

console = Console()

while True:
    starwars()
    while True:
        player_name= console.input("[yellow][i]Hello there[i]! what is your name?: ")
        player_name = player_name.upper()
        if player_name == "": 
            console.print(f"[red][{player_name}] ****NO INPUT****[/] I sense a great deal of confusion in you, enter you name ")
            continue
        else:
            break     
   
    print(Padding(f"Welcome {player_name} complete the quiz to find out if you are a SITH or JEDI", (2, 40), style="bold black on green", expand=True,))    
    question_list = []
    quiz = Quiz(question_data)
    quiz.run()
      
    print(Padding(f"complete your quest {player_name} and become a jedi master", (2, 50), style="bold black on green", expand=True,))                  
    new_question_list = []
    quest = Story(quest_data)
    quest.run()
    finishdo()
    while True:
        new_game =console.input("\n[yellow]Do you want to play again:\n\nA.[/] Yes\n[yellow]B.[/] No\n")
        new_game = new_game.upper()
        if new_game != "A" and new_game != "B":
            console.print(f"[red][{new_game}] ****INVALID INPUT****[/] [blue]Enter [[/]A[blue]] or [[/]B[blue]][/]")
            continue
        else:
            break
                
    if new_game == "B":
        print(Padding(f"Good bye {player_name} May the force be with you", (2, 50), style="bold black on blue", expand=True,))
        
        break
         
    
    
    
       