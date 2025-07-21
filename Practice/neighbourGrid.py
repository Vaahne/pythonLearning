#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    rows = len(grid)
    cols = len(grid[0]) if rows>0 else 0
    total = 0
    neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    for i in range(rows):
        for j in range(cols):
            valid = True
            for nr,nc in neighbours:
                r,c = i+nr,j+nc
                if 0 <= r < rows and 0<=c<cols:
                    if grid[i][j] <= grid[r][c]:
                        valid = False
                        break;
            if valid:
                total +=1
    return total            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
