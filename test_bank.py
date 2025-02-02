from try.bank import value
def main():
    test_zero()
    test_20()
    test_100()

def test_zero():
    assert value("Hello guys") == 0
    assert value("hello") == 0
    assert value("Hello GUYS") == 0
    assert value("Hello ") == 0

def test_20():
    assert value("h") == 20
    assert value("HI") == 20
    assert value("how are you") == 20

def test_100():

    assert value("I AM FINE") == 100
    assert value("i am fine") == 100

if __name__ == "__main__":
    main()
