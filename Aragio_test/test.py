from problems import *


##################################
# DON'T EDIT THIS FILE!
# Only run this file using `python test.py` in the terminal
##################################


# global variables
NAME_MAX_LEN = 10
ROUND_TIME = 60*5
MIN_SCORE = 10
SCORE_DEP_RATE = 0.95


def test_check_user_name():
    if check_user_name("") == None:
        pass
    else:
        assert check_user_name("") == False, "Empty name should return False"
        assert check_user_name(
            "a" * (NAME_MAX_LEN+1)) == False, "Names that exceed limit should return False"
        assert check_user_name(
            "a" * NAME_MAX_LEN) == True, "Names within the limit should return True"
        assert check_user_name("12 3") == True, "Name can be any characters"
        print("function 1 check_user_name function passed!\n")


def test_convert_time():
    if convert_time(ROUND_TIME) == None:
        pass
    else:
        assert convert_time(
            ROUND_TIME) == "Starting Soon", "Should say `Starting Soon` at the start time of the round"
        assert convert_time(
            1) == "00:01", "1 second should return the string `00:01`"
        assert convert_time(61) == "01:01", "61 seconds should return `01:01`"
        assert convert_time(
            3600) == "60:00", "3600 seconds should return `60:00`"
        print("function 2convert_time function passed!\n")


def test_format_data():
    if format_data(0, 0) == None:
        pass
    else:
        assert format_data(3, 4) == "move 3 4", "Correct format!"
        assert format_data(-1, 0) == "move -1 0", "Negative values should work"
        print("function 3 format_data function passed!\n")


def test_release_mass():
    players = {0: {"x": 0, "y": 0, "color": (100, 100, 100), "score": 100, "name": "Ori"},
               1: {"x": 100, "y": 100, "color": (200, 200, 200), "score": 200, "name": "Oreo"},
               }
    if release_mass(players) == None:
        pass
    else:
        assert release_mass(players) == {0: {"x": 0, "y": 0, "color": (100, 100, 100), "score": 95, "name": "Ori"},
                                         1: {"x": 100, "y": 100, "color": (200, 200, 200), "score": 190, "name": "Oreo"},
                                         }, "Score correctly depleted!"
        print("function 4 release_mass function passed!\n")


def test_distance():
    if distance(0, 0, 3, 4) == None:
        pass
    else:
        assert (0, 0, 3, 4) == 5, "Correct calculation!"
        assert (0, 0, -3, -4) == 5, "Negative coordinates should work"
        assert (1, 1, 1, 1) == 0, "Same point should return distance of 0"
        print("function 5 distance function passed!\n")


def test_player_collision():
    if player_collision((0, 0, 1), (2, 0, 1)) == None:
        pass
    else:
        assert player_collision(
            (0, 0, 1), (2, 0, 1)) == True, "Players touch at (1, 0)"
        assert player_collision(
            (0, 0, 1), (0, 1, 1)) == True, "Players overlap"
        assert player_collision((-1, -1, 1), (-1, -1, 1)
                                ) == True, "Players are at same coordinate"
        assert player_collision(
            (100, -100, 1), (-100, 100, 1)) == False, "Players don't touch"
        assert player_collision(
            (10, 10, 10), (-10, -10, 10)) == False, "Players don't touch"
        print("function 6 player_collision function passed!")


# run tests
if __name__ == '__main__':
    print("\nRunning tests...\n")
    test_check_user_name()
    test_convert_time()
    test_format_data()
    test_release_mass()
    test_distance()
    test_player_collision()
    print("Finished running tests\n")
