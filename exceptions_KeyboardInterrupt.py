#KeyboardInterrupt

try:
    print 'Press Return or Ctrl-C:',
    ignored = raw_input()
except Exception, err:
    print 'Caught exception:', err
except KeyboardInterrupt, err:
    print 'Caught KeyboardInterrupt'
else:
    print 'No exception'

#MacBook-Pro-de-jose:exceptions joseuranga$ python exceptions_KeyboardInterrupt.py Press Return or Ctrl-C: ^CCaught KeyboardInterrupt
