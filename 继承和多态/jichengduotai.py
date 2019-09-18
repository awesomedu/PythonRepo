#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running.......')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Dog is running')

a = Animal()
b = Dog()
c = Cat()

print('a is animal?',isinstance(a,Animal))
print('a is dog?',isinstance(a,Dog))
print('a is cat?',isinstance(a,Cat))


print('b is animal?',isinstance(b,Animal))
print('b is dog?',isinstance(b,Dog))
print('b is cat?',isinstance(b,Cat))




