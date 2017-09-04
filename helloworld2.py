def spam():
    global eggs
    eggs = 'changed to spam'

eggs = 'global'
spam()
print(eggs)
