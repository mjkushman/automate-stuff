#! /usr/bin/env python3
#This program is a password locker. Allows user to keep track of passwords, and copy/paste required pw.

#pw.py - an insecure password locker program.

#k/v pairs are account name/password
PASSWORDS = {'email': 'abcdefg1234567',
			 'blog': 'nrienaielurns432452435',
			 'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]  #first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to the clipboard.')
else:
	print('There is no account named ' + account)
	