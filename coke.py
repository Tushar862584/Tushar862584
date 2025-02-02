amount_due = 50


while amount_due > 0:
   print("Amount Due :", amount_due)
   X = int(input("Insert Coin: "))
   if X in [25 ,10 ,5]:
     amount_due -= X


change_owed = abs(amount_due)
print("changed owed: ",change_owed)

