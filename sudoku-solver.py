from utils import *

# start = input("Entre com os dígitos do Sudoku ('.' para casas em branco): ")
initial_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

# display(initial_grid)
# print(grid_values(initial_grid))


def eliminate(values): # Receives a dictionary 
    # Iterates over all the puzzle boxes
    for box in values.keys():

        # If the box have only one value assigned to it,
        # it will replace this value from every one of its peers 
        if len(values[box]) == 1:
            for peer_box in peers[box]:
                values[peer_box] = values[peer_box].replace(values[box], '')
    return values                

def only_choice(values): # Receives a dictionary
    for unit in unitlist:
        for digit in '123456789':
            hits=0
            for box in unit:
                if digit in values[box]:
                    hits=hits+1
                    last_box = box
                if hits == 1:
                    values[last_box] = digit
    return values

e = eliminate(grid_values(initial_grid))
o = only_choice(e)
print(o)
