from utils import *

# start = input("Entre com os dígitos do Sudoku ('.' para casas em branco): ")
initial_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
# initial_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

display(initial_grid)

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = eliminate(values)
        values = only_choice(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        # solved_values = len([box for box in values.keys() if len(values[box]) == 1])

        #False if there is a box with no value
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
            
    return values

result = reduce_puzzle(grid_values(initial_grid))
print('\nRESULT:')
display_dictionary(result)