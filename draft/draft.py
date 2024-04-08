import random

global nums
global colors

def generateNeighbors(grid: list, H: int, W: int, N: int):
    neighbors = []
    for row_index, i_value in enumerate(grid):
        for col_index, j_value in enumerate(i_value):
            if j_value > 0:
                nums.append((row_index, col_index))
                neighbors.append(getNeighbors(row_index, col_index, H, W, N))
    return neighbors

def getNeighbors(row: int, col: int, H: int, W: int, N: int):

    coordinates = set()
    coordinates.add((row,col))

    for i in range(N+1):
        left, right = (row,col-i), (row,col+i)
        top, bottom = (row-i,col), (row+i, col)

        if left[1] >= 0:
            coordinates.add(left)
        if right[1] < W:
            coordinates.add(right)
        if top[0] >= 0:
            coordinates.add(top)
        if bottom[0] < H:
            coordinates.add(bottom)
        
        start, end = left, top

        for dis in range(i):
            cur_row, cur_col = start[0]-dis , start[1]+dis
            if (cur_row, cur_col) == end:
                break
            if checkBounds(cur_row, cur_col, H, W):
                coordinates.add((cur_row, cur_col))

        start, end = top, right
        for dis in range(i):
            cur_row, cur_col = start[0]+dis, start[1]+dis
            if (cur_row, cur_col) == end:
                break
            if checkBounds(cur_row, cur_col, H, W):
                coordinates.add((cur_row, cur_col))
        
        start, end = right, bottom
        for dis in range(i):
            cur_row, cur_col = start[0]+dis, start[1]-dis
            if (cur_row, cur_col) == end:
                break
            if checkBounds(cur_row, cur_col, H, W):
                coordinates.add((cur_row, cur_col))
        
        start, end = bottom, left
        for dis in range(i):
            cur_row, cur_col = start[0]-dis, start[1]-dis
            if (cur_row, cur_col) == end:
                break
            if checkBounds(cur_row, cur_col, H, W):
                coordinates.add((cur_row, cur_col))
    return coordinates

def checkBounds(row: int, col: int, H: int, W: int):
    if row < 0 or row >= H:
        return False
    if col < 0 or col >= W:
        return False
    return True

def _main(H: int, W: int, N: int):
    if N >= max(H,W):
        print(H*W)
    grid = GenerateGrid(H, W)
    grid[0][0] = 1
    ngs = generateNeighbors(grid, H, W, N)
    
    if len(ngs) > 0:
        fin = ngs[0].union(*ngs)
        print(len(fin))
    for items in ngs:
        for co in items:
            x,y = co
            grid[x][y] = f'\033[{41}m  *  \033[0m'

    for i in nums:
        a,b = i
        grid[a][b] = f'\033[{colors[random.randint(0,2)% len(colors)]}m  +  \033[0m'
    print("="*10)
    pp(grid)
    print("="*10)

def GenerateGrid(H: int, W: int):
    lst = []
    for i in range(H):
        new_lst = []
        for j in range(W):
            new_lst.append(random.randint(-10, 0))
        lst.append(new_lst)
    return lst

## Print Formatter
def pp(lst: list):
    for i in range(len(lst[0])):
        if i == 0:
            print(f'{" ":>2}', end=" ")
        print(f'{i:>5}', end=" ")
    print('\n')
    count = 0
    for i in lst:
        for k, j in enumerate(i):
            if k == 0:
                print(f'{count:>2}', end=" ")
                count+=1
            print(f'{j:>5}', end=" ")
        print('\n')

if __name__ == "__main__":
    debug = False
    random.seed(3)
    nums = []
    colors = [42,43,44,45,46,47]
    # H > 0, W > 0, N >= 0
    H, W, N = 5, 5, 5
    _main(H, W, N)
