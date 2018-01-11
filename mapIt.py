#! python3
#mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    #Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)

'''
print('first arg (index 0): ' + sys.argv[0])
print('second arg (index 1): ' + sys.argv[1])
print('third arg (index 2): ' + sys.argv[2])
print('fourth arg (index 3): ' + sys.argv[3])
'''
