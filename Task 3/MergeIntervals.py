# A list of tuples
intervals_list = [(1, 3), (2, 6), (8, 10), (15, 18)]

# Sort the intervals
intervals_list.sort()

# Creating a list of individual elements of tuples
listed = []
for i in intervals_list:
    for j in i:
        listed.append(j)

# Creating a new list by skipping the elements if they lie in the interval
new_list = []
i = 0
while i < len(listed) - 1: 
    if (listed[i] > listed[i+1]) or (listed[i] == listed[i+1]):
        i += 2  
    else:
        new_list.append(listed[i])
        i += 1
new_list.append(listed[-1])

# Merging the intervals
merged_intervals = []
for i in range(0, len(new_list)-1, 2):
    merged_intervals.append(tuple(new_list[i:i+2]))

print(merged_intervals)