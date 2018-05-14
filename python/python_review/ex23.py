# Exercise 23 - File Overlap
# .read() -> reads entire file and makes it 1 string
# .readlines() -> read all lines of file and outputs list of lines

# Using map function
def read_nums_alt(filename):
    with open(filename, 'r') as o_file:
        return map(lambda num: int(num), o_file.readlines())

def read_nums(filename):
    return read_nums_alt(filename)
    # num_list = []
    # with open(filename, 'r') as o_file:
    #     for num in o_file:
    #         num_list.append(int(num))
    # return num_list

primes = read_nums('primenumbers.txt')
hapnums = read_nums('happynumbers.txt')

print([i for i in primes if i in hapnums])


    