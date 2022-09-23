from functions import starwars, start
from rich.console import Console
from rich.padding import Padding
from rich import print
from classes import Player, Quiz, Player
from data import question_data

console = Console()

if __name__ == "__main__":
    # loops through game
    while True:
        starwars()
        player = Player()
        player.askName()

        start()
        player.displayName()
        quiz = Quiz(question_data)
        quiz.run()

        while True:
            new_game = console.input(
                "\n[yellow]Restart game?:\n\nA.[/] Yes\n[yellow]B.[/] No\n"
            )
            new_game = new_game.upper()
            if new_game != "A" and new_game != "B":
                console.print(f"[red][{new_game}] *INVALID INPUT*[/] Enter A or B ")

            else:
                break

        if new_game == "B":
            print(
                Padding(
                    f"Good bye May the force be with you",
                    (2, 50),
                    style="bold black on blue",
                    expand=True,
                )
            )

            break
