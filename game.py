import random
import sys
while True:
     try:
          X=int(input("Level:" ))
          random1 =random.randint(1,X)
          if X > 0:
               break
     except ValueError:
          pass
while True:
     try:
          guess=int(input("Guess: "))
          if guess > 0:
               if guess < random1:
                    print("Too small!")
               elif guess > random1:
                    print("Too large!")
               else :
                    print("Just right!")
                    sys.exit(1)

     except ValueError :
          pass

