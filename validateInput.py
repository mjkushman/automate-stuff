while True:
	print('enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('\nPlease enter a number for your age.')

while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():
		break
	print('\nPasswords can only have letters and numbers.')