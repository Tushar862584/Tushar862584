def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i=0

    if len(s)<2 or len(s)>6 :
        return False

    if s[0].isalpha()==False:
         return False
    if  s[1].isalpha()==False:
        return False
    for C in s:
     X=[ "_"," ","!","?","."]
     if C in X :
       return False




    while i<len(s):
       if s[i].isalpha() ==False:

            if s[i]=="0":
                return False
            else:
              break



       i += 1


    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False




    return True


if __name__ == "__main__":
    main()
