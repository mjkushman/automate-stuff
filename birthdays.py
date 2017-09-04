birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (leave blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(name + '\'s birthday is ' + birthdays[name])
    else:
        print('I do not have a birthday for ' + name)
        print('What is %s\'s birthday?' % (name))
        bday = input()
        birthdays[name] = bday
        print('Birthday for %s has been added.' % (name))
