#!/usr/bin/env python3

import time

#Author : Tomas Ferreira
#Exercise 3 of the first automation track class

#Creates the class Pizza
class Pizza():

	def __init__(self, size, pizza_type, sauce_type):
		self.size = size
		self.pizza_type = pizza_type
		self.sauce_type = sauce_type
		self.bake_pizza()

	# Simulates the baking of the pizza - waits 2 seconds (just for flair)
	def bake_pizza(self):
		print("Baking...")
		time.sleep(2)
		print("Pizza ready ! Enjoy your {0}cm {1} with {2}".format(self.size, self.pizza_type, self.sauce_type))



pizza_1 = Pizza(50, "Quattro Formaggi", "Olive oil")
pizza_2 = Pizza(32, "Prosciutto", "Garlic sauce")
pizza_3 = Pizza(40, "Margheritta", "Tomato sauce")

