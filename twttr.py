X=input("input: ")
result = " "
vowels =["a","e","i","o","u","A","E","I","O","U"]

for i in range(len(X)):
    if X[i] not in vowels :
         result=result+X[i]


print("after removing vowels: ", result)
