def main():
      X=  (input("enter string "))
      print(convertor(X))


def convertor(X):
      X1=X.replace(":)",'🙂')
      X2=X1.replace(":(",'🙁')
      return X2



main()
