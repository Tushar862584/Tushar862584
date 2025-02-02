x , y, z = input("expression: ").split(" ")

x1=float(x)
z1=float(z)
if (y=="+"):
     A = x1 + z1
if (y=="-"):
     A = x1 - z1
if (y == "*"):
     A = x1 * z1
if (y == "/"):
     A = x1 / z1

print(A)
