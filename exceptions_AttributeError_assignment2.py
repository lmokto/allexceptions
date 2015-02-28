# -*- coding: utf-8 -*-

#Or when trying to modify a read-only attribute:

class MyClass(object):
    @property
    def attribute(self):
        return 'This is the attribute value'

o = MyClass()
print o.attribute
o.attribute = 'New value'


'''
ttributeError_assignment2.py
This is the attribute value
Traceback (most recent call last):
  File "/Users/joseuranga/Desktop/exceptions/exceptions_AttributeError_assignment2.py", line 12, in <module>
    o.attribute = 'New value'
AttributeError: can't set attribute
'''