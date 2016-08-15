#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
	"""docstring for Animal"""
	def run(self,type):
		self.__type = type
		print '%s is running...' % self.__type

class Dog(Animal):
	pass

class Cat(Animal):
	"""docstring for Cat"""
	pass
				
						
dog = Dog()
dog.run('dog')

cat = Cat()
cat.run('cat')

print isinstance(dog,Animal)