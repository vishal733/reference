#!/usr/bin/python

# Contains information on error handling

# Multiple errors can be handled together as below
try:
    //something
except (RuntimeError, TypeError, NameError):
    pass


import sys
import exceptions

except (RuntimeError, TypeError, NameError) as ex:
                msg = sys.exc_info()
                if msg[0] == exceptions.TypeError:  # works
                    print "Type Error Custom"
                print  sys.exc_info()         # Ex: (<type 'exceptions.TypeError'>, TypeError("__init__() got an unexpected keyword argument 'expires_in'",), <traceback object at 0x7f1d0f109bd8>)
                print ex        # Ex: __init__() got an unexpected keyword argument 'expires_in'
                logging.warning("S3Upload::S3Connection failed. Error: "+ str(ex))
                

