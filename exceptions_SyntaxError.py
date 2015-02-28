# -*- coding: utf-8 -*-

'''
A SyntaxError occurs any time the parser finds source code it does not understand. This can be while importing a module, invoking exec, or calling eval(). Attributes of the exception can be used to find exactly what part of the input text caused the exception.
'''

try:
    print eval('five times three')
except SyntaxError, err:
    print 'Syntax error %s (%s-%s): %s' % \
        (err.filename, err.lineno, err.offset, err.text)
    print err

'''
Syntax error <string> (1-10): five times three
invalid syntax (<string>, line 1)
'''
