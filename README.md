# Coding Assignment Tic Tac Toe Challenge


## Functional Specification

### Overview
* Two players take turns placing X’s and O’s on a 3x3 grid.
* The win condition is the first player to get three across a column, down a row, or on either diagonal.

## Helpful links
* [Download Python (Windows, macOS, and Linux) – python.org](https://www.python.org/downloads/)

* [Create a Python console application using Visual Studio Code – VS Code Docs](https://code.visualstudio.com/docs/python/python-tutorial)

* [A Tour of Python – Python Tutorial (official docs)](https://docs.python.org/3/tutorial/)

## User Stories
- ** As a user**, I want see a welcome message
- ** As a user**, I want to be offered a chance to learn how to play
- ** As a user**, I want to input my X/O choices based off of number placement
- ** As a user**, I want to know when I win.

### Functional Requirements:
Feature 1:  User input prompts
- description:  Game asks user if they would like instructions?
 If user (yes) => View Instructions on Wiki page and Start game
 If user (no) =>  Start game

Feature 2:  Game board display 
- description Create a 3x3 game grid with comma-separated numbers.

Feature 3:  Get Current player move (User input)
- description, Game auto starts with player X.  User input a number between 1-9.

Feature 4:  Update board with moves
- description, board updates with user inputs

Feature 5:  Check for winner
- description, checks for winner: across/diagonal/down

Feature 6: Stop game
- description, user can quit at any time during gameplay by typing 'quit'



## TO DO Features :
Check for tie game
Format player inputs, add colors, Red = X Blue = O
Interactive:  Players can pay against one another online
Validate Input so cannot make illegal moves
When player wins, provide a gif
Play again
Render to production

Run this command in the terminal:

```bash
python3 applications.py
```