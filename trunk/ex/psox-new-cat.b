.+++++++.>.<+++. 0x00 0x07 0x00 0x0A for PSOX-Init; Note that at this point; PSOX Server sends a response; we'll defer picking it up;
>..<. Send 0x00 0x00 0x0A for the min_minorver and my_minorver and mandatory newline
>,,, Absorb and discard response from majorver; response code from minorver; and server's minorver; note that the server did not send newlines
[-] Just making sure that this cell is cleared;
>+ Initialize a 0x01

[
>.<..<<.>,,, 0x00 0x01 0x01 0x0A; then discard EOF status and number of good bytes and retrieve input
>>..<<. 0x00 0x00 then the char from stdin; this code will not break on receiving a NUL
>] Put the pointer to a known 0x01 and put a nice bracket



+[] Infinite loop separator


Final code:
.+++++++.>.<+++.>..<.>,,,[-]>+[>.<..<<.>,,,>>..<<.>]
