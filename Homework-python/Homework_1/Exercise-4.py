#!/usr/bin/env python3


#Author : Tomas
#Exercise 4 of the first automation track class


def validate_age():
	birth_year = int(input("Hello, i'm going to need your birth year: "))
	if birth_year >= 1942:
		raise AssertionError("I'm afraid you're not old enough!")  # OR assert birth_year < 1942 , "I'm afraid you're not old enough!"
	else:	
		print("You're good to go, please wait in queue to get your shot")


validate_age()