import sys
def main():

    if len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
         sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
         sys.exit("Not a Python file")

    try:
         file = open(sys.argv[1],"r")
         lines= file.readlines()

    except FileNotFoundError:
         sys.exit("File does not exist")
    count = 0
    for line in lines:
            if not(line.isspace() or line.lstrip().startswith("#")):
                count += 1
    print(count)



if __name__== "__main__" :
   main()




