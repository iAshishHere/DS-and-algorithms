def palindrome(word,start,end):
    if start >= end:
        return True
    else:
        return (word[start] == word[end]) & (palindrome(word, start + 1, end - 1))

res = palindrome("abba",0,3)
print(res)