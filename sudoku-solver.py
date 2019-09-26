from utils import *

# start = input("Entre com os dígitos do Sudoku ('.' para casas em branco): ")
initial_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

# display(initial_grid)
# print(grid_values(initial_grid))

#Receives a dictionary 
def eliminate(values):
    # Iterates over all the puzzle boxes
    for box in values.keys():

        # If the box have only one value assigned to it,
        # it will replace this value from every one of its peers 
        if len(values[box]) == 1:
            for peer_box in peers[box]:
                values[peer_box] = values[peer_box].replace(values[box], '')
    return values                



d = eliminate(grid_values(initial_grid))
print(d)