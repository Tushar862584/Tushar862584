from  try.twttr import shorten

def main():
    testalpha()
    testdigit()
    testsymbol()


def testalpha():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("What's your name") == "Wht's yr nm"
    assert shorten("TwTTeR") == "TwTTR"

def testdigit():
    assert shorten("1298") == "1298"

def testsymbol():
    assert shorten("????") == "????"
    assert shorten("'''") =="'''"


if __name__ == "__main__":
    main()
