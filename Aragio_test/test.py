from problems import *

# global variables
NAME_MAX_LEN = 10
ROUND_TIME = 60*5
MIN_SCORE = 10
SCORE_DEP_RATE = 0.95


def test_check_user_name():
    assert check_user_name("") == False, "Empty name should return False"
    assert check_user_name(
        "a" * (NAME_MAX_LEN+1)) == False, "Names that exceed limit should return False"
    assert check_user_name(
        "a" * NAME_MAX_LEN) == True, "Names within the limit should return True"
    assert check_user_name("12 3") == True, "Name can be any characters"
    print("check_user_name function passed!")


# run tests
if __name__ == '__main__':
    print("Running tests")
    test_check_user_name()
