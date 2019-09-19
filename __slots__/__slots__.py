#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass

s = Student() #实例
s.name = 'tangdu'
s.age = 18
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:',e)

g = GraduateStudent()
g.score = 88
