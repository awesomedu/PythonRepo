#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise  ValueError('bad score')


tangdu = Student('tangdu',20)
# 私有变量通过get set 方法取值、赋值
print('tangdu.get_name() = ',tangdu.get_name())
tangdu.set_score(60)
print('tangdu.get_score() = ',tangdu.get_score())
# 通过. 获取name , 带__的变量外部不能访问
print('property get name' % tangdu.name)





