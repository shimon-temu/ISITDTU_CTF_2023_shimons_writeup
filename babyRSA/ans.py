from Crypto.Util.number import *
from math import gcd
from non_coprime_exponent import find_set_of_possible_plaintexts, find_set_of_possible_plaintexts_variant
import re

p1 = 401327687854144602104262478345650053155149834850813791388612732559616436344229998525081674131271
p2 = 500233813775302774885494989064149819654733094475237733501199023993441312997760959607567274704359
p3 = 969568679903672924738597736880903133415133378800072135853678043226600595571519034043189730269981
e1 = 398119
e2 = 283609
e3 = 272383

c = 104229015434394780017196823454597012062804737684103834919430099907512793339407667578022877402970

set1 = find_set_of_possible_plaintexts_variant(e3, p3, c, e2, p2)
set2 = []
for candidate in set1:
    set2 += find_set_of_possible_plaintexts_variant(e2, p2, candidate, e1, p1)

set3 = []
for candidate in set2:
    set3 += find_set_of_possible_plaintexts(e1, p1, candidate)

possible_plaintexts = list(map(long_to_bytes, set3))
for m in possible_plaintexts:
    match_obj = re.search(b"ISITDTU{.+}", m)
    if match_obj != None:
        print(match_obj[0])