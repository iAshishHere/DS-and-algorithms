
def josephus_probem(n,k):
    if n==1:
        return 0;
    return (josephus_probem(n-1,k)+k) % n


res = josephus_probem(2,3)
print(res)