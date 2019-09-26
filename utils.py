rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

# Returns a dictionary 
def grid_values(grid):
    values = []
    all_digits='123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

#Print sudoku strings
def display(grid_values):
    grid_display = ''
    i=1
    for value in grid_values:
        if i%27 == 0 and i<=56:
            grid_display = grid_display + value + '\n------+------+------\n'
        elif i%9 == 0:
            grid_display = grid_display + value + '\n'
        elif i%3 == 0:
            grid_display = grid_display + value + ' |'
        else: 
            grid_display = grid_display + value + ' '        
        i = i+1
    print(grid_display)