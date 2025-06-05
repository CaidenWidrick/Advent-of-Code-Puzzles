def check_coord(coord:tuple, lines:list):
    XMAS_count = 0
    
    row_num = int(coord[0])
    index = int(coord[1])

    sur_letters_abv = [char for i, char in enumerate(lines[row_num-1])]


file = 'input4.txt'
with open(file, 'r') as f:
    content = f.read()

lines = content.splitlines()

x_coords = [] #list of tuples -- (row num, index)
for i, line in enumerate(lines):
    x_indexes = [j for j, char in enumerate(line) if char == 'X']
    
    for coord_tuple in [(int(i), int(index)) for index in x_indexes]:
        x_coords.append(coord_tuple)