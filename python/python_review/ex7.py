# Exercise 7 - List Comprehensions

# range(incl, excl)
# list([iterable]) - converts sequence (string, tuples)
# or collection (set, dictionary) or iterator and converts to list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([num for num in a if num % 2 == 0])