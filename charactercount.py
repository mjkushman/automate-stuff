import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message = message.lower()
count = {}
uniques = 0

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
uniques = len(count.keys())
pprint.pprint(uniques)
pprint.pprint(count)
