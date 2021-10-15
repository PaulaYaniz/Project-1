### Python code for the base of my game.
Here you can see how the labyrinth is created. In the future, the user and the minotaur will move.

```
print("Welcome to the Minotaur's labyrinth game!")
print("  (Press enter in the keyboard to continue)")
input()
print("The Minotaur was the son of the Cretan Bull and Pasiphae, a human girl. King Minos asked Dedalos, the builder, to make a labyrinth to enclose the minotaur so that he would not kill the people of the city.")
print("However, the Minotaur had to be fed so every so often 7 girls and 7 boys were given to him to eat.")
print("Theseus was one of the boys who had to be sacrificed but he fell in love with Ariadna, the king's daughter. Ariadna was very clever so she gave Theseus a sewing thread to mark the path through the labyrinth.")
print("Finally, Theseus managed to kill the Minotaur and return without getting lost to his house.")
print("  (Press enter in the keyboard to continue)")
input()
print("Now, you can see an example on how the labyrinth would look like. You are @ and the Minotaur is M. Exit is E")
print("The walls are # and the floor are .")
print()
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

minot_x = 8
minot_y = 8

theseus_x = 2
theseus_y = 2

exit_x = 9
exit_y = 6

for i in range(10):
  for j in range(10):
    if (i == theseus_x) and (j == theseus_y):
      print("@", sep="", end="")
    if (i == minot_x) and (j == minot_y):
      print("M", sep="", end="")
    if (i == exit_x) and (j == exit_y):
      print("E", sep="", end="")
    elif lab[i][j] == 1:
      print("#", sep="", end="")
    else:
      print(".", sep="", end="")
  print()

print("  (Press enter in the keyboard to continue)")
input()
print("Now, you are Theseus and you need to move in the labyrinth. Use your keyboard to move.")
dir = input("Enter the direction NSWE:")
if dir == 'N':
    theseus_x_next = theseus_x
    theseus_y_next = theseus_y - 1

if dir == 'S':
    theseus_x_next = theseus_x
    theseus_y_next = theseus_y + 1

if dir == 'W':
    theseus_x_next = theseus_x - 1
    theseus_y_next = theseus_y

if dir == 'E':
    theseus_x_next = theseus_x + 1
    theseus_y_next = theseus_y

if (theseus_x_next, theseus_y_next) != 1:
    theseus_x = theseus_x_next
    theseus_y = theseus_y_next

    print("You are in the position", theseus_x, theseus_y)
    print("Please note that this is just the base of the game. In a future your movement will be stored so you can move across the labyrinth")

  ```
  
  Output:
  ````
Welcome to the Minotaur's labyrinth game!
  (Press enter in the keyboard to continue)

The Minotaur was the son of the Cretan Bull and Pasiphae, a human girl. King Minos asked Dedalos, the builder, to make a labyrinth to enclose the minotaur so that he would not kill the people of the city.
However, the Minotaur had to be fed so every so often 7 girls and 7 boys were given to him to eat.
Theseus was one of the boys who had to be sacrificed but he fell in love with Ariadna, the king's daughter. Ariadna was very clever so she gave Theseus a sewing thread to mark the path through the labyrinth.
Finally, Theseus managed to kill the Minotaur and return without getting lost to his house.
  (Press enter in the keyboard to continue)

Now, you can see an example on how the labyrinth would look like. You are @ and the Minotaur is M. Exit is E
The walls are # and the floor are .

##########
#..#.....#
#.@...#...#
#....#...#
#.....#..#
#.##.....#
#..####..#
#.#......#
#....#..M.#
######E###
  (Press enter in the keyboard to continue)

Now, you are Theseus and you need to move in the labyrinth. Use your keyboard to move.
Enter the direction NSWE:
````
#If you enter S, for example, the result will be:
```
You are in the position 2 3
Please note that this is just the base of the game. In a future your movement will be stored so you can move across the labyrinth
```
