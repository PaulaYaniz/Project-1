# Unit 1: A classic game 
![image](https://user-images.githubusercontent.com/89135778/137404871-b4304425-ce71-41c6-aaae-f430bbe45b56.png)


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

## Flow Diagrams
![Project1diagram](https://user-images.githubusercontent.com/89135778/137405018-157665e4-5b8c-4a9a-a860-b53a6ac69ce2.png)

This diagram is the most basic base of my game. You can see that there is the basic information like the user name and the timer. Also, here is first made the labyrinth, with a 2-dimensinal list where "#" is a wall and "." the floor. The user needs to reach "E", the exit. The user will start in position x=1 y=1 and the minotaur in position x=9 y=9. 
After this basic introducitons I am going to explain a bit more the algorithm.

```
#Example of how the labyrinth could look like. The user cannot see this.

  0123456789
0 ##########
1 #@......##
2 #.##.....#
3 #..#.....#
4 #....##..#
5 #...#....E
6 #........#
7 #..#...###
8 #.......M#
9 ##########
```
![image](https://user-images.githubusercontent.com/89135778/137404081-61a7ce18-4586-4c1b-9491-c91ee54ffdb2.png)

In this loop the user, Perseo, moves. He can go North (N), South (S), West (W)  or East (E) with the keyboard. If Perseo arrives to a "#" in the labyrinth, he would have hit a wall, so he would have lost and has to start over. By doing this, the user must remember where are the walls, maybe drawing their own labyrinth by hand in a paper.

![image](https://user-images.githubusercontent.com/89135778/137404105-cf5e4745-103d-4cfc-8c7e-7e59c2812fbf.png)

In this loop the Minotaur moves. This is done automatically every time the user moves. 

![image](https://user-images.githubusercontent.com/89135778/137404125-8786aeb1-11c3-4d2a-9242-7afb309d7246.png)

To finish the game, the user needs to reach "E", the exit. If not, the time can be over or the user may be next to the Minotaur, so it would eat him.



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
