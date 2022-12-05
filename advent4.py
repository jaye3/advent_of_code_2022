# Part A
print("Day 4: Part A = ", end='')

def is_overlapping(section1, section2):
    areas1 = []
    areas2 = []
    for i in range(int(section1[0]), int(section1[1]) + 1):
        areas1.append(i)
    for j in range(int(section2[0]), int(section2[1]) + 1):
        areas2.append(j)
    if all(elm1 in areas2 for elm1 in areas1) or all(elm2 in areas1 for elm2 in areas2):
        return True
    else:
        return False


count = 0
with open('advent4.txt', 'r') as input_file:
    for line in input_file:
        pair = line.rstrip('\n').split(',')
        for i in range(len(pair)):
            pair[i] = pair[i].split('-')

        sect1, sect2 = pair[0], pair[1]
        if is_overlapping(sect1, sect2):
            count += 1
    
print(count)



# Part B
print("Day 4: Part B = ", end='')
def has_overlap(section1, section2):
    areas1 = []
    areas2 = []
    for i in range(int(section1[0]), int(section1[1]) + 1):
        areas1.append(i)
    for j in range(int(section2[0]), int(section2[1]) + 1):
        areas2.append(j)
    if any(elm1 in areas2 for elm1 in areas1) or any(elm2 in areas1 for elm2 in areas2):
        return True
    else:
        return False


count = 0
with open('advent4.txt', 'r') as input_file:
    for line in input_file:
        pair = line.rstrip('\n').split(',')
        for i in range(len(pair)):
            pair[i] = pair[i].split('-')

        sect1, sect2 = pair[0], pair[1]
        if has_overlap(sect1, sect2):
            count += 1
    
print(count)
