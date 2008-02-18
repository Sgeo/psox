from sys import stdin, stdout

def send(text):
    stdout.write(text)
    stdout.flush()
    
def receive(num):
    return stdin.read(num)
    

#PSOX-Init
send("\x00\x07\x01\n")
send("\x00\x00\n")
receive(3)

#Map the domain
send("\x00\x02\x03") #0x00 0x02 0x03 (map custom domain)
send("\x03") #0x03 (the domain number we want to use for this domain
send("exdom") #The PRI, remember that STRINGNLs don't need NULs at the end
send("\n") #Mandatory 0x0A after every function call
receive(1) #Throw away the returned version number

#Use the function 0x06
send("\x00\x03\x06")
send("a\x01")
send("\n")
print receive(1)

#Use the function 0x05
send("\x00\x03\x05")
send("\x01\xFF\x01a\x00")#First longnum
send("\x02\xFF\x01\x00\x00") #Second longnum
send("\x01\x02\x03") #FNUM(3)
send("\n") #Mandatory \n
print receive(3)[1] #Resulting longnum should be 3 bytes, print 2nd


#Use the function 0x07
send("\x00\x03\x07")
send("\x01\x01\x0A\x00\x01\x01\x0A\x00\x01\x01\x0A\x00\x01\x01\x0A\x00\x01\x01\x0A\x00\x01\x01\x0A\x00\x01\x01\x05\x00\x00") #VARG(LNUM) representing (10,10,10,10,10,10,5)
send("\n")
print receive(3)[1]

#Exit with code 0
send("\x00\x02\x01\x00\x0A")
