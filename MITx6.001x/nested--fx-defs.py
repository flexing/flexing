# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:14:54 2017
"""
#def f(x, y):
#   '''
#   x: int or float.
#   y: int or float
#   '''
#   x + y - 2  

#def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z
#
#def b(q, r):
#    return a(q>r, q, r)

#x = 12
#def g(x):
#      x = x + 1
#      def h(y):
#          return x + y
#      return h(6)
#g(x)
# 


#def foo(x, y = 5):
#   def bar(x):
#      return x + 1
#   return bar(y * 2)
#          
#foo(3)
# 

#def foo(x, y = 5):
#   def bar(x):
#      return x + 1
#   return bar(y * 2)
#          
#foo(3, 0)


#def foo (x):
#   def bar (z, x = 0):
#      return z + x
#   return bar(3, x)
#
#foo(2)

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
 
 