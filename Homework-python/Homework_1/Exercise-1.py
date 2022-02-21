#!/usr/bin/env python3

# Author : Tomas
# Exercise 1 of the first automation track class
# Function 1 was the most obvious solution
# Function 2 was an improvement to make the code more elegant, but ended up with the same amount of lines of code


# Function 1 : most intuitive solution
print('Function 1 - most intuitive')
def cumulative_sum():
    total = 0
    for i in range(5):
        summ = i+(i+1)
        total += summ
        print(summ)
    print(total)
    
cumulative_sum()

# Function 2 : more elgant, usage of lambda function
print('Function 2 - lambda usage')
def cumulative_sum():
    total = 0
    add_x = lambda x : x + (x+1)
    for i in range(5):
        total += add_x(i)
        print(add_x(i))
    print(total)

    
cumulative_sum() 
