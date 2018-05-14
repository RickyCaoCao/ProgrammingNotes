# Exercise 4 - Divisors

# range(incl, excl)
# list([iterable]) - converts sequence (string, tuples)
# or collection (set, dictionary) or iterator and converts to list

num = int(raw_input("Enter a number: "))
divisors = [i for i in range(1, num+1) if num%i == 0]
print(divisors)