#!/usr/bin/python
# -*- coding: utf-8 -*-

# 实例属性
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# s = Student('tangdu')
# s.score = 90
#
# print('tangdu score %s' % s.score)

# 类属性
# class Student(object):
#     name = 'tangdu'
#
# a = Student()
# print('实例属性 %s' % a.name)
# print('类属性 %s' % Student.name)

#类属性应用
class Student(object):
    count = 0

    def __init__(self,name):
        self.name =  name