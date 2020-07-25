def countSetBit(n):
    res = 0
    while(n):
        if(1&n):
            res = res + 1
        n = n >> 1

    return res

res = countSetBit(9000000)
print(res)