def rope_of_length(n,a,b,c):
    if n < 0:
        return -1
    if n == 0:
        return 0
    res = max(rope_of_length(n-a,a,b,c), rope_of_length(n-b,a,b,c), rope_of_length(n-c,a,b,c))
    if(res==-1):
        return -1
    return res+1


#Test cases

res = rope_of_length(5,2,5,1)
print("------------")
print(res)
print("------------")


res = rope_of_length(6,2,5,1)
print("------------")
print(res)
print("------------")


res = rope_of_length(23,12,9,11)
print("------------")
print(res)
print("------------")

res = rope_of_length(5,4,2,6)
print("------------")
print(res)
print("------------")