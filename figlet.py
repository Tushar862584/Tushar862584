import random
import sys
from pyfiglet import Figlet
if len(sys.argv)==1:
    normal =True
elif (len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[2]=='--f')):
    normal = False
else:
     print("Invalid usage")
     sys.exit(1)

figlet = Figlet()
X=input("input: ")

figlet.getFonts()
if normal == False:
  try:
     figlet.setFont(font=sys.argv[2])
     print(figlet.renderText(X))
  except:
      print("Invalid usage")
      sys.exit(1)
else:
    font=random.choice(figlet.getfonts())
    print(figlet.renderText(X))
