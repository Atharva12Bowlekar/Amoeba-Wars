# Amoeba-Wars

Two-Player Board Game

The game is played on a square grid. The first player is ’O’ and the other is ’X’. The game starts with an ’O’ amoeba in the bottom left corner, and an ’X’ amoeba in the top right corner (all the examples suppose a game played on an 8x8 board):
 
’O’ plays first and has one move. Then, the players take turns in making three consecutive moves. Each move can be to:
•	Create a new amoeba, by writing the player’s symbol in an accessible empty cell, or
•	Kill one of the opponent’s amoebas in an accessible cell, by shading the cell. A shaded cell is not empty and is not an amoeba.
A cell is accessible if it is next to one of the player’s live amoebas, horizontally, vertically, or diagonally.
For example, in the following opening firstly ’O’ played at B2, secondly ’X’ created three new Amoebaes (i.e., G7, F6, and E5), and finally ’O’ created two (i.e., C3 and D4) and killed one of ’X’s (i.e., E5):
 
A player must make all of their moves in a turn. The game ends when a player cannot make all the moves. The score of a player is the number of live amoebas they have when the game ends, plus the number of opponent’s amoebas killed. The player with the highest score wins.

Initially, the game asks for the size of the board. The board must be square (e.g., 6x6, 7x7, 8x8). Once the size has been entered, the initial board is drawn and the ’O’ player starts. The drawing displays the board, the column and row references (i.e., A, B, C,... and 1, 2, 3,..., respectively), and the current score on top of the board, as illustrated (supposing an 8x8 board):


O 01 - 01 X
------------------
8| | | | | | | |X|
7| | | | | | | | |
6| | | | | | | | |
5| | | | | | | | |
4| | | | | | | | |
3| | | | | | | | |
2| | | | | | | | |
1|O| | | | | | | |
------------------

|A|B|C|D|E|F|G|H|
On each turn, the program informs the current player of the moves left and provides a list of feasible moves. For example, the feasible moves for player ’O’ in the above board are: A2, B2, and B1. The players can make their moves one at the time by entering the coordinates of the chosen cell (e.g., A2). The program recognises invalid moves and informs the player in case of a mistake. After each move, the program draws the state of the board, informs the current player of the moves left, and provides a list of feasible moves. Finally, the program recognises when the game is over and a message is displayed to show the final score and congratulate the winner. After that, the program asks if the players want to play another game.

