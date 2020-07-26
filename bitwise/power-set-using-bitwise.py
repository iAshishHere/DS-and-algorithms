def powerSet(words):
    word_length = len(words)
    total_power_set = pow(2,word_length)

    for x in range(total_power_set):
        for word in range(word_length):
            if(x & (1<<word)!=0):
                print(words[word], end= ""),
        print("")

    pass

powerSet("abc")