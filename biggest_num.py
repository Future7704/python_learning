number_list = [3, 6, 2, 8, 4, 10]

biggest_num = number_list[0]
for num in number_list[1:]:
    if num > biggest_num:
        biggest_num = num

print(biggest_num)