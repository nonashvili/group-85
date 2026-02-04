def int_sum():
    user_sen=input("enter sentance:")
    sum=0
    for i in user_sen:
        if i>="0" and i<="9":
            sum+=int(i)

    print(sum)

int_sum()