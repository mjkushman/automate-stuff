#tablePrinter
#tablePrinter prints out a table with justified rows and columns

'''Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose'''

''' NOTES
list of lists of strings.
like so:
listoflists = [
	['string1','string2'], #inner list 1
	['string3','string4']  #inner list 2
	]
In this example listoflists has 2 items, and each item has 2 more items.

In the desired output, reading left to right is :
list 1 string 1, list 2 string 1, list 3 string 1,
list 1 string 2, list 2 string 2, list 3 string 2,
list 1 string 3, list 2 string 3, list 3 string 3

'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(len(tableData))

def printTable(lists):
	colWidths = [0] * len(lists)
	print(colWidths)
	for i in lists:
		colWidths[i] = (max(lists, key=len)
	print(colWidths)

printTable(tableData)

#colWidths[0] = len(max(tableData[0], key=len))


