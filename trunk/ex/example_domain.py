#Note: This is an early example of what a domain might look like. Try not to take it too seriously

from psox.utils import n2ln, s2ls #num to longnum and string to longbytes
from psox.safety import unsafe
from psox.domain import Domain, argtypes, funcnum
from psox.types import STRING, LBYTES, LNUM, FNUM, VARG

class MyDomain(Domain):
    
    @funcnum(0x05) #[MANDATORY] This will make this function be bound to 0x05 in this domain
    @argtypes(LNUM, LNUM, FNUM(3)) #[MANDATORY] This specifies what arguments the function will take. Note that the FNUM(3) indicates fixed bytes acting as one number
    def add(self, num1, num2, num3):
        """Add two longnums, resulting in a longnum"""
        return n2ln(num1+num2) #The return must be a string..
    
    
    @funcnum(0x06)
    @unsafe #Note that this comes _directly_ after @funcnum
    @argtypes(FNUM(1), FNUM(1))
    def unsafe_add(self, num1, num2):
        return chr(num1+num2)
        
        
    @funcnum(0x07)
    @argtypes(VARG(LNUM)) #You can use VARG(sometype) only as the last type in argtypes. The caller, when it reaches that point, will specify the number of arguments it wishes to send. i.e. to add 5 longnums, this would be called with 0x05 0x07 0x05 ln1 ln2 ln3 ln4 ln5
    def varadd(self, nums*):
        return n2ln(sum(nums))
        

the_domain = MyDomain() #the_domain is MAGIC