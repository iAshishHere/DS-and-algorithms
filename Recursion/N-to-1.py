
#print number from 1 to N

def one_to_N(number):
    if(number==0):
        return
    else:
        one_to_N(number-1)
        print(number)



one_to_N(5)

#print number from N to 1

def N_to_One(number):
    if (number == 0):
        return
    else:
        print(number)
        N_to_One(number - 1)

N_to_One(5)