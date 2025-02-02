def main():
  Answer = input("what time is it: ")
  Time= convert(Answer)
  if ( Time >=7 and  Time <= 8) :
   print("breakfast time")
  elif (Time >= 12 and Time <= 13) :
   print("lunch time")
  elif (Time >= 18 and Time <= 19):
   print("dinner time")


def convert(time):

    hours, minutes = time.split(":")
    X= float(hours)+(float(minutes)/60)
    return X


main()
