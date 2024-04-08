import unittest
from common.grid import GenerateGrid, GenerateRandomGrid
from common.neighbors import GetNeighborCounts, generateNeighbors
from common.debug import pp

global debug

class TestGridGeneration(unittest.TestCase):
    def test_size(self):
        grid = GenerateRandomGrid(Height=10, Width=10)
        self.assertEqual(len(grid), 10)
        self.assertEqual(len(grid[0]), 10)
        
        grid = GenerateRandomGrid(Height=10, Width=5)
        self.assertEqual(len(grid), 10)
        self.assertEqual(len(grid[0]), 5)
    
    def test_manual_positive_values(self):
        grid = GenerateGrid(Height=10, Width=10, FixedPositiveValues=[(0,0), (9,9)])
        self.assertEqual(grid[0][0], 1)
        self.assertEqual(grid[9][9], 1)
        count = 0
        for r in grid:
            for c in r:
                if c > 0:
                    count += 1
        self.assertEqual(count, 2)

class TestCellCountsStandard(unittest.TestCase):
    def test_count_center(self):
        Height, Width, NeighborhoodSize = 11, 11, 3
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(5,5)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),25)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)

    def test_count_edge(self):
        Height, Width, NeighborhoodSize = 11, 11, 3
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(5,1)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),21)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)
    
    def test_count_multiple_distinct(self):
        Height, Width, NeighborhoodSize = 11, 11, 2
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(3,7), (7,3)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),26)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)
    
    def test_count_multiple_overlap(self):
        Height, Width, NeighborhoodSize = 11, 11, 2
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(7,3), (6,5)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),22)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)

class TestCellCountsCustom(unittest.TestCase):
    def test_count_oddShapes(self):
        Height, Width, NeighborhoodSize = 1, 21, 1
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(0,5), (0,0)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),5)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)
    
    def test_count_oddShapes(self):
        Height, Width, NeighborhoodSize = 1, 1, 2
        grid = GenerateGrid(Height, Width, FixedPositiveValues=[(0,0)])
        self.assertEqual(GetNeighborCounts(grid, Height, Width, NeighborhoodSize),1)
        if debug:
            ng = generateNeighbors(grid, Height, Width, NeighborhoodSize)
            pp(grid, ng)

if __name__ == '__main__':
    debug = True
    unittest.main()
