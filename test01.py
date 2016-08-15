#! /usr/bin/env python
# -*- coding:utf-8 -*-


def log(*text):
    def decorator(func):
        def wrapper(*args, **kw):
            print 'begin call %s %s():' % (text, func.__name__)
            func(*args, **kw)
            print 'end call %s %s():' % (text, func.__name__)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

print now()