from functions import starwars,start
from rich.console import Console
from rich.padding import Padding
from rich import print
from classes import Quiz, Story
from data import question_data, quest_data
console = Console()

if __name__ == "__main__":
    # loops through game
    while True:
        starwars()
        # ask for name and checks valid input
        while True:
            player = console.input("[yellow]Hello there! what is your name?: ")
            player = player.upper()
            if player == "":
                console.print(f"[red][{player}] **NO INPUT**[/] enter you player ")
            else:
                break
        print(Padding(f"Welcome {player} Are you SITH or JEDI lets find out",
                      (2, 40), style="bold black on green", expand=True,))
        start()
       
        # empty list to store questions
        question_list = []
        # grabs the question data
        quiz = Quiz(question_data)
        # calls the functions
        quiz.run()
        
    
        # empty list to store questions
        quest_question_list = []
        # grabs the quest data
        quest = Story(quest_data)
        # calls the functions
        quest.run()
        
        # check to play agin,check valid input
        while True:
            new_game = console.input(
                "\n[yellow]Restart game?:\n\nA.[/] Yes\n[yellow]B.[/] No\n")
            new_game = new_game.upper()
            if new_game != "A" and new_game != "B":
                console.print(
                    f"[red][{new_game}] *INVALID INPUT*[/] Enter A or B ")

            else:
                break

        if new_game == "B":
            print(
                Padding(
                    f"Good bye {player} May the force be with you",
                    (2,
                     50),
                    style="bold black on blue",
                    expand=True,
                ))

            break
