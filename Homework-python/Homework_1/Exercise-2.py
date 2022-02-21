#!/usr/bin/env python3

#Author : Tomas
#Exercise 2 of the first automation track class

""" Q: Why result1 is None? :(  A: Because this function didn't have a return statement :)
    """
def multiply1(a,b):
	result = a*b
	print('Result: {0}'.format(result))
	return result #added returned statement


result1 = multiply1(2,4)
print(result1)

#######################################

""" Q: Why do we have only 15 instead of Result: 15 as well? :(  A: Because the function won't execute beyond the return ! You need to put your print before the return statement :)
    """
def multiply2(a,b):
	result = a*b
	print('Result: {0}'.format(result))
	return result #switched return statement - so that it is the last piece of code inside the function

result2 = multiply2(3,5)
print(result2)
