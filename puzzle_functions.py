# The constants describing the multiplicative factor for finding a word in
# a particular direction.  These should be used in function get_points.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4


def get_current_player(player_one_turn):
    """ (bool) -> str

    Return 'Player One' iff player_one_turn is True; otherwise, return
    'Player Two'.

    >>> get_current_player(True)
    'Player One'
    
    >>> get_current_player(False)
    'Player Two'
    """
    
    # Complete this function
    
    if player_one_turn == True:
        return 'Player One'
    else:
        return 'Player Two'

# Define the other functions from the handout here

def get_factor(direction):
    ''' (str) -> int
        
    Return the corresponding factor associated with each direction.
        
    >>> get_factor('up')
    4
    >>> get_factor('down')
    2
    '''
    
    if direction == 'up':
        return UP_FACTOR
    elif direction == 'down':
        return DOWN_FACTOR
    elif direction == 'forward':
        return FORWARD_FACTOR
    elif direction == 'backward':
        return BACKWARD_FACTOR
    
def get_points(direction, words_left):
    ''' (str, int) -> int
    
    Return the score that would be earned iff the word were to be found with 
    the given direction and the remaining words in words_left. 
    
    >>> get_points ('up', 5)
    20
    >>> get_points ('forward', 1)
    34
    '''
    
    if words_left >= 5:
        return words_left * get_factor(direction)
    elif 5 > words_left > 1:
        return (10 - words_left) * get_factor(direction)
    else:
        return ((10 - words_left) * get_factor(direction)) + 25  
    
def calculate_score (puzzle, direction, guess, row_or_col_num, words_left):
    ''' (str, str, str, int, int) -> int
    
    Return the appropriate score iff the puzzle contains guess in the given
    direction and given row or column number(row_or_col_num) with the 
    remaining words in word_left.
    
    >>> calculate_score (skbc\silk\lscs, 'forward', 'silk', 1, 5)
    5
    >>> calculate_score (tfvh\khho\jkdf, 'up', 'tkf', 0, 5)
    0
    '''
    
    if direction == 'forward' and contains(get_row(puzzle, row_or_col_num), guess):
        return get_points (direction, words_left)
    elif direction == 'backward' and contains(get_row(puzzle, row_or_col_num), (reverse(guess))):
        return get_points (direction, words_left)
    elif direction == 'down' and contains(get_column(puzzle, row_or_col_num), guess):
        return get_points (direction, words_left)
    elif direction == 'up' and contains(get_column(puzzle, row_or_col_num), (reverse(guess))):
        return get_points (direction, words_left)
    else:
        return 0    
    
def get_winner (player_one_score, player_two_score):
    ''' (int, int) -> str
    
    Return the string 'Player One wins!', 'Player Two Wins!' or 'Tie game!' 
    as appropriate based on player_one_score and player_two_score. 
    
    >>> get_winner (1, 5)
    'Player Two Wins!'
    >>> get_winner (1, 1)
    'Tie Game!'
    >>> get_winner (5, 1)
    'Player One Wins!'
    '''
    
    if player_one_score > player_two_score:
        return 'Player One Wins!'
    elif player_one_score == player_two_score:
        return 'Tie Game!'
    else:
        return 'Player Two Wins!'    
    
# Helper functions.  Do not modify these, although you are welcome to call
# them.

def get_row(puzzle, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle

    Return row row_num of puzzle.

    >>> get_row('abcd\\nefgh\\nijkl\\n', 1)
    'efgh'
    """

    rows = puzzle.strip().split('\n')
    return rows[row_num]


def get_column(puzzle, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle

    Return column col_num of puzzle.
    >>> get_column('abcd\\nefgh\\nijkl\\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def reverse(s):
    """ (str) -> str

    Return a reversed copy of s.

    >>> reverse('abc')
    'cba'
    """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed

    return s_reversed


def contains(s1, s2):
    """ (str, str) -> bool

    Return whether s2 appears anywhere in s1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return s2 in s1
