import sys


SEARCHED_WORD = 'XMAS'
REVERSED_WORD = 'SAMX'


def word_to_right(grid, start_i, start_j):
    if start_j + len(SEARCHED_WORD) > len(grid[start_i]):
        return False
    for j in range(start_j, start_j + len(SEARCHED_WORD)):
        if grid[start_i][j] != SEARCHED_WORD[j - start_j]:
            return False
    return True


# backwards
def word_to_left(grid, start_i, start_j):
    if start_j - len(SEARCHED_WORD) < -1:
        return False
    j = start_j
    while j > start_j - len(SEARCHED_WORD):
        if grid[start_i][j] != SEARCHED_WORD[start_j - j]:
            return False
        j -= 1
    return True


def word_to_up(grid, start_i, start_j):
    if start_i - len(SEARCHED_WORD) < -1:
        return False
    i = start_i
    while i > start_i - len(SEARCHED_WORD):
        if grid[i][start_j] != SEARCHED_WORD[start_i - i]:
            return False
        i -= 1
    return True


def word_to_down(grid, start_i, start_j):
    if start_i + len(SEARCHED_WORD) > len(grid):
        return False
    for i in range(start_i, start_i + len(SEARCHED_WORD)):
        if grid[i][start_j] != SEARCHED_WORD[i - start_i]:
            return False
    return True


def word_to_main_diag_down(grid, start_i, start_j):
    if start_j + len(SEARCHED_WORD) > len(grid[start_i]):
        return False
    if start_i + len(SEARCHED_WORD) > len(grid):
        return False
    for i in range(start_i, start_i + len(SEARCHED_WORD)):
        for j in range(start_j, start_j + len(SEARCHED_WORD)):
            if i - start_i == j - start_j and grid[i][j] != SEARCHED_WORD[i - start_i]:
                return False
    return True


def word_to_main_diag_up(grid, start_i, start_j):
    if start_j - len(SEARCHED_WORD) < -1 or start_i - len(SEARCHED_WORD) < -1:
        return False
    i = start_i
    j = start_j
    while i > start_i - len(SEARCHED_WORD) and j > start_j - len(SEARCHED_WORD):
        if i - start_i == j - start_j:
            if grid[i][j] != SEARCHED_WORD[start_i - i]:
                return False
        else:
            return False
        i -= 1
        j -= 1

    return True


def word_to_sec_diag_down(grid, start_i, start_j, SEARCHED_WORD=SEARCHED_WORD):
    if start_j - len(SEARCHED_WORD) < -1 or start_i + len(SEARCHED_WORD) > len(grid):
        return False
    i = start_i
    j = start_j
    while i < start_i + len(SEARCHED_WORD) and j >= start_j - len(SEARCHED_WORD) + 1:
        if i + j == start_i + start_j:
            if grid[i][j] != SEARCHED_WORD[i - start_i]:
                return False
        else:
            return False
        i += 1
        j -= 1
    return True


def word_to_sec_diag_up(grid, start_i, start_j):
    return word_to_sec_diag_down(grid, start_i, start_j, REVERSED_WORD)
"""
def word_to_sec_diag_up(grid, start_i, start_j):
    if start_j + len(SEARCHED_WORD) > len(grid[start_i]) or start_i - len(SEARCHED_WORD) < -1:
        return False
    i = start_i
    j = start_j
    for k in range(len(SEARCHED_WORD)):
        if i + j != start_i + start_j:
            return False
        if grid[i][j] != SEARCHED_WORD[k]:
            return False
        i -= 1
        j += 1
        if j >= len(grid[0]):
            return False
    return True
"""


number_of_apperances = 0


with open(sys.argv[1]) as file:
    letter_grid = file.read().split('\n')
    letter_grid = letter_grid[:len(letter_grid) - 1]
    print(letter_grid)
    i = 0
    while i < len(letter_grid):
        j = 0
        while j < len(letter_grid[i]):
            if word_to_right(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_left(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_up(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_down(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_main_diag_down(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_main_diag_up(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_sec_diag_down(letter_grid, i, j):
                number_of_apperances += 1
            if word_to_sec_diag_up(letter_grid, i, j):
                number_of_apperances += 1
            j += 1
        i += 1


print(number_of_apperances)
