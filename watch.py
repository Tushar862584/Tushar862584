import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
           url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9_]+)",s)
           if url :
              url1 = url.groups()
              return "https://youtu.be/" + url1[3]


if __name__ == "__main__":
    main()
