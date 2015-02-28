# -*- coding: utf-8 -*-

'''
http://pymotw.com/2/exceptions/index.html

Un EOFError se produce cuando una funci�n incorporada como input() o input() crudo no lee ning�n dato antes de encontrar al final de la secuencia de entrada. Los m�todos de archivo como read() devuelven una cadena vac�a al final del archivo.

'''
while True:
    data = raw_input('prompt:')
    print 'READ:', data


'''
MacBook-Pro-de-jose:exceptions joseuranga$ python /Users/joseuranga/Desktop/exceptions/exceptions_EOFError.py
prompt:/abc/fg.txt
READ: /abc/fg.txt
prompt:Traceback (most recent call last):
  File "/Users/joseuranga/Desktop/exceptions/exceptions_EOFError.py", line 10, in <module>
    data = raw_input('prompt:')
EOFError
'''