# Exercise 2 - Odd or Even

# try/except
# isdigit()
# type(num) is not int

def reps_int(num):
    if num.isdigit():
        return int(num)
    return "NaN"

def check_parity(num):
    if num == "NaN":
        return "Not a number ._."
    elif(num % 2 == 0):
        return "even"
    return "odd"
    
def check_four_mult(num):
    if (num != "NaN") and (num % 4 == 0):
        print("Your number is also divisible by four!")

user_input = raw_input("Enter a number: ")
num = reps_int(user_input)
print("Your number is {}!".format(check_parity(user_input)))