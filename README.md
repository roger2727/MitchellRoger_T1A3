# T1A3 Star Wars terminal app

Github repo [_here_](https://github.com/roger2727/MitchellRoger_T1A2). \
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

this terminal app is a star wars adventure game with a quiz to determain if you are a jedi or sith and a choose your own adventure story.
<br>
<br>

## **Styling Convention**

The PEP8 style guidelines were implemented to develop this Python application.

Example of some of the guidlines (PEP 8 – Style Guide for Python Code | peps.python.org 2022)

<br>

- Use 4 spaces per indentation level.
- Limit all lines to a maximum of 79 characters.
- Surround top-level function and class definitions with two blank lines.
- Imports should usually be on separate lines

<br>
<br>

## **Game Features**

<br>
<br>

### **Feature 1: The quiz works out if you are a sith or jedi from the answers you give**

The quiz uses a counter to count how many correct questions the user gets, then i used an if statment to check if the user guesses correct more than half of the questions. If so It will print out that you are a Jedi and display ascci art.

<br>
<br>

### **Feature 2: choose your path in a starwars story quest**

The story quest will ask you to choose a path a or b than uses an if statement to check that the user's answer matches the correct answer. If correct, the next quest is printed out. If incorect, it will print you are incorect, and it will ask you if you want to play again. If you say yes, the question count is reset, and you start the quest again

<br>
<br>

### **Feature 3: Restart options**

The game has a restart feature at the end of both the quiz and quests, so the player does not have to go through the whole game to do the quiz again, and vice versa for the story quest. I accomplished this by using the input and putting it in an if statement to catch what the user picks

<br>
<br>

## **Implementation plan**

link to Trello Implementation plan [_here_](https://trello.com/b/p572wN56/star-wars-terminal-app).

![Example screenshot](/docs/trelloboard.png)

<br>
<br>

## **How To Install and run**

1. Install Python3

   - check if Python3 is installed, type in the terminal python3 --version' into terminal

   - Installation instructions: https://realpython.com/installing-python/

2. Create a Virtual Environment

   - type in the terminal python3 -m venv venv
   - type in the terminal . venv/bin/activate
   - Installation instructions: https://docs.python.org/3/library/venv.html

3. Install pip (To check if pip is installed, type 'pip --version' into terminal

   - if pip not intalled type python -m ensurepip --upgrade
   - Installation instructions: https://pip.pypa.io/en/stable/installation/

4. Install rich module pakage

   - type python -m pip install rich into the terminal
   - Installation instructions: https://pypi.org/project/rich/

5. run app

   - type in the terminal python3 main.py

<br>
<br>

## **Screenshots**

![Example screenshot](/docs/Screen%20Shots.png)

<br>
<br>

## **Reference**

Refrence for PEP8 style guidelines

PEP 8 – Style Guide for Python Code | peps.python.org 2022. viewed 21 September 2022, [_https://peps.python.org/pep-0008/_].
