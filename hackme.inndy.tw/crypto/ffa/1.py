from z3 import *

p = Int('p')
q = Int('q')

s = Solver()
s.add(And(1<=p,p<=9), And(1<=q,q<=19), And(5<(3*p-4*q),(3*p-4*q)<10))
s.check() 
print s.model()
