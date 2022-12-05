'''
[V]         [T]         [J]        
[Q]         [M] [P]     [Q]     [J]
[W] [B]     [N] [Q]     [C]     [T]
[M] [C]     [F] [N]     [G] [W] [G]
[B] [W] [J] [H] [L]     [R] [B] [C]
[N] [R] [R] [W] [W] [W] [D] [N] [F]
[Z] [Z] [Q] [S] [F] [P] [B] [Q] [L]
[C] [H] [F] [Z] [G] [L] [V] [Z] [H]
 1   2   3   4   5   6   7   8   9 
'''

# Part A
print("Day 5: Part A = ", end='')

positions = [
    ['C','Z','N','B','M','W','Q','V'],
    ['H','Z','R','W','C','B'],
    ['F','Q','R','J'],
    ['Z','S','W','H','F','N','M','T'],
    ['G','F','W','L','N','Q','P'],
    ['L','P','W'],
    ['V','B','D','R','G','C','Q','J'],
    ['Z','Q','N','B','W'],
    ['H','L','F','C','G','T','J']
]

# test = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P']
# ]
    
def get_move_info(line):
    qty_og_end = ''
    for i in range(len(line) - 1):
        if line[i].isdigit():
            qty_og_end += line[i]
            if not line[i+1].isdigit():
                qty_og_end += ' '
    if line[-1].isdigit():
        qty_og_end += line[-1]
    move_info = qty_og_end.split()  
    return move_info

def move_box(original, move_info):
    qty, start, final = int(move_info[0]), int(move_info[1]) - 1, int(move_info[2]) - 1
    for i in range(qty):
        curr_box = original[start][-1]
        original[start].pop(-1)
        original[final].append(curr_box)


with open('advent5.txt','r') as input_file:
    for line in input_file:
        move_info = get_move_info(line)
        move_box(positions, move_info)

final_str = ''
for j in range(len(positions)):
    final_str += positions[j][-1]
print(final_str)


# Part B
print("Day 5: Part B = ", end='')
positions = [
    ['C','Z','N','B','M','W','Q','V'],
    ['H','Z','R','W','C','B'],
    ['F','Q','R','J'],
    ['Z','S','W','H','F','N','M','T'],
    ['G','F','W','L','N','Q','P'],
    ['L','P','W'],
    ['V','B','D','R','G','C','Q','J'],
    ['Z','Q','N','B','W'],
    ['H','L','F','C','G','T','J']
]

def move_boxes(original, move_info):
    qty, start, final = int(move_info[0]), int(move_info[1]) - 1, int(move_info[2]) - 1
    boxes = []
    for i in range(qty, 0, -1):
        curr_box = original[start][-i]
        boxes.append(curr_box)
        original[start].pop(-i)
    original[final].extend(boxes)
    

with open('advent5.txt','r') as input_file:
    for line in input_file:
        move_info = get_move_info(line)
        move_boxes(positions, move_info)

final_str = ''
for j in range(len(positions)):
    final_str += positions[j][-1]
print(final_str)