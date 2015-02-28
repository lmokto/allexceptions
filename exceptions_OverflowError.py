# -*- coding: utf-8 -*-

'''
Cuando una operación aritmética supera los límites del tipo variable, un OverflowError es aumento. Enteros largos asignan más espacio a medida que crecen los valores, así terminan criando MemoryError. Manejo de excepciones de punto flotante no está estandarizado, así que no se comprueban los flotadores. Regulares enteros se convierten en valores largos según sea necesario.

'''

#OverflowError

import sys

import sys

print 'Regular integer: (maxint=%s)' % sys.maxint
try:
    i = sys.maxint * 3
    print 'No overflow for ', type(i), 'i =', i
except OverflowError, err:
    print 'Overflowed at ', i, err

print
print 'Long integer:'
for i in range(0, 100, 10):
    print '%2d' % i, 2L ** i

print
print 'Floating point values:'
try:
    f = 2.0**i
    for i in range(100):
        print i, f
        f = f ** 2
except OverflowError, err:
    print 'Overflowed after ', f, err

'''
Regular integer: (maxint=9223372036854775807)
No overflow for  <type 'long'> i = 27670116110564327421

Long integer:
 0 1
10 1024
20 1048576
30 1073741824
40 1099511627776
50 1125899906842624
60 1152921504606846976
70 1180591620717411303424
80 1208925819614629174706176
90 1237940039285380274899124224

Floating point values:
0 1.23794003929e+27
1 1.53249554087e+54
2 2.34854258277e+108
3 5.5156522631e+216
Overflowed after  5.5156522631e+216 (34, 'Result too large')
'''