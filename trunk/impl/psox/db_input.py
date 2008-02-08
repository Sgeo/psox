from domain import Domain, argtypes, rettypes
from psoxtypes import FNUM
from psoxglobals import FDDICT, SEEINTERNAL

PSOX_VERSION = (0, 0, 0)
MY_VERSION = 1

class InputDomain(Domain):
    def __init__(self):
        pass
        
    def __getitem__(self, numchar):
        """We're pretending that this is the real function, for now"""

        @argtypes()
        def f(self):
            num = ord(numchar)
            if(SEEINTERNAL): print "num == " + repr(num)
            the_data = FDDICT[1].read(num)
            if(num):
                if(len(the_data)<num):
                    eof_status = "\x00" #There was an EOF
                    non_eof_chars = chr(len(the_data))
                    padding = "\x00" * (num - len(the_data))
                else:
                    eof_status = "\x01" #No EOF
                    non_eof_chars = chr(len(the_data))
                    padding = ""
                result = eof_status + non_eof_chars + the_data + padding
            else: #We're reading in a full line
                if(len(the_data)==0 or the_data[-1]!="\n"):
                    eof_status = "\x00" #EOF
                    the_data += "\n" #Complimentary newline
                else:
                    eof_status = "\x01"
                result = eof_status + the_data + "\x00"
            return result
        return f
        
the_domain = InputDomain
