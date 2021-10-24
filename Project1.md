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

### Design statement:
I will design and make a classical text-based game for a client who is the owner of the local game shop. The text-based game will be about how Theseus finds the exit to the Minotaur's labyrinth without getting eaten by the Minotaur or dying because of starvation and it is constructed using the software Python. It will take 3 weeks to make and will be evaluated according to the criteria that is below.

### Justify the software selected:
Python is one of the most accessible programming languages because it is not complicated and has simplified syntax very similar to the English language, which is perfect for beginners. According to many sources, 30% of programmers use Python as their main programming language, so there is a big Internet community for asking for help. 
Also, its codes can be easily written and executed much faster than other programming languages. 
Python is an open source and has a lot of libraries to complement the code, so you can do practically anything with your code.

### Justify the structure of the proposed solution:
My program has the typical game type and it is easy to understand. There are comments on each step, so someone that reads the code can understand what is happening easily. Also, there are functions that make the code simple and variables with names that are understandable.

## Success Criteria
1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.
4. The game has to be played in less than 20 minutes each time.
5. The user will only need its computer, a pen and a sheet of paper to play.
6. The game must show the best scores stored in the local database.
7. The game should have 3 difficulty levels with night and day modes.

# Criteria B: Design

## System Diagram
![image](https://user-images.githubusercontent.com/89135778/137406212-d287995b-8009-4980-9966-ec4a63d0bb57.png)

This is the System Diagram. You can see how the game is operated in a computer HP with its especifications, with the operative system of WIndows 10. The programme used to tun this game is PyCharm Edu and the archive's name is game.py. There is also a local database where the name, time and score is stored.


## Flow Diagrams
![Project1diagram](https://user-images.githubusercontent.com/89135778/137440549-eeb239c1-e9a9-4c56-b958-2c099a1fa3ab.png)

This diagram is the most basic base of my game. You can see that there is the basic information like the user name and the timer. Also, here is first made the labyrinth, with a 2-dimensinal list where "#" is a wall and "." the floor. The user needs to reach "E", the exit. The user will start in position x=1 y=1 and the minotaur in position x=9 y=9. 
After this basic introducitons I am going to explain a bit more the algorithm. The user will input in the keyboard and will receive output in the monitor screen.

```
#Example of how the labyrinth would look like.

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
![image](https://user-images.githubusercontent.com/89135778/137441033-ddae5c4e-5389-46a2-8061-0fc05aa3ab40.png)

In this loop the user, Theseus, moves. He can go North (N), South (S), West (W)  or East (E) with the keyboard. If Theseus arrives to a "#" in the labyrinth, he would have hit a wall, so he would have lost and has to start over. By doing this, the user must remember where are the walls, maybe drawing their own labyrinth by hand in a paper.

![image](https://user-images.githubusercontent.com/89135778/137404105-cf5e4745-103d-4cfc-8c7e-7e59c2812fbf.png)

In this loop the Minotaur moves. This is done automatically every time the user moves. 

![image](https://user-images.githubusercontent.com/89135778/137441090-ccd2e234-eafd-41fc-a55a-2e921721486b.png)

To finish the game, the user needs to reach "E", the exit. If not, the time can be over or the user may be next to the Minotaur, so it would eat him.



### Caesar Cypher
![Caesar](https://user-images.githubusercontent.com/89135778/137412426-fb1e8e2d-5f45-41f4-9d25-922c4bfecd90.png)

The database in the game has to be protected so that personal data is not exposed. To solve this requirement I am using the Caesar cypher. **Fig. 2**
shows the flow diagram for this function.

## User Interface Sketch
![userinterface](https://user-images.githubusercontent.com/89135778/138592407-778181c6-93e3-4379-aab8-a2acc6b80728.jpg)

## What is the personal relevance of the game? Why did you pick the theme?
I love Greek and Roman myths and gods. They have relevance in our daily lifes. For example, they have had influence on art, sculptures, Percy Jackson books, The Maze Runner series and many more. I think everyone should hear these stories because you can learn a lot of things about them. The idea of creating a game about a labyrinth first came and I wasn't even sure if it was possible to create it, but after some research I found how to do it. After that, I was thinking of the thematic and I thought that doing it about the Minotaur's myth could be very interesting. 

## Future improvements ideas:
- Random initial positions for Theseus and Minotaur
- The game could tell the user if the Minotaur is close
- New labyrinths with different difficulty levels
- Available in other languages: Spanish


## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 10min         | Sep 30                 |           |
| 2       | Create flow diagrams for the project                           | To have clear ideas on how to code and how the programme would work                                                                   | 20 min        | Sep 30                  |           |
| 3       | Code the base of my game                                      | The game has a base, which is the labyrinth                                                                 |40min               |  Oct 7                     |           |
| 4       | Caesar cypher       | To check that there is security | 5 min         | Oct 14                  |           |
