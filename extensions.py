X=input("file name: ")
X1=X.lower()
if ".gif" in X1:
        print("image/gif")
elif ".jpg" in X1:
        print("image/jpeg")
elif ".jpeg" in X1:
        print("image/jpeg")
elif ".png" in X1 :
        print("image/png")
elif ".pdf" in X1:
        print("application/pdf")
elif ".txt" in X1 :
        print("text/plain")
elif ".zip" in X1:
        print("application/zip")
else:
        print("application/octet-stream")

