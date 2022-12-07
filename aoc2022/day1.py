import csv

file = open('inputs/day1-1.csv', 'r')
data = list(csv.reader(file, delimiter='\n'))
file.close()

# print(data)

elf_dict = dict()
elf_num = 1
total_cals = 0
elf_cals = list()

for each_list in data:
    if len(each_list) != 0:
        total_cals += int(each_list[0])
        elf_dict[elf_num] = total_cals
    else:
        elf_num+=1
        total_cals = 0
        elf_cals = list()

max_cals = max(elf_dict.values())
# print(max_cals)  # part 1

three_max = sorted(elf_dict, key=elf_dict.get, reverse=True)[:3]

# print(three_max)

three_sum = 0

for each_key in three_max:
    val = elf_dict[each_key]
    three_sum += val

print(three_sum)  # part 2
