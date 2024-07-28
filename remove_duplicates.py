original_list = [4, 3, 2, 3, 5, 1, 4, 4, 6, 4]
unique_list = []

for i in original_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)
