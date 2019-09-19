#!/usr/bin/python
# -*- coding: utf-8 -*-

class A(object):
    def add(self,x):
        y = x + 1
        print(y)
class B(A):
    def add(self,x):
        super(B,self).add(x)


b = B()
b.add(2)
print(b)
