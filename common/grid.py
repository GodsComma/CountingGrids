from functools import partial
import random

def GenerateGrid(Height: int, Width: int, FixedPositiveValues: list[tuple[int,int]]=[]):
    """Generates a grid with a fixed values .

    Args:
        Height (int):Grid Height
        Width (int): Grid Width
        Fixed PositiveValues (list[tuple[int,int]], optional): Manual Positive Values for testing/debugging. Defaults to [].

    Returns:
        lst list[list[int]]: Grid that hosts the problem space
    """
    lst: list[list[int]] = []
    for _ in range(Height):
        new_lst = []
        for _ in range(Width):
            _val = _generate_random_val() if len(FixedPositiveValues) == 0 else _generate_random_val(True)
            new_lst.append(_val)
        lst.append(new_lst)
        
    for r,c in FixedPositiveValues:
        lst[r][c] = 1
    return lst

def _generate_random_val(OnlyNegatives=True):
    """Generate a random int value .

    Args:
        OnlyNegatives (bool, optional): . Defaults to True.

    Returns:
        (int): Value between -10 to 0 or -10 to 1
    """
    # random.seed(13)
    return random.randint(-10, 0) if OnlyNegatives else random.randint(10,1)


GenerateRandomGrid = partial(GenerateGrid, FixedPositiveValues=[])

def checkBounds(row: int, col: int, Height: int, Width: int):
    """Check the bounds of the bounding box .

    Args:
        row (int): row index
        col (int): col index
        Height (int): matrix height
        Width (int): matrix width

    Returns:
        bool: true, if (row,col) is with in bounds else false
    """
    if row < 0 or row >= Height:
        return False
    if col < 0 or col >= Width:
        return False
    return True