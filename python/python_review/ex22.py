# Exercise 22 - Read from File
# str.strip() removes the \n
# To add keys, just dict['newkey']

# Original
# with open("nameslist.txt", 'r') as open_file:
#     names_list = {}
#     name = open_file.readline().strip()
#     while name:
#         if name in names_list.keys():
#             names_list[name] += 1
#         else:
#             names_list[name] = 1
#         name = open_file.readline().strip()
#     for pair in names_list.items():
#         print(pair)

# Alternative - Better
# Key Difference: 'for line in open_file'
with open("nameslist.txt", 'r') as open_file:
    names_list = {}
    for line in open_file:
        name = line.strip()
        if name in names_list.keys():
            names_list[name] += 1
        else:
            names_list[name] = 1
    for pair in names_list.items():
        print(pair)