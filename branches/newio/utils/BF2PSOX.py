#Note that this makes the assumption that EOF=0


replace_list = [
(">", ">>"),
("<", "<<"), 
(".", ">..<."),
(",", "[-].+..+++++++++.,,,"),
]

psox_init = ".+++++++.[-]+.+++++++++.[-]..++++++++++.,,,[-]"

from sys import stdin, stdout, exit

the_text = stdin.read()

for (i, j) in replace_list:
    the_text = the_text.replace(i, j)
    
the_text = psox_init + the_text

stdout.write(the_text)
stdout.flush()
stdout.close()
exit(0)
