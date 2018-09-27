#!/bin/sh

from hashlib import md5
from timeit import default_timer
a = default_timer()
b = raw_input("Entrer le hash md5:").strip()
for c in open(raw_input("Choissez le dictionnaire: "), "r"):
    d =  md5()
    d.update(str(c.strip()))
    if b in d.hexdigest():
        print "Hash crack: %s\n Complété %s seconds." %(c, int(default_timer()-a)); exit()
print "Terminé en %s seconds.\n[ ! ] Hash non cracké !" %(int(default_timer()-a)); exit()
