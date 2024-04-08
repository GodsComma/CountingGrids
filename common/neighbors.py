from common.grid import checkBounds

def GetNeighborCounts(grid: list, Height: int, Width: int, NeighborhoodSize: int):
    """Retrieves the number of neighboring cells in the grid ."""
    neighbors =  generateNeighbors(grid, Height, Width, NeighborhoodSize)
    return _getUniqueCount(neighbors)

def generateNeighbors(grid: list, Height: int, Width: int, NeighborhoodSize: int):
    """Generates a list of neighbors for each node in a grid .
    Returns:
        list[tuple[int,int]]: List of valid neighbors for all of the positive values in the grid
    """
    neighbors = []
    for row_index, i_value in enumerate(grid):
        for col_index, j_value in enumerate(i_value):
            if j_value > 0:
                neighbors.append(_getNeighbors(row_index, col_index, Height, Width, NeighborhoodSize))
    return neighbors

def _getUniqueCount(Neighbors):
    """Returns the number of unique neighbors in the given list of Neighbors .
    """
    # Add Optimization Here
    if len(Neighbors) == 0:
        return 0
    return len(Neighbors[0].union(*Neighbors))

def _getNeighbors(row: int, col: int, H: int, W: int, N: int):
    """Get the coordinates of the neighboring nodes of a given co-ordinate .

    Returns:
        set(tuple(row, col)): set of neighbors for a given co-ordinate
    """
    
    # TODO: Add check for when N > Distance between (0,0) and (H,W) and if N is larger the
    # ignore the calculations and return H * W

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
