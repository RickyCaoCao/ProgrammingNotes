# Exercise 15 - Reverse Word Order
# str.split() == split on whitespace
# str.split('t') == split on 't'
# "*".join(a_list) == join list of strings with "*" between elements
# random.sample(a_list, rep) == create a list with rep number of samples of a_list

def reverse_phrase(a_str):
    return ' '.join(a_str.split()[::-1])

phrase = raw_input("Enter a multi-word phrase: ")
print(reverse_phrase(phrase))
