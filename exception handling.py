
import sys
a = 10
b = [1,2,3,4]
c = 7

def divide(a,b):
	if b == 0:
		raise ZeroDivisionError("Cannot divide by zero")
	return a/b

try:
	c = divide(5, b[c])
	raise Exception("Chumma oru error")
	print("Value of c is {}".format(c))
except (NameError, IndexError, KeyError) as e:
	print("Error happened: {}".format(e))
except ZeroDivisionError as e:
	print("ZeroDivisionError: {}".format(e))
else:
	print("All good")
finally:
	print("Whatever the case is, I will work")
