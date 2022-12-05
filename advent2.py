# Part A
print("Day 2: Part A = ", end='')

outcome_dict = {
    ("A", "X"): (1, 3), 
    ("A", "Y"): (2, 6), 
    ("A", "Z"): (3, 0),
    ("B", "X"): (1, 0), 
    ("B", "Y"): (2, 3), 
    ("B", "Z"): (3, 6),
    ("C", "X"): (1, 6), 
    ("C", "Y"): (2, 0), 
    ("C", "Z"): (3, 3)
}

def get_total_points(outcome_dict):
    total_points = 0
    with open("advent2.txt", 'r') as input_file:
        for line in input_file:
            move = line.rstrip("\n").split(" ")
            move = tuple(move)
            total_points += sum(outcome_dict[move])
    print(total_points)

get_total_points(outcome_dict)

# Part B
print("Day 2: Part B = ", end='')

winning_dict = {
    ("A", "X"): (3, 0), 
    ("A", "Y"): (1, 3), 
    ("A", "Z"): (2, 6),
    ("B", "X"): (1, 0), 
    ("B", "Y"): (2, 3), 
    ("B", "Z"): (3, 6),
    ("C", "X"): (2, 0), 
    ("C", "Y"): (3, 3), 
    ("C", "Z"): (1, 6)
}

get_total_points(winning_dict)

