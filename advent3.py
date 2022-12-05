# Part A
print("Day 3: Part A = ", end='')
def get_item_priority(first, next, val_str):
    for ch1 in first:
        for ch2 in next:
            if ch1 == ch2:
                return val_str.find(ch1)
                    
priorities = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum_priorities = 0
with open("advent3.txt", 'r') as input_file:
    for line in input_file:
        line = line.rstrip("\n")
        mid = len(line) // 2
        sack1, sack2 =  line[:mid], line[mid:]
        sum_priorities += get_item_priority(sack1, sack2, priorities)
print(sum_priorities)

# Part B
print("Day 3: Part B = ", end='')
def get_badge_priority(first, next, last, val_str):
    common_1_2 = []
    for ch1 in first:
        for ch2 in next:
            if ch1 == ch2:
                common_1_2.append(ch1)
    for ch3 in last:
        if ch3 in common_1_2:
            return val_str.find(ch3)

all_sacks = []
curr_sack = []
with open("advent3.txt", 'r') as input_file:
    for line in input_file:
        line = line.rstrip("\n")
        if len(curr_sack) < 2:
            curr_sack.append(line)
        else:
            curr_sack.append(line)
            all_sacks.append(curr_sack.copy())
            curr_sack = []
        
total_priorities = 0
for trio in all_sacks:
    sack1, sack2, sack3 = trio[0], trio[1], trio[2]
    curr_badge = get_badge_priority(sack1, sack2, sack3, priorities)
    total_priorities += curr_badge

print(total_priorities)

