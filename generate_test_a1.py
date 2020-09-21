from Q15 import Q15no
from random import random
from math import e

def q11mpy_test_cases():
    for i in range(16):
        a = Q15no(float_val=random())
        b = Q15no(float_val=random())
        a = Q15no(bin_val=a.bin[:12]+'0000')
        b = Q15no(bin_val=b.bin[:12]+'0000')
        c = a * b
        c = Q15no(bin_val=c.bin[:12]+'0000')
        print(str(a.hex) + " " + str(a.value))
        print(str(b.hex) + " " + str(b.value))
        print(str(c.hex) + " " + str(c.value))
        print('')

def q15exp_test_cases():

    fac = [
        Q15no(hex_val='0x4000'),
	    Q15no(hex_val='0x1555'),
	    Q15no(hex_val='0x0555'),
	    Q15no(hex_val='0x0111'),
	    Q15no(hex_val='0x002d'),
	    Q15no(hex_val='0x0006'),
	    Q15no(hex_val='0x0000'),
	    Q15no(hex_val='0x0000'),
	    Q15no(hex_val='0x0000'),
    ]

    for i in range(16):
        a = Q15no(float_val=(random()*2 -1))
        t = Q15no(hex_val=a.hex)
        s = Q15no(hex_val='7fff')
        s = s + a
        for i in range(8):
            t *= a
            s += t * fac[i]
        print(a.hex, a.value)
        c = Q15no(float_val=(e**a.value)%1)
        print(c.hex, c.value, e**a.value)
        if a.value > 0:
            if a < Q15no(hex_val='0x58b8'):
                s = s + Q15no(hex_val='7fff')
        print(s.hex, s.value)
        print('')

def q15inv_test_cases():
    for i in range(16):
        a = Q15no(float_val=-1*random())
        print(str(a.hex) + " " + str(a.value))
        b = 1/(1-a.value)
        print(b)
        t = Q15no(hex_val=a.hex)
        s = Q15no(hex_val='7fff')
        for i in range(9):
            s += t
            t *= a
        print(str(s.hex) + " " + str(s.value))
        print('')

if __name__ == '__main__':
    q15inv_test_cases()