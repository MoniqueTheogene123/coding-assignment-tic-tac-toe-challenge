{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "d5eb54ff-99ad-41df-a3fc-3e967bb649da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# interactive tic tac toe game.\n",
    "\n",
    "import pandas as pd\n",
    "import os\n",
    "import random\n",
    "import numpy as np\n",
    "from matplotlib.patches import Circle\n",
    "\n",
    "import time\n",
    "time.sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "285637b3-ebf7-403e-bc92-c8e638725178",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Tic Tac Toe!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Would you like instructions on how to play the game? (yes/no) :  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Visit this page to learn: https://en.wikipedia.org/wiki/Tic-tac-toe.\n",
      "\n",
      "Starting the game now...\n",
      "\n",
      " 1 | 2 | 3 \n",
      "-----------\n",
      " 4 | 5 | 6 \n",
      "-----------\n",
      " 7 | 8 | 9 \n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Player X, Enter a number between 1-9:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " 1 | X | 3 \n",
      "-----------\n",
      " 4 | 5 | 6 \n",
      "-----------\n",
      " 7 | 8 | 9 \n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Player O, Enter a number between 1-9:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " O | X | 3 \n",
      "-----------\n",
      " 4 | 5 | 6 \n",
      "-----------\n",
      " 7 | 8 | 9 \n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Player X, Enter a number between 1-9:  quit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Quitting Game\n"
     ]
    }
   ],
   "source": [
    "def instructions_input():\n",
    "    \"\"\"Ask user if they want instructions and handle input validation\"\"\"\n",
    "    while True:\n",
    "        instructions = input(\"Would you like instructions on how to play the game? (yes/no) : \").lower()\n",
    "        \n",
    "        if instructions in ['yes', 'y']:\n",
    "            print(\"Visit this page to learn: https://en.wikipedia.org/wiki/Tic-tac-toe.\")\n",
    "            return True\n",
    "        elif instructions in ['no', 'n']:\n",
    "            print(\"No instructions, OK! Let's go\")\n",
    "            return False\n",
    "        else:\n",
    "            print(\"Invalid input. Please enter 'yes' or 'no'\")\n",
    "\n",
    "def display_board(board):\n",
    "    \"\"\"Display the current game board\"\"\"\n",
    "    print(f\"\\n {board[0][0]} | {board[0][1]} | {board[0][2]} \")\n",
    "    print(\"-----------\")\n",
    "    print(f\" {board[1][0]} | {board[1][1]} | {board[1][2]} \")\n",
    "    print(\"-----------\")\n",
    "    print(f\" {board[2][0]} | {board[2][1]} | {board[2][2]} \")\n",
    "\n",
    "def main():\n",
    "    print(\"Welcome to Tic Tac Toe!\")\n",
    "    \n",
    "    # Initialize empty board\n",
    "    board = [['1','2','3'], \n",
    "             ['4','5','6'], \n",
    "             ['7','8','9']]\n",
    "    \n",
    "    # Call the function - it will handle the loop and validation\n",
    "    instructions_input()\n",
    "    \n",
    "    # Game continues here regardless of choice\n",
    "    print(\"\\nStarting the game now...\")\n",
    "    \n",
    "    current_player = 'X'\n",
    "    game_over = False\n",
    "    \n",
    "    while not game_over:\n",
    "        display_board(board)\n",
    "        print(\"\\n\")\n",
    "        user_input = input(f\"Player {current_player}, Enter a number between 1-9: \")\n",
    "        \n",
    "        # TO DO:  Validate input\n",
    "        \n",
    "        # If user wants to quit, let them at any time\n",
    "        if user_input.lower()== 'quit':\n",
    "            print(\"\\n Quitting Game\")\n",
    "            return\n",
    "\n",
    "        # Update board\n",
    "        valid_move = False\n",
    "        for row in range(3):\n",
    "            for col in range(3):\n",
    "                if board[row][col] == user_input:\n",
    "                    board[row][col] = current_player\n",
    "                    valid_move = True\n",
    "                    break\n",
    "            if valid_move:\n",
    "                break\n",
    "        \n",
    "        if not valid_move:\n",
    "            print(\"Invalid move! Please try again.\")\n",
    "            continue\n",
    "\n",
    "        \n",
    "        # Check for win across diagnal row\n",
    "        if check_winner(board, current_player):\n",
    "            display_board(board)\n",
    "            print(f\"\\nPlayer {current_player} wins!\")\n",
    "            game_over = True\n",
    "            \n",
    "            \n",
    "        # Switch player\n",
    "        current_player = 'O' if current_player == 'X' else 'X'\n",
    "\n",
    "# Run the game\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "417ad26e-5e06-41d8-a3b8-e5164f6191af",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
