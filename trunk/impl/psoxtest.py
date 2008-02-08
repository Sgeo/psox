from sys import stdin, stdout
stdout.write("\x00\x07\x01\n")
stdout.write("\x00\x00\n")
stdout.flush()
stdin.read(3)

while True:
    stdout.write("\x00\x01\x00\n")
    stdout.flush()
    stdin.read(1) #Junk
    stdout.write(stdin.readline())
    stdout.flush()
    stdin.read(1) #Drop complimentary \x00

while True:
    #stdout.write("Test\n")
    #stdout.flush()
    stdout.write("\x00\x01\x01\n")
    stdout.flush()
    stdin.read(2) #Drop junk
    somechar = stdin.read(1)
    stdout.write("\x00\x00" + somechar)
    stdout.flush()

