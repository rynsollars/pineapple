__author__ = 'ryansollars'

def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        return('Error: Invalid argument')

print (spam(42))
print (spam(12))
print (spam(0))
print (spam(1))

