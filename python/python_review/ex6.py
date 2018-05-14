# Exercise 6 - String Lists

# len(Str)
# capital bools
# strings are list (of chars)
# string[ left : right : iter ]

def is_palindrome(a_str):
    half_len = len(a_str)/2
    for i in range(1, half_len):
        if a_str[i-1] != a_str[-i]:
            return False
    return True

# a_str[::] means string as is
# a_str[::-1] means string reversed (-1 == jump backwards by 1)
def is_palindrome_alt(a_str):
    return a_str == a_str[::-1]


user_in = raw_input("Enter any string: ")

if is_palindrome_alt(user_in):
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome.")