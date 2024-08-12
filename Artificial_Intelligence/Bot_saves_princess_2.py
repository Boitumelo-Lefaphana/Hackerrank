def nextMove(n, r, c, grid):
    # Find the princess's position
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                pr, pc = i, j
                break
    
    # Calculate the difference between bot and princess positions
    row_diff = pr - r
    col_diff = pc - c
    
    # Determine the next move
    if row_diff < 0:
        return "UP"
    elif row_diff > 0:
        return "DOWN"
    elif col_diff < 0:
        return "LEFT"
    elif col_diff > 0:
        return "RIGHT"

# Input handling
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(n):
    grid.append(input())

# Get the next move
print(nextMove(n, r, c, grid))
