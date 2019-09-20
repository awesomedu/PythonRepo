#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

d = dict(name='tangdu',age=20,score = 100)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)


