.+++++++.>+.<+++.>-..<.,,,[-] PSOX_Init

.+.-.++++++++++. 0x00 0x01 0x00 0x0A

>.<--.>. 0x00 0x08 0x00

Let's discard the EOF indicator

,

then let's feed in the rest of the URL   in feeding it in a 0x0A will be fed in due to complimentary newline

+[,.]

Now a new infile FD was made at 0x04 let's switch to it

++.>[-]+++++++++++++++++.<++.>-------. 0x02 0x10 0x04 0x0A (0x00 comes from above line)

>[-]+[[-].+..+++++++++.,,,.] Simple CAT

++.-.-.++++++++++. 0x02 0x01 0x00 (0x00 comes from above line)

