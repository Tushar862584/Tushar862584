def main():
    X=input("Fraction:")
    Y= convert(X)
    Z= gauge(Y)
    print(Z)



def convert(fraction):
    while True:
      try:
         numerator,denominator= fraction.split("/")
         x1=int(numerator)
         y1=int(denominator)
         F = x1 / y1
         if (F <= 1):
            T = int(F*100)
            return T
      except (ValueError, ZeroDivisionError):
         pass




def gauge(T):
    if (T<=1):
        return "E"
    elif (T>=99):
        return "F"
    else:
        return str(T) + "%"



if __name__ == "__main__":
    main()
