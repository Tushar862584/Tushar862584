from week8.um import count
def main():
    test_case()
    test_word()
    test_space()

def test_case():
     assert count("UM is") == 1
     assert count("UM is um") == 2


def test_word():
    assert count("yummi") == 0


def test_space():
    assert count("tushar um hello") == 1
    assert count("um!") == 1


if __name__ == "__main__":
    main()
