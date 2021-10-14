# Unit 1: A classic game 
![](game.gif)

# Criteria A: Planning

## Problem definition

The owner of the local game shop is an enthusiast of classic computer games. He has been looking for a talented programmer that can help him revive his passion for text-based games. He has few requirements for this task:

1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.

Apart for this requirements, the owner is open to any type of game, topic or genre.

## Proposed Solution

Design statement:
I will design and make a classical text-based game for a client who is the owner of the local game shop. The text-based game will be about the Minotaur's labyrinth and is constructed using the software Python. It will take 3 weeks to make and will be evaluated according to the criteria that is below.

Justify the tools/structure of your solution:
Python is one of the most accessible programming languages because it is not complicatedit and has simplified syntax very similar to the English language, which is perfect for beginners. Also, its codes can be easily written and executed much faster than other programming languages. Python is an open source and has a lot of libraries to complement the code.

## Success Criteria
1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.
4. The game has to be played in less than 20 minutes each time.
5. The user will only need its computer, a pen and a sheet of paper to play.
6. The game must show the best scores stored in the local database.

# Criteria B: Design

## System Diagram
![](IMG_0153.jpg)

**Figure 1.** System diagram for the proposed solution

As shown in **Fig. 1**, the proposed solution runs on Python and it is developed using Pycharm (v. 2021). The proposed game...

## Flow Diagrams

### Caesar Cypher

The database in the game has to be protected so that personal data is not exposed. To solve this requirement I am using the Caesar cypher. **Fig. 2**
shows the flow diagram for this function.


## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 10min         | Sep 24                 | B         |
| 2       | Create a encryption function for the user data                | A function tested that uses the caesar cypher                                                                   | 20 min        | Oct 6                  | C         |
| 3       | Integrate the encryption with the database save/load function | The database is encrypted and can be read/write                                                                 |               |                        | C         |
| 4       | Create a function for encoding the database                   | a function tested that encodes the database                                                                     | 40min         | Oct 7                  | C         |
| 5       | Unit Test: function for encoding with the Caesar cypher       | To check that the function works as expected. Test with input "hello" and key =1. The outcome should be "ifmmp" | 5 min         | Oct 7                  | E         |
