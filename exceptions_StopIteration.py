l=[0,1,2]
i=iter(l)

print i
print i.next()
print i.next()
print i.next()
print i.next()

'''
$ python exceptions_StopIteration.py

<listiterator object at 0x10045f650>
0
1
2
Traceback (most recent call last):
  File "exceptions_StopIteration.py", line 19, in <module>
    print i.next()
StopIteratiop
'''
