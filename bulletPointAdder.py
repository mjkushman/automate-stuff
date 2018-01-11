#! /usr/bin/env python3
#bullet point adder adds bullet points to the beginning of each line of copied text.

import pyperclip
text = pyperclip.paste()


#Separate lines and add stars.
lines = text.split('\n')
for i in range (len(lines)):  #look through all incexes in the "lines" list
	lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

