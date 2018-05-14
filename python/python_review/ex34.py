# Exercise 34 - Birthday JSON
# For JSON

# json library
# json.dump(json_obj, file)
# json.load(file)

import json

def write_json_birthdays(f_name, birthdays):
    with open(f_name, 'w') as open_file:
        json.dump(birthdays, open_file)

def read_json_birthdays(f_name):
    with open(f_name, 'r') as open_file:
        return json.load(open_file)
    

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

    f_name = 'birthdays.json'
    write_json_birthdays(f_name, birthdays)
    bdays_json = read_json_birthdays(f_name)

    print(texts['intro'])
    for key in bdays_json.keys():
        print(key)
    name = raw_input(texts['prompt'])
    
    if name in bdays_json:
        print("{}'s birthday is {}.".format(name, bdays_json[name]))
    else:
        print(texts['no_name'])
