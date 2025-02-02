import sys
import inflect
p = inflect.engine()
list = [ ]
while True:
  try:
        X=input("name: ").title()
        if len(X)<1:
          break
        else:
          list.append(X)
  except :
       print()
       break
output = p.join(list)
output1=("Adieu, adieu, to "+output)
print (output1)
