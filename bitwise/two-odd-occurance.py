def two_odd_occurance(elements):
    xor = res1 = res2 = 0
    for element in elements:
        xor = xor ^ element

    firstNum = xor & ~ (xor-1)  #to get set bit of the first occuring and rest as 0

    for element in elements:
        if(element&firstNum!=0):
            res1=res1^element
        else :
            res2=res2^element


    return (res1,res2)


res = two_odd_occurance([1,1,7,3,2,2,2,3,7,9,2,12,2,2])
print(res)