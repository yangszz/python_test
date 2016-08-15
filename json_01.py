#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.score = score


def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])	

s = Student('yangs',24,88)
print(json.dumps(s, default=student2dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
