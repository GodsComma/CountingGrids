import random

## Print Formatter
def pp(grid: list[list[int]], ngs: list[tuple[int,int]]=[]):
    """Pretty print list of indices.

    Args:
        lst (list[list[int]]): Grid to print items
    """
    print("= "*(3*len(grid[0])+2))
    colors = [42,43,44,45,46,47]
    for items in ngs:
        for co in items:
            x,y = co
            if type(grid[x][y]) is int and grid[x][y] > 0:
                grid[x][y] = f'\033[{colors[random.randint(0,2)% len(colors)]}m  +  \033[0m'
            elif type(grid[x][y]) is not str:
                grid[x][y] = f'\033[{41}m  *  \033[0m'
    
    for i in range(len(grid[0])):
        if i == 0:
            print(f'{" ":>2}', end=" ")
        print(f'{i:>5}', end=" ")
    print('\n')
    count = 0
    for i in grid:
        for k, j in enumerate(i):
            if k == 0:
                print(f'{count:>2}', end=" ")
                count+=1
            print(f'{j:>5}', end=" ")
        print('\n')