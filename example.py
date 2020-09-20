from Q15 import Q15no

a = Q15no(hex_val='0x4000')
b = Q15no(float_val= -0.5)
c = Q15no(bin_val='1110000000000000')


print("a = %f, b = %f, a + b = %f" % (a.value, b.value,(a+b).value))
print("a = %f, c = %f, a - c = %f" % (a.value, c.value,(a-c).value))
print("a = %f, b = %f, a * b = %f" % (a.value, b.value,(a+b).value))

print("a = %f, b = %f, c = %f" % (a.value, b.value,c.value))
if c == a * b:
    print("In here")