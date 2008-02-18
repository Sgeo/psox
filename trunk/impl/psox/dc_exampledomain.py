#Note: This is an early example of what a domain might look like. Try not to take it too seriously


from domain import Domain, argtypes, rettypes
from psoxtypes import STRING, LBYTES, LNUM, FNUM, VARG
from psoxglobals import SAFETYLIST

PSOX_VERSION = (0, 0, 0) #First number specifies major version, next two specify minimum minor version, and current minor version

class MyDomain(Domain):
    @argtypes(LNUM, LNUM, FNUM(3)) #[MANDATORY] This specifies what arguments the function will take. Note that the FNUM(3) indicates fixed bytes acting as one number
    @rettypes(LNUM) #[OPTIONAL] Converts the returned Python values into something accepted by PSOX
    def f05(self, num1, num2, num3): #Note that the name of the function specifies the function number. Hex digits are capitalized
        """Add two longnums, resulting in a longnum"""
        return num1+num2 #The return must be a string, but @rettypes takes care of that for us
    
    if("no06" not in SAFETYLIST): #How to check for safety stuff
        @argtypes(FNUM(1), FNUM(1))
        def f06(self, num1, num2):
            return chr(num1+num2) #Not bothering to use @rettypes here, returning a sheer string
        
        
    @argtypes(VARG(LNUM)) #This will cause a tuple to be passed in
    @rettypes(LNUM)
    def f07(self, nums):
        return sum(nums)
        

the_domain = MyDomain #the_domain is MAGIC. Note that we do not create an instance..
