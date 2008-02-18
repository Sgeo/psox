import sys

def send(text):
    sys.stdout.write(text)
    sys.stdout.flush()
    
def receive(num):
    return sys.stdin.read(num)
    
    
#PSOX-Init
send("\x00\x07\x01\n\x00\x00\n")
receive(3) #Discard PSOX-Init bytes

while True:
    send("\x00\x01\x01\n")
    received = receive(3)
    #Format is EOF indicator, number of bytes received not EOF, and the byte, or \x00 if EOF
    #EOF indicator is \x00 if there was an EOF, \x01 otherwise
    if(received[0]=="\x00"):
        send("\x00\x02\x01\x00\n") #Done
        break
    send("\x00\x00" + received[2]) #\x00\x00 escapes the next char, so NULs are repeated correctly
    
