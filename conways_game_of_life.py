import random, time, copy
WIDTH = 60

spam = [1, 2, 3]
eggs(spam)
print(spam) []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else: 
            column.append(' ') # Add a dead cell
    next_cell.append(column) # next_cell is a list of column lists
while True: # Main program loop
    print('\n\n\n\n\n') # Separate each step with new_lines.
    current_cell = copy.deepcopy(next_cell)
    # Print current_cell on yhe screen:
    #                  