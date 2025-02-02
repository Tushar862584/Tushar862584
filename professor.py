import random



def main():
    level=get_level()

    score = final (level)
    print ("final score :",score)

def get_level():
    while True:
        try:
            level= int(input("enter level [1,2,3] : "))
            list =[1,2,3]
            if level in list :
                return level
            else :
                print("EEE")
                pass
        except ValueError:
             print("EEE")
             pass

def final(level):
    round =1
    score =0
    while round <=10:
        x,y =generate_integer(level)
        final = process(x,y)
        if final ==True:
            score += 1
        round += 1
    return score

def process(x,y):
    test = 1
    while (test <= 3):
        try:
            answer= int(input(f"{x} + {y} = "))
            if answer == (x+y):
               return True
            else :
              test +=1
              print("EEE")
        except :
               test += 1
               print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def generate_integer(level):
    if level ==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
        return x,y
    elif level ==2:
         x=random.randint(10,99)
         y=random.randint(10,99)
         return x,y
    else:
         x=random.randint(100,999)
         y=random.randint(100,999)
         return x,y


if __name__ == "__main__":
    main()
