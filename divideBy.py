def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error. Cannot divide by 0.')
print(spam(2))
print(spam(24))
print(spam(0))
 
