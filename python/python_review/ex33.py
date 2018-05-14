# Exercise 33 - Birthday Dictionaries
# For dictionaries

# use dict.get(key, default_val) to prevent key doesn't exist errors
# forward slash is escape character

if __name__ == "__main__":
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'
    }

    texts = {
        'intro': 'Welcome to the birthday dictionary. We know the birthdays of: ',
        'prompt': 'Who\'s birthday do you want to look up? ',
        'no_name': 'Sorry, that name is not in the dictionary. '
    }

    print(texts['intro'])
    for key in birthdays.keys():
        print(key)
    name = raw_input(texts['prompt'])
    
    if name in birthdays:
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print(texts['no_name'])
