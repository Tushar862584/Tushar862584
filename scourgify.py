import sys
import csv


if len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")
if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
         sys.exit("Not a csv file")
X=[]
try :
        with open(sys.argv[1], "r") as csvfile:
          reader =csv.DictReader(csvfile)
          for line in reader:
            last,first= line["name"].split(",")
            X.append({"first": first.lstrip(), "last": last , "house" : line["house"]})

except FileNotFoundError:
         sys.exit(f"could not read {sys.argv[1]}")
with open(sys.argv[2], "w") as file:
          writer =csv.DictWriter(file,fieldnames=["first","last","house"])
          writer.writerow({"first": "first" , "last" : "last" , "house" : "house"})
          for line in X:
                  writer.writerow({"first": line["first"] , "last" : line["last"] , "house" : line["house"]})


