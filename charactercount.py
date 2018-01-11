import pprint
print('Type your message here:')
message = input()
message = message.lower()
count = {}
uniques = 0

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
uniques = len(count.keys())


print(str(uniques) + ' unique characters', )
print()
#I have no idea why the following function doesn't print out the dictionary all pretty. Instead of pretty, it prints in a row.
pprint.pprint(count)
