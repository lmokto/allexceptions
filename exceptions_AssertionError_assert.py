# -*- coding: utf-8 -*-

'''
En el pasado, Python ha apoyado a los mensajes de cadena simple como excepciones, as� como las clases. Desde 1.5, todos los m�dulos de biblioteca est�ndar utilizan clases de excepciones. A partir de Python 2.5, cadena excepciones resultan en un DeprecationWarning y soporte para cadena de excepciones se eliminar� en el futuro.

Se definen las clases de excepci�n en una jerarqu�a, que se describe en la documentaci�n de la biblioteca est�ndar. Adem�s de los obvios beneficios organizacionales, herencia de excepci�n es �til porque relacionados con excepciones pueden ser atrapadas por la captura de su clase base. En la mayor�a de los casos, estas clases base no pretenden ser levantado directamente.

BaseException
Base class for all exceptions. Implements logic for creating a string representation of the exception using str() from the arguments passed to the constructor.

Exception
Clase base para las excepciones que no resultan en dejar la aplicaci�n en ejecuci�n. Todas las excepciones definidas por el usuario deben utilizar excepci�n como clase base.

StandardError
Base class for built-in exceptions used in the standard library.exceptions

ArithmeticError
Base class for math-related errors.

LookupError
Base class for errors raised when something can�t be found.

EnvironmentError
Base class for errors that come from outside of Python (the operating system, filesystem, etc.).

'''

EXCEPTIONS = ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'EnvironmentError', 'Exception', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__doc__', '__name__', '__package__']


assert False, ''' The assertion failed '''


'''
Traceback (most recent call last):
  File "/Users/joseuranga/Desktop/exceptions/exceptions_AssertionError_assert.py", line 31, in <module>
    assert False, """ The assertion failed """
AssertionError:  The assertion failed
'''