# Exercise 3 - List Less Than Ten
# SHIFT + ALT + DOWN/UP for copy line

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than_five(arr):
    b = []
    for num in arr:
        if num < 5:
            b.append(num)
    return b

# List Comprehension Method
# http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
a_filt = [num for num in a if num < 5]
# a_filt = less_than_five(a)
for num in a_filt:
    print(num)


