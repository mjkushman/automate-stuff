import os

for folderName, subfolders, filenames in os.walk('/users/t_kushm/projects'):
	print('Displaying ' + folderName.upper())

	print('\n---Subfolders in {}:'.format(folderName))
	for subfolder in subfolders:
		print('----/{}/'.format(subfolder))
	print('\n-----Files in ' + folderName + ':')
	for filename in filenames:
		print('------{})'.format(filenames.index(filename)+1), filename)

	print ('')
	print ('')