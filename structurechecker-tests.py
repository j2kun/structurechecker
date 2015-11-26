from structurechecker import *
from unittest import test


import a
test([], checkHierarchy(a, ['f1', 'f2', 'f3',], depth="a"))
test(['a.f4'], checkHierarchy(a, ['f1', 'f2', 'f4',], depth="a"))

import b
test([], checkHierarchy(b, {'Dog':[], 'Cat':['meow']}, depth="b"))
test(['b.Llama'], checkHierarchy(b, {'Dog':[], 'Llama':['meow']}, depth="b"))
test(['b.Cat.woof'], checkHierarchy(b, {'Dog':[], 'Cat':['meow', 'woof']}, depth="b"))
test(['b.Dog.Head'], checkHierarchy(b, {'Dog':{'Head':[]}, 'Cat':['meow']}, depth="b"))
test(['b.bye'], checkHierarchy(b, {'Dog':[], 'Cat':['meow'], 'bye':[], 'hi':[]}, depth="b"))


test(['a.f4', 'b.Dog.woof', 'b.bye', 'c'], checkStructure([a,b], 
   {'a': ['f1', 'f2', 'f4'],
    'b': {'Dog':{'Tail':[], 'woof':[]}, 'Cat':['meow'], 'bye':[], 'hi':[]},
    'c':[]}))

