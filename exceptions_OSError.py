# OSError

import os

for i in range(10):
    print i, os.ttyname(i)
    
'''
0 /dev/ttys000
1
Traceback (most recent call last):
  File "exceptions_OSError.py", line 15, in <module>
    print i, os.ttyname(i)
OSError: [Errno 25] Inappropriate ioctl for device
'''
