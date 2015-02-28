# -*- coding: utf-8 -*-

'''
Cuando falla una referencia del atributo o asignaci—n, AttributeError se levanta. Por ejemplo, cuando se trata de hacer referencia a un atributo que no existe:
'''

class NoAttributes(object):
    pass

o = NoAttributes()
print o.attribute


'''
Traceback (most recent call last):
  File "/Users/joseuranga/Desktop/exceptions/exceptions_AttributeError_assignment.py", line 11, in <module>
    print o.attribute
AttributeError: 'NoAttributes' object has no attribute 'attribute'
'''