# Part A
print("Day 1: Part A = ", end='')

def get_highest_cal():
    highest = 0
    curr_calories = 0
    with open("advent1.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip("\n")
            if line.isdigit():
                cal = int(line)
                curr_calories += cal
            else:
                if curr_calories > highest:
                    highest = curr_calories
                curr_calories = 0
    return highest

print(get_highest_cal())

# Part B
print("Day 1: Part B = ", end='')

def get_totals():
    curr_calories = 0
    cal_list = []
    with open("advent1.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip("\n")
            if line.isdigit():
                cal = int(line)
                curr_calories += cal
            else:
                cal_list.append(curr_calories)
                curr_calories = 0
    return cal_list

max_sum = 0
all_totals = get_totals()

for i in range(3):
    max_cals = max(all_totals)
    max_sum += max_cals
    all_totals.remove(max_cals)

print(max_sum)
