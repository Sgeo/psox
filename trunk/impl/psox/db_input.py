from domain import Domain, argtypes, rettypes
from psoxglobals import cur_infile

PSOX_VERSION = (0, 0, 0)
MY_VERSION = 1

class InputDomain(Domain):
    def __init__(self):
        pass
        
    def __getitem__(self, item):
        """We're pretending that this is the real function, for now"""
        num = ord(item)
        the_data = cur_infile.read(num)
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
        
        def f(self):
            return result
        f.regex = r""
        return f
        
the_domain = InputDomain
