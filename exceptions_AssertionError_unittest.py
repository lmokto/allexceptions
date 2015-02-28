import unittest

class AssertionExample(unittest.TestCase):
    def test(self):
        self.failUnless(False)

unittest.main()


'''
F
======================================================================
FAIL: test (__main__.AssertionExample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/joseuranga/Desktop/exceptions/exceptions_AssertionError_unittest.py", line 5, in test
    self.failUnless(False)
AssertionError: False is not True

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
'''