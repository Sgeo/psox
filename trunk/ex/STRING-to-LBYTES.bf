[
This program demonstrates how to take a STRING from a function and send it as the argument to another function. This will read the string returned by function 0x02 0x04 and send it to the hypothetical function 0x03 0x00. Note that this program is not valid PSOX, as PSOX-Init has been omitted, and also the domain 0x03 was not bound to. Also note how we can delay retrieving each caracter returned by 0x02 0x04 until we are ready to send it to 0x03 0x00.
]

.++.++.++++++. Sending 0x00 0x02 0x04 0x0A; Note that we do NOT need to retrieve the result yet;


>.+++.<. Sending 0x00 0x03 0x0A; Note that we didn't retrieve the result from 0x02 0x04 yet

>>

+>,[<.>.,]. 
