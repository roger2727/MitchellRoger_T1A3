# T1A3 Star Wars terminal app

Github repo [_here_](https://github.com/roger2727/MitchellRoger_T1A3). \
link to video presentation [_here_](hkg).

## Table of Contents

- [General Info](#general-information)
- [Styling Convention](#styling-convention)
- [Game Features](#game-features)
- [Implementation Plan](#implementation-plan)
- [How To Install And Run](#how-to-install-and-run)
- [Screenshots](#screenshots)
- [Reference](#reference)

<br>
<br>

## **General Information**

This python terminal app is a star wars adventure game with a quiz to determine if you are a Jedi or Sith and choose your own adventure story.

<br>

## **Styling Convention**

The PEP8 style guidelines were implemented to develop this Python application.

Example of some of the guidelines (PEP 8 – Style Guide for Python Code | peps.python.org 2022)

- Use four spaces per indentation level.
- Limit all lines to a maximum of 79 characters.
- Surround top-level function and class definitions with two blank lines.
- Imports should usually be on separate lines.
  <br>
  <br>

## **Game Features**

<br>
<br>

## **Feature 1: The quiz works out if you are a sith or Jedi from the answers you give**

- The quiz uses a counter to count how many correct questions the user gets. Then I used an if statement to check if the user guessed correct more than half of the questions. If so, It will print out that you are a Jedi and display ASCII art.
  <br>
  <br>

## **Feature 2: different story quests**

- Depending on what your result is after completing the quiz, you will be directed to the corresponding story quest.

<br>
<br>

## **Feature 3: choose your path in a StarWars story quest**

- The story quest will ask you to choose a path a or b that uses an if statement to check that the user's answer matches the correct answer. If correct, the next quest is printed out. If incorrect, it will print you are incorrect and ask you if you want to play again. If you say yes, the question count is reset, and you start the quest again
  <br>
  <br>

## **Feature 4: Restart options**

- The game has a restart feature at the end of both the quiz and quests, so the player does not have to go through the whole game to do the quiz again, and vice versa for the story quest. I accomplished this by using the input and putting it in an if statement to catch what the user picks.

<br>
<br>

## **Implementation plan**

link to Trello Implementation plan [_here_](https://trello.com/b/p572wN56/star-wars-terminal-app).

![Example screenshot](/docs/trelloboard.png)

<br>
<br>

## **How To Install and run**

1. Install Python3

   - check if Python3 is installed, type in the terminal `python3 --version`' into the terminal

   - Installation instructions: https://realpython.com/installing-python/

2. Create a Virtual Environment

   - type in the terminal `python3 -m venv venv`
   - type in the terminal `. venv/bin/activate`
   - Installation instructions: https://docs.python.org/3/library/venv.html

3. Install pip (To check if pip is installed, type `pip --version` into the terminal

   - if pip is not installed type `python3 -m ensurepip --upgrade`
   - Installation instructions: https://pip.pypa.io/en/stable/installation/

4. Install the rich module package

   - type `python3 -m pip install` rich into the terminal
   - Installation instructions: https://pypi.org/project/rich/

5. run the app

   - type in the terminal `python3 main.py`

## Execute Program

1. Create a Virtual Environment
   - type in the terminal `python3 -m venv venv`
   - type in the terminal `. venv/bin/activate`
   - Installation instructions: https://docs.python.org/3/library/venv.html
2. In your terminal, go to the directory containing the application
3. To execute run.sh file by entering: `./run.sh`

<br>
<br>

## **Screenshots**

![Example screenshot](/docs/Screen%20Shots.png)

<br>
<br>

## **Reference**

Refrence for PEP8 style guidelines

PEP 8 – Style Guide for Python Code | peps.python.org 2022. viewed 21 September 2022, [_https://peps.python.org/pep-0008/_].
