### Python code for the base of my game.
Here you can see how the labyrinth is created. In the future, the user and the minotaur will move.

```
lab = [[1,1,1,1,1,1,1,1,1,1],
       [1,0,0,1,0,0,0,0,0,1],
       [1,0,0,0,0,1,0,0,0,1],
       [1,0,0,0,0,1,0,0,0,1],
       [1,0,0,0,0,0,1,0,0,1],
       [1,0,1,1,0,0,0,0,0,1],
       [1,0,0,1,1,1,1,0,0,1],
       [1,0,1,0,0,0,0,0,0,1],
       [1,0,0,0,0,1,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1]]

perseo_x = 1
perseo_y = 1

for i in range(10):
  for j in range(10):
    if (i == perseo_x) and (j == perseo_y):
      print("@", sep="", end="")
    elif (lab[i][j] == 1):
      print("#", sep="", end="")
    else:
      print(".", sep="", end="")
  print()
  ```
  
  Output:
  ````
##########
#@.#.....#
#....#...#
#....#...#
#.....#..#
#.##.....#
#..####..#
#.#......#
#....#...#
##########
````
  
