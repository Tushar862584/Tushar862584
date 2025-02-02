import re


def main():
    print(count(input("Text: ")))


def count(s):
   list = re.findall(r"\b\w*um\w*" , s , re.IGNORECASE)
   return len(list)
if __name__ == "__main__":
    main()
