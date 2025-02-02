from week4.fuel import convert, gauge
import pytest
def main():
    test_input()
    test_Valueerror()
    test_Zerodivisor()


def test_input():
    assert convert("1/4") == 25
    assert convert ("1/100") == 1
    assert convert ("99/100") == 99
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_Valueerror():
    with pytest.raises(ValueError):
        convert("the/me")
def test_Zerodivisor():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__ == "__main__":
    main()

