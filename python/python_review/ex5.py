# Exercise 5 - List Overlap

# range(incl, excl)
# list([iterable]) - converts sequence (string, tuples)
# or collection (set, dictionary) or iterator and converts to list
# use & and | on sets for intersection and union, respectively

import random as rand
import timeit
def gen_rand_int_list():
    return [rand.randint(1,100000) for i in range(rand.randint(1, 100))]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Faster
# print(set(a) & set(b))
# print(timeit.timeit('set([num for num in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]])'))

# Slower
# print(set([num for num in a if num in b]))
# print(timeit.timeit('set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) & set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])'))

# print(gen_rand_int_list())