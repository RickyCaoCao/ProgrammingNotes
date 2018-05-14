# Exercise 1 - Character Input
# From https://www.practicepython.org/
# Use raw_input(...) as it takes it as string
# input(...) uses "eval"


name = raw_input("Provide your name: ")
age = raw_input("Provide your age: ")
repeat = int(raw_input("Repeats: "))
age = 2018+100-int(age)
print("Your name is {} and you will be 100 in the year {}".format(name, age))
print(repeat * "lol\n")