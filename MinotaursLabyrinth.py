# MINOTAUR'S LABYRINTH GAME
# In this game the user has to move through the labyrinth and reach the exit, without getting eaten by the Minotaur or lack of time

from random import randint
import time
import os

# CLEAR OUTPUT
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# LABYRINTH FUNCTION
# y is the row, x is the column
# 1 is wall, 2 is exit
def print_lab():
  for y in range(10):
    for x in range(10):
      if (x == minot_x) and (y == minot_y):
        print("M", sep="", end="")
      elif (x == theseus_x) and (y == theseus_y):
        print("@", sep="", end="")
      elif lab[y][x] == 2:
        print("E", sep="", end="")
      elif lab[y][x] == 1:
        print("#", sep="", end="")
      else:
        print(".", sep="", end="")
    print()

# MAIN PROGRAM
# Here I tell a brief resume of the greek myth and I link it to my game. Then I show an example of the labyrinth.
print("WELCOME TO THE MINOTAUR'S LABYRINTH GAME!")
name = input("What is your name?: ")
clear()
print("Hello", name + ", thanks for playing the Minotaur's Labyrinth game!")
print()
print("The Minotaur was the son of the Cretan Bull and Pasiphae, a human girl. King Minos asked Dedalos, the builder, to make a labyrinth to enclose the minotaur so that he would not kill the people of the city.")
print("However, the Minotaur had to be fed so every so often 7 girls and 7 boys were given to him to eat.")
print("Theseus was one of the boys who had to be sacrificed but he fell in love with Ariadna, the king's daughter. Ariadna was very clever so she gave Theseus a sewing thread to mark the path through the labyrinth.")
print("Finally, Theseus managed to kill the Minotaur and return without getting lost to his house.")
print()
print("  (Press enter in the keyboard to continue)")
input()
clear()
print("Now, you can see an example on how the labyrinth would look like. You are @ and the Minotaur is M. Exit is E")
print("The walls are # and the floor are .")
print()

# TWO TYPES OF LABYRINTHS
n = randint(1, 2)

if n == 1:
    lab = [[1,1,1,1,1,1,1,1,1,1],
           [1,0,0,1,0,0,0,0,0,1],
           [1,0,0,0,0,1,0,1,1,1],
           [1,0,1,0,1,1,0,0,0,1],
           [1,0,0,0,0,0,1,0,1,1],
           [1,0,1,1,0,0,0,0,0,1],
           [1,0,0,1,1,1,1,0,0,1],
           [1,0,1,0,0,0,0,0,0,1],
           [1,0,0,0,0,1,0,0,0,1],
           [1,1,1,1,1,1,1,1,2,1]]
    minot_x = 8
    minot_y = 8
    theseus_x = 2
    theseus_y = 1
    print("This is labyrinth 1:")

else:
    lab = [[1,1,1,1,1,1,1,1,1,1],
           [1,0,1,0,0,0,1,0,0,1],
           [1,0,0,0,0,1,1,0,1,1],
           [1,0,0,1,0,0,0,0,0,1],
           [1,0,1,1,1,1,0,1,0,1],
           [1,0,0,1,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,1],
           [1,1,0,1,1,0,1,1,0,1],
           [1,0,0,1,0,0,0,0,0,1],
           [1,1,1,1,2,1,1,1,1,1]]
    minot_x = 4
    minot_y = 5
    theseus_x = 8
    theseus_y = 1
    print("This is labyrinth 2:")

print_lab()
print()
print()
print("Your objective is to arrive to 'E', the exit, without being in the same point as the Minotaur.")
print("To move, use your keyboard: 'N' for North, 'S' for South, 'W' for West and 'E' for East.")
print()
print("  (Press enter in the keyboard to continue)")
input()
clear()

# LABYRINTH VISUALIZATION
# Here the user chooses if they want to play watching the labyrinth or not
print("GAME MODE:")
print("If you play during the day, you will see the labyrinth. If you play during the night, you won't.")
print("Hint: if it is the first time you play, day mode is easier.")
print()
mode = input("Please write 'NIGHT' for playing in the night and 'DAY' for playing in the day: ")
mode = mode.lower()
clear()
if (mode != "day") and (mode != "night"):
    print("I don't understand")
    mode = "day"

print('You are playing', mode, 'mode.')

if mode == "day":
    max_time = 120
    print("You have 2 minutes")
else:
    max_time = 360
    print("You have 6 minutes")


print("Now, you are like Theseus and you need to move in the labyrinth. Use your keyboard to move.")

mov = 0
init = time.time()

while(1):

  # TIME
  # Here the timer is set up. If instead of 20 minutes you want to play maximum 5, change 20 to 5
  elapsed = int(time.time() - init)
  left = max_time - elapsed
  elapsed_min = int(elapsed/60)
  elapsed_sec = int(elapsed%60)
  left_min = int(left/60)
  left_sec = int(left%60)


  # THESEUS MOVEMENT
  if mode == "night":
    print("If you need a hint, write HINT")
  else:
    print_lab()
    print()

  dir = input("Enter the direction NSWE:")
  clear()
  if dir == "N" or dir == "n":
      theseus_x_next = theseus_x
      theseus_y_next = theseus_y - 1
  elif dir == "S" or dir == "s":
      theseus_x_next = theseus_x
      theseus_y_next = theseus_y + 1
  elif dir == "W" or dir == "w":
      theseus_x_next = theseus_x - 1
      theseus_y_next = theseus_y
  elif dir == "E" or dir == "e":
      theseus_x_next = theseus_x + 1
      theseus_y_next = theseus_y
  elif dir == "HINT" or dir == "hint" or dir == "Hint":
      print("You are here: ")
      print_lab()
      print()
  else:
      theseus_x_next = theseus_x
      theseus_y_next = theseus_y
      print("INCORRECT DIRECTION. Please use N for North, S for South, E for East and W for West.")

  if lab[theseus_y_next][theseus_x_next] != 1:
      theseus_x = theseus_x_next
      theseus_y = theseus_y_next
      print(name, "moves to position", str(theseus_x)+(",")+str(theseus_y))
  else:
      print("Impossible, you hit a wall.", name, "stays in position", str(theseus_x)+(",")+str(theseus_y)+".", "Please go in other direction")

  # SCORES
  mov += 1
  if mov == 1:
    print(name, "has done", mov, "movement.")
  else:
    print(name, "has done", mov, "movements in total.")

  # TIME
  print("Time left:", str(left_min)+ "min,", str(left_sec)+ "s")
  print()

  # MINOTAUR MOVEMENT
  minot_x_next = minot_x + randint(-1, 1)
  minot_y_next = minot_y + randint(-1, 1)
  if lab[minot_y_next][minot_x_next] == 0:
    minot_x = minot_x_next
    minot_y = minot_y_next

  # EXIT CONDITIONS
  # The game finish and the user wins or loses
  if lab[theseus_y][theseus_x] == 2:
    print("Congratulations "+name+"! You did it!")
    score = int(((max_time*2 - mov - elapsed)/(max_time*2))*100)
    print("Your score is", score)
    print("You have arrived to the exit in", elapsed_min, "minutes and", elapsed_sec, "seconds and doing", mov, "movements.")
    if score > 80:
      print("Congratulations "+name+"! You are awesome!")
    elif score < 20:
      print("You did good", name, "but try harder the next time. You almost die!")
    else:
      print("Good job", name+"! If you continue playing you will be better!")

    score_file = "score.txt"
    s = open(score_file, "a")
    line = name + " - " + str(score) + "\n"
    s.write(line)
    s.close()
    s = open(score_file, "r")
    print()
    print("LAST SCORES: ")
    print(s.read())
    s.close()

    break

  if theseus_y == minot_y and theseus_x == minot_x:
    print()
    print("Oh no, the minotaur has eaten", name+"!")
    print("GAME OVER")
    break

  if elapsed > max_time:
    print()
    print("Time over.", name, "is tired and dies.")
    print("GAME OVER")
    break

# END GAME
input()

