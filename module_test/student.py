#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Studen(object):
	"""docstring for Studen"""
	def __init__(self, name,score):
		super(Studen, self).__init__()
		self.name = name
		self.score = score

	def print_score(self):
		print '%s : %s' % (self.name,self.score)

yangs = Studen('yangs',100)
zhang = Studen('zhang',60)

yangs.print_score()
zhang.print_score()	