from week8.numb3rs import validate

def main():
    test_size()
    test_range()

def test_size():
    assert validate(r"1.2.3.4") == True
    assert validate(r"32.12.67.90") == True
    assert validate(r"32.12.67.90.60") == False
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False


def test_range():
     assert validate (r"255.255.255.255") == True
     assert validate(r"500.1.1.1") == False
     assert validate(r"1.500.1.1") == False
     assert validate(r"1.1.500.1") == False
     assert validate(r"1.1.1.500") == False
     assert validate(r"tushar") == False

if __name__== "__main__" :
   main()
