#An UnboundLocalError is a type of NameError specific to local variable names.

def throws_global_name_error():
    print unknown_global_name

def throws_unbound_local():
    local_val = local_val + 1
    print local_val

try:
    throws_global_name_error()
except NameError, err:
    print 'Global name error:', err

try:
    throws_unbound_local()
except UnboundLocalError, err:
    print 'Local name error:', err


'''
Global name error: global name 'unknown_global_name' is not defined
Local name error: local variable 'local_val' referenced before assignment
'''