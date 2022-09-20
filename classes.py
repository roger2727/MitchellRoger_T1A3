
from functions import yoda, vadar, finishdo,startquest
from rich.console import Console
from rich import print
from rich.padding import Padding


console = Console()


class Question:

    def __init__(self, quiz_text, quiz_answers, wrong_answers):
        """
        Constructs all the necessary attributes for quiz.

        Args:
            quiz_text (str): question text
            quiz_answers (str): answer text
            wrong_answers (str): wrong answer text
        """

        self.text = quiz_text
        self.answer = quiz_answers
        self.wrong = wrong_answers


class Questionaire:

    def __init__(self, question_data):
        """runs a for loop over the questions,
        apends a new question in a empty list

        Args:
            question_data (str): dictionary with question
        """

        self.question_number = 0
        self.counter = 0
        self.question_list = []

        for question in question_data:
            
            question_text = question["question"]
            question_answer = question["correct_answer"]
            wrong_answers = question["incorrect_answers"]
            new_question = Question(
                question_text, question_answer, wrong_answers)

            self.question_list.append(new_question)
            # empty list to store questions

    def check_questions(self):
        """ checks question in range

        Returns:
            str: returns if question number is less then the list of questions
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """adds one to the question number,gets input.
        checks for valid input and diplays question and question number
        """

        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
           
            user_answer = console.input(Padding(
                f"Q:{self.question_number}/10: {current_question.text}\nEnter A or B:",
                (2, 2), style="bold on blue", expand=True,))
            console.rule("")
            user_answer = user_answer.upper()

            if user_answer != "A" and user_answer != "B":
                console.print(
                    f"[red][{user_answer}]*INVALID INPUT*[/]Enter A or B:")
                continue
            else:
                break

        self.check_answer(
            user_answer,
            current_question.answer,
            current_question.wrong)

    def check_answer(self, user_answer, correct_answer, wrong_answers):
        """checks user input matches with correct answer

        Args:
            user_answer (str):user input
            correct_answer (str): correct answer
            wrong_answers (str): wrong answer
        """

        if user_answer == correct_answer:
            self.counter += 1
            print(f"{self.counter}")

    def final(self):
        pass

    def run(self):
        """calls the functions
        """
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

        if self.question_number == 10:
            if self.counter > 6:

                print(
                    Padding(
                        f"You have completed the quiz  you are a [i]JEDI[i]",
                        (2,
                         50),
                        style="bold on green",
                        expand=True,
                    ))
                yoda()

                while True:

                    replay_quiz = console.input(
                        "[yellow]continue or rerty[/]\nA. continue\nB. Retry ")
                    replay_quiz = replay_quiz.upper()
                    if replay_quiz != "A" and replay_quiz != "B":
                        console.print(
                            f"[red]*INVALID INPUT*[/] Enter A or B:[/]")
                        continue
                    else:
                        break
                if replay_quiz == "B":
                    self.counter = 0
                    self.question_number = 0
                    return self.question_number
                else:
                    startquest()

            else:
                print(
                    Padding(
                        f"***You have completed the quiz you are a SITH***",
                        (2,
                         30),
                        style="bold on red",
                        expand=True,
                    ))
                vadar()
                while True:

                    start_again = console.input(
                        "[yellow]continue or rerty[/]\nA. continue\nB.Retry\n")
                    start_again = start_again.upper()
                    if start_again != "A" and start_again != "B":
                        console.print(
                            f"[red]{start_again} INVALID INPUT[/]Enter A or B")
                        continue
                    else:
                        break
                if start_again == "B":
                    self.counter = 0
                    self.question_number = 0
                    return self.question_number
                else:
                    startquest()


class Story(Questionaire):
    """Constructs all the necessary attributes for story

    Args:
        Questionaire (class): Story inherits attributes from Questionaire
    """

    def check_answer(self, user_answer, correct_answer, wrong_answers):

        if user_answer == correct_answer:
            self.counter += 1

            print(
                Padding(
                    "correct",
                    (1,
                     1),
                    style="white on green",
                    expand=False))
        else:
            self.counter =0
            
            print(
                Padding(
                    f"[black] ☠︎ ☠︎ ☠︎[/]{wrong_answers}[black]☠︎ ☠︎ ☠︎[/]",
                    (2,
                     40),
                    style="bold black on red",
                    expand=True,
                ))

            while True:

                player_dies = console.input(
                    "\n[yellow]Restart Quest?:[/]\n\nA. Yes\nB. No")
                player_dies = player_dies.upper()
                if player_dies != "A" and player_dies != "B":
                    console.print(
                        f"[red][{player_dies}]*INVALID INPUT*[/]Enter A or B")
                    continue

                self.question_number = 0
                if player_dies == "A":
                    return self.question_number
                if player_dies == "B":
                    self.question_number = 5
                    return self.question_number

    def final(self):
        if self.counter == 5:
            return finishdo()
