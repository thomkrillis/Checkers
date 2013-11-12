Checkers
========
First project for Artificial Intelligence course: make a checkers AI

NOTE: this code is far from elegant and could be heavily refactored.

AI performs alpha-beta prunning with iterative deepening.

The board information is stored as a bitboard, a list of three unsigned binary integers corresponding to the piece
  positions of first player, second player, and kings.

Includes p vs. p, p vs. c, and c vs. c where computers could both make random moves, both run AI, or play random vs. AI.
User can also set which player goes first, how long the AI can search, and how long the output display pauses during 
  random decision-making, and the user can load an initial board state.
  
Tested in python shell (no colours) and command prompt (short game history).
