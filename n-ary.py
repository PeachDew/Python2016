def reverse(array):
    rev = []
    for i in range(len(array)):
        rev.append(array[len(array) - 1 - i])
    return rev

print(reverse([9,8,7,6,5,4,3,2,1]))

def converttodecimal(num, base):
    num = str(num)
    arrnum = []
    for i in num:
        arrnum.append(int(i))
    arrnum = reverse(arrnum)
    number = 0
    for i in range(len(arrnum)):
        number += arrnum[i] * base ** i
    print(number)

def converttobase(dec, base):
    comb = []
    dec = dec
    while dec > 0:
        print(dec)
        comb.append(dec % base)
        dec //= base
    print(reverse(comb))
    comb = ''.join([str(x) for x in (reverse(comb))])
    return(comb)

converttodecimal(147, 8)
print(converttobase(103, 8))
