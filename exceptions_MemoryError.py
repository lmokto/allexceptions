# -*- coding: utf-8 -*-

import itertools

#Si tu programa se queda sin memoria y es posible recuperar (mediante la eliminaci?n de algunos objetos, por ejemplo), se provoca un MemoryError.

# Try to create a MemoryError by allocating a lot of memory
l = []
for i in range(3):
    try:
        for j in itertools.count(1):
            print i, j
            l.append('*' * (2**30))
    except MemoryError:
        print '(error, discarding existing list)'
        l = []

'''
$ python exceptions_MemoryError.py
python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
0 1
0 2
0 3
(error, discarding existing list)
1 1
1 2
1 3
(error, discarding existing list)
2 1
2 2
2 3
(error, discarding existing list)
'''