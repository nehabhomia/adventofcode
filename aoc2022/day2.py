import csv

file = open('inputs/day2.csv', 'r')
data = list(csv.reader(file, delimiter=' '))
file.close()

# print(data)

your_total = 0
elf_total = 0
your_score = 0
elf_score = 0

# scores = {'A': 1, 'B': 2, 'C': 3, 'Win': 6, 'Loss': 0, 'Draw': 3, 'X': 1, 'Y': 2, 'Z': 3}
#
# for each_list in data:
#     elf_action = each_list[0]
#     your_action = each_list[1]
#     if elf_action == 'A' and your_action == 'X':
#         elf_score = scores[elf_action] + scores['Draw']
#         your_score = elf_score
#     elif elf_action == 'B' and your_action == 'Y':
#         elf_score = scores[elf_action] + scores['Draw']
#         your_score = elf_score
#     elif elf_action == 'C' and your_action == 'Z':
#         elf_score = scores[elf_action] + scores['Draw']
#         your_score = elf_score
#     elif elf_action == "A":
#         if your_action == "Y":
#             your_score = scores[your_action] + scores['Win']
#             elf_score = scores[elf_action] + scores['Loss']
#         else:
#             your_score = scores[your_action] + scores['Loss']
#             elf_score = scores[elf_action] + scores['Win']
#     elif elf_action == "B":
#         if your_action == "Z":
#             your_score = scores[your_action] + scores['Win']
#             elf_score = scores[elf_action] + scores['Loss']
#         else:
#             your_score = scores[your_action] + scores['Loss']
#             elf_score = scores[elf_action] + scores['Win']
#     elif elf_action == "C":
#         if your_action == "X":
#             your_score = scores[your_action] + scores['Win']
#             elf_score = scores[elf_action] + scores['Loss']
#         else:
#             your_score = scores[your_action] + scores['Loss']
#             elf_score = scores[elf_action] + scores['Win']
#     your_total += your_score
#     elf_total += elf_score
#     # print(your_score)
#
# # if your_total > elf_total:
# #     print('you win!')
# # else:
# #     print('the elf wins!')
#
# print(your_total)

# part 2

scores = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
# a = rock, b = paper, c = scissors, x = lose, y = draw, z = win

for each_list in data:
    elf_action = each_list[0]
    result = each_list[1]
    if result == 'Y':
        elf_score = scores[elf_action] + scores['Y']
        your_score = elf_score
    elif result == "X":
        if elf_action == "A":
            your_action = 'C'
        elif elf_action == 'B':
            your_action = 'A'
        else:
            your_action = 'B'
        your_score = scores[your_action] + scores['X']
        elf_score = scores[elf_action] + scores['Z']
    elif result == "Z":
        if elf_action == "A":
            your_action = 'B'
        elif elf_action == 'B':
            your_action = 'C'
        else:
            your_action = 'A'
        your_score = scores[your_action] + scores['Z']
        elf_score = scores[elf_action] + scores['X']
    your_total += your_score
    elf_total += elf_score
    # print(your_score)
print(your_total)