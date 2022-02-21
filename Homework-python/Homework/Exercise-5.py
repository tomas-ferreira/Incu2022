#!/usr/bin/env python3

import pytest


#Author : Tomas
#Exercise 5 of the first automation track class homework



test_string = "Pass"

def get_string():
	return test_string

def set_string(test_str):
	global test_string
	test_string = test_str

save_str = ""

def setUp():
	global save_str
	save_str = get_string()
    
    
def tearDown():
	global save_str
	set_string(save_str)


def test_setstring():
	setUp()
	test_var = input("Write [Pass] or [Fail] to test the assertion: ")
	set_string(test_var)
	assert get_string() == "Pass"
	tearDown()

test_setstring()

