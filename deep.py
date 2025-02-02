X=input("enter the value")
X1=X.lower()
if (X1.strip()=="42"):
    print("yes")
elif(X1.strip()=="forty-two"):
    print("yes")
elif(X1.strip()=="forty two"):
    print("yes")
else :
    print("No")
