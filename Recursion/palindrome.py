def palindrome(word,start,end):
    if (word[start]!=word[end]):
        return False
    else:
        palindrome(word[start + 1: end - 1], start + 1, end - 1)


    if end-start==0:
        return True





res = palindrome("abbaa",0,4)
print(res)