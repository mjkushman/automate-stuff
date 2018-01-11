import os
totalSize = 0
for filename in os.listdir('/Users/t_kushm/Projects/automate-stuff'):
	totalSize = totalSize + os.path.getsize(os.path.join('/Users/t_kushm/Projects/automate-stuff', filename))
	print(filename, os.path.getsize(os.path.join('/Users/t_kushm/Projects/automate-stuff',filename)))

print('Total size: ',totalSize)
