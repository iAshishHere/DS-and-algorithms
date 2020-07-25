
#solution 1
#Time complexity = theta(total Bits in n)
def countSetBit(n):
    res = 0
    while(n):
        if(1&n):
            res = res + 1
        n = n >> 1

    return res

res = countSetBit(9000000)
print(res)

#solution 2 (Brian and Kerningham Algorithm)
#when we substract 1 from the bit, all the bit which has 0 with the last set bit becomes 1.
def countSetBit(n):
    res = 0
    while(n):
        n &= (n - 1)
        res = res + 1
    return res

res = countSetBit(9000000)
print(res)