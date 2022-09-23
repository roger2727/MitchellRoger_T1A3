from os import name
from typing import final
from data import quest_data, darth_data
from functions import yoda, vadar, jedi_end, jedi_quest
from functions import die, sith_quest, sith_end
from rich.console import Console
from rich import print
from rich.padding import Padding

console = Console()


class Player:

    # initialization or constructor method of
    def __init__(self):
        self.name = name

    def askName(self):

        while True:
            self.name = console.input("Hello there! what is your name? ")
            if self.name == "":
                console.print("[red]**NO INPUT**[/] enter your name ")
                return Player.askName(self)
            else:
                break

    def displayName(self):
        print(f"Welcome [yellow]{self.name}[/]\n")
        print("complete the quiz to find out if you are a jedi or sith\n")


class Question(Player):
    def __init__(self, quiz_text, quiz_answers, wrong_path):
        """
        Constructs all the necessary attributes for quiz.

        Args:
            quiz_text (str): question text
            quiz_answers (str): answer text
            wrong_path (str): wrong answer text
        """

        self.text = quiz_text
        self.answer = quiz_answers
        self.wrong = wrong_path


class Questionaire:
    def __init__(self, question_data):
        """runs a for loop over the questions,
        apends a new question in a empty list

        Args:
            question_data (str): dictionary with question
        """

        self.question_num = 0
        self.counter = 0
        self.question_list = []

        for question in question_data:

            question_text = question["question"]
            question_answer = question["correct_answer"]
            wrong_path = question["incorrect_answers"]
            new_question = Question(question_text, question_answer, wrong_path)

            self.question_list.append(new_question)
            # empty list to store questions

    def check_questions(self):
        """checks question in range

        Returns:
            str: returns if question number is less then the list of questions
        """
        self.new = len(self.question_list)
        return self.question_num < len(self.question_list)

    def next_question(self):
        """adds one to the question number,gets input.
        checks for valid input and diplays question and question number
        """

        cur_question = self.question_list[self.question_num]
        self.question_num += 1

        while True:

            console.print(
                Padding(
                    f"Q:{self.question_num}/{self.new}: {cur_question.text}",
                    (1, 1),
                    style="bold on blue",
                    expand=True,
                )
            )
            user_answer = input("\n Enter A or B: ")

            user_answer = user_answer.upper()

            if user_answer != "A" and user_answer != "B":
                console.print(f"[red]*INVALID INPUT*[/]Enter A or B:")
                continue
            else:
                break

        self.check_answer(user_answer, cur_question.answer, cur_question.wrong)

    def check_answer(self, user_answer, correct_answer, wrong_path):
        """checks user input matches with correct answer

        Args:
            user_answer (str):user input
            correct_answer (str): correct answer
            wrong_path (str): wrong answer
        """

        if user_answer == correct_answer:
            self.counter += 1

    def final(self):
        pass

    def run(self):
        """calls the functions"""
        while self.check_questions():

            self.next_question()

            self.final()


class Quiz(Questionaire):
    def final(self):
        """calculats how many questions you got right,
        user validation,promt to play again

        Returns:
            _type_: _description_
        """

        if self.question_num == 10:
            if self.counter >= 6:

                print(
                    Padding(
                        f"You have completed the quiz  you are a [i]JEDI[i]",
                        (2, 50),
                        style="bold on green",
                        expand=True,
                    )
                )
                yoda()

                while True:

                    replay_quiz = console.input(
                        "[yellow]continue or rerty[/]\nA. continue\nB. Retry "
                    )
                    replay_quiz = replay_quiz.upper()
                    if replay_quiz != "A" and replay_quiz != "B":
                        console.print("[red]*INVALID INPUT*[/]Enter A or B:")
                        continue
                    else:
                        break
                if replay_quiz == "B":
                    self.counter = 0
                    self.question_num = 0
                    return self.question_num
                else:

                    jedi_quest()
                quest = Story(quest_data)
                # calls the functions
                quest.run()

            else:
                print(
                    Padding(
                        f"***You have completed the quiz you are a SITH***",
                        (2, 30),
                        style="bold on red",
                        expand=True,
                    )
                )
                vadar()

                while True:

                    start_again = console.input(
                        "[yellow]continue or rerty[/]\nA. continue\nB.Retry\n"
                    )
                    start_again = start_again.upper()
                    if start_again != "A" and start_again != "B":
                        console.print(
                            f"[red]{start_again} INVALID INPUT[/]Enter A or B"
                        )
                        continue
                    else:
                        break
                if start_again == "B":
                    self.counter = 0
                    self.question_num = 0
                    return self.question_num
                else:
                    sith_quest()
                darth = Sith(darth_data)
                darth.run()


class Story(Questionaire):
    """Constructs all the necessary attributes for story

    Args:
        Questionaire (class): Story inherits attributes from Questionaire
    """

    def check_answer(self, user_answer, correct_answer, wrong_path):

        if user_answer == correct_answer:
            self.counter += 1

            print(Padding("correct", (1, 1), style="on green", expand=False))

        else:
            self.counter = 0
            die()
            print(
                Padding(
                    f"[black] ☠︎ ☠︎ ☠︎[/]{wrong_path}[black]☠︎ ☠︎ ☠︎[/]",
                    (2, 40),
                    style="bold black on red",
                    expand=True,
                )
            )
            self.restart()

    def restart(self):

        while True:

            self.player_dies = console.input(
                "\n[yellow]Restart Quest?:[/]\n\nA. Yes\nB. No"
            )
            self.player_dies = self.player_dies.upper()
            if self.player_dies != "A" and self.player_dies != "B":
                console.print(
                    f"[red][{self.player_dies}]*INVALID INPUT*[/]Enter A or B"
                )
                continue

            self.question_num = 0
            if self.player_dies == "A":
                return final(self)
            if self.player_dies == "B":
                self.question_num = 5
                return self.question_num

    def final(self):
        if self.counter == 5:

            jedi_end()


class Sith(Story):
    def final(self):
        if self.counter == 5:

            sith_end()
