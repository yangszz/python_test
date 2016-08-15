#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	print foo('0')

if __name__ == '__main__':
	main()