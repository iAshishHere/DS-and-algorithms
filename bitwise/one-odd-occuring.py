def one_odd_occurance(elements):
    res=0
    for element in elements:
        res=res ^ element

    return res

res = one_odd_occurance([1,1,7,3,2,2,2,3,7])
print(res)
