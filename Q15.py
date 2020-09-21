import re
from copy import deepcopy

TWO_POW_15 = 2 ** 15
TWO_POW_16 = 2 ** 16

class Q15no:

    def __init__(self, float_val= None, hex_val = None, bin_val = None):
        if (float_val != None or hex_val or bin_val):
            if(float_val != None):
                if(float_val >= 0):
                    self.hex_rep = self.format_hex(hex(int(float_val * TWO_POW_15 ))[2:])
                else:
                    self.hex_rep = hex(int(-1 * float_val * TWO_POW_15))[2:]
                    self.twos_compliment()
            elif(hex_val):
                self.hex_rep = self.format_hex(hex_val)
            else:
                if len(bin_val) > 16:
                    raise AttributeError("Binary number too big")
                self.hex_rep = self.format_hex(hex(int(bin_val, 2)))
        else:
            raise AttributeError("Please provide atleast one of the following\
                                    arguments (float_val, hex_val, bin_val)")

    def twos_compliment(self):
        num = int(self.hex_rep, 16)
        if num == 0:
            self.hex_rep = '0000'
        else:
            self.hex_rep = self.format_hex(hex(TWO_POW_16 - num))

    def format_hex(self, hex_val):
        regex = re.match('^(0x|0X)?([a-fA-F0-9]{1,4})$', hex_val)
        if regex == None:
            raise ArithmeticError("Wrong Format %s, correct format '0x1a21'\
                                    and should not exceed 4 characters (i.e. 16bits)" % hex_val)
        hex_no = regex.groups()[1]
        return (('0' if ord(hex_no[0]) <= ord('7') else 'f') *(4 - len(hex_no)) + hex_no).lower()

    @property
    def hex(self):
        return self.hex_rep

    @property
    def value(self):
        num = int(self.hex_rep, 16)
        if num >= TWO_POW_15:
            return -1 * float(TWO_POW_16 - num) / TWO_POW_15
        else:
            return float(num) / TWO_POW_15

    @property
    def int_val(self):
        return int(self.hex_rep, 16)

    @property
    def bin(self):
        return "{:016b}".format(self.int_val)

    def is_negative(self):
        return ord(self.hex_rep[0]) > ord('7')

    def __repr__(self):
        return "Q15 number- hex: 0x" + self.hex_rep + ", value: " + str(self.value)

    def __add__(self, b):
        return Q15no(hex_val= hex((self.int_val + b.int_val) % 2**16))

    def __sub__(self, b):
        return Q15no(hex_val= hex((self.int_val - b.int_val) % 2**16))

    def __gt__(self, b):
        return self.int_val > b.int_val

    def __lt__(self, b):
        return self.int_val < b.int_val

    def __mul__(self, b):
        flip = False
        a1, b1 = deepcopy(self), deepcopy(b)
        if self.is_negative():
            a1.twos_compliment()
            flip = not flip
        if b.is_negative():
            b1.twos_compliment()
            flip = not flip
        result = Q15no(hex_val= hex(((a1.int_val * b1.int_val) / TWO_POW_15) % TWO_POW_16))
        del a1, b1
        if flip:
            result.twos_compliment()
        return result

    def __eq__(self, b):
        return self.hex_rep == b.hex_rep