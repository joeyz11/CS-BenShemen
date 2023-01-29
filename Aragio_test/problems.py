##################################
# Only edit the function bodies and return statements!
##################################

# global variables
NAME_MAX_LEN = 10
ROUND_TIME = 60*5
MIN_SCORE = 10
SCORE_DEP_RATE = 0.95


# Demo function
def list_sum(num_list):
    """
    Sums up the values in a list

    Paramters
        num_list (list): a list of numbers
    Returns
        my_sum (int): the sum of the values in the list
    """
    return None


# function 1: check_user_name()
def check_user_name(name):
    """
    Checks if name can be used.

    Parameters
        NAME_MAX_LEN
    Returns
        valid (bool): True if the length of `name` is between 1 and NAME_MAX_LEN [inclusive]
    """
    return None


# function 2: convert_time(t_sec)
def convert_time(t_sec):
    """
    Convert a time given in seconds to a time in minutes as a string.

    Parameters
        t_sec (int): time in seconds
        ROUND_TIME
    Returns
        t_min (str): time formatted MM:SS as a string if t_sec is less than ROUND_TIME, else return the string `Starting Soon`
    """
    return None


# function 3: format_data(x, y)
def format_data(x, y):
    """
    Formats updated x and y coordinate.

    Parameters
        x (int): The updated x coordinate
        y (int): The updated y coordinate
    Returns
        A string in the format `move x y` where x and y are replaced by values
    """
    return None


# function 4: release_mass(players)
def release_mass(players):
    """
    Decreases score of players whose score is greater than MIN_SCORE to SCORE_DEP_RATE the original score. 

    Parameters
        players (dict): a dict of players mapping id to player 
            where each player is the dict {"x": int, "y": int, "color": tuple, "score": int, "name": str}
        MIN_SCORE
        SCORE_DEP_RATE
    Returns
        players (dict): the updated dict
    """
    return None


# function 5: distance(x1, y1, x2, y2)
def distance(x1, y1, x2, y2):
    """
    Finds the distance between two points.

    Paramters
        x1 (int): x coordinate of first point
        y1 (int): y coordinate of first point
        x2 (int): x coordinate of second point
        y2 (int): y coordinate of second point
    Returns
        dis (int): distance between the two points
    """
    return None


# function 6: player_collision(p1, p2)
def player_collision(p1, p2):
    """
    Calculates if the two players are colliding or not.

    Parameters
        p1 (tuple): player 1 in the form of a tuple (center_x, center_y, radius)
        p2 (tuple): player 2 in the form of a tuple (center_x, center_y, radius)
    Returns
        colliding (bool): True if the two players touches, False otherwise
    """
    return None
