def displayPathtoPrincess(N, grid):
    # Find the bot's and princess's positions
    bot_position = None
    princess_position = None
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)
    
    bot_row, bot_col = bot_position
    princess_row, princess_col = princess_position
    
    # Calculate the difference in rows and columns
    row_diff = princess_row - bot_row
    col_diff = princess_col - bot_col
    
    # Determine the moves
    moves = []
    
    # Move vertically
    if row_diff > 0:
        moves.extend(["DOWN"] * row_diff)
    elif row_diff < 0:
        moves.extend(["UP"] * (-row_diff))
    
    # Move horizontally
    if col_diff > 0:
        moves.extend(["RIGHT"] * col_diff)
    elif col_diff < 0:
        moves.extend(["LEFT"] * (-col_diff))
    
    # Print the moves
    for move in moves:
        print(move)

# Example usage:
N = 3
grid = [
    "---",
    "-m-",
    "p--"
]

displayPathtoPrincess(N, grid)
