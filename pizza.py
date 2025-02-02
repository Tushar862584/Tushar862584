import csv
import sys
from tabulate import tabulate
if len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
         sys.exit("Too many command-line arguments")
if ".csv" not in sys.argv[1]:
         sys.exit("Not a csv file")
X= []
try :
        with open(sys.argv[1], "r") as csvfile:
          reader =csv.reader(csvfile)
          for line in reader:
            X.append(line)
except FileNotFoundError:
         sys.exit("File does not exist")
print(tabulate(X[1:],headers=X[0],tablefmt ="grid"))
