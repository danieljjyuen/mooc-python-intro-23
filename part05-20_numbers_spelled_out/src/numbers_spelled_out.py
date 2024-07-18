# Write your solution here
def dict_of_numbers():
    di = {}
    di[0] = "zero"
    di[1] = "one"
    di[2] = "two"
    di[3] = "three"
    di[4] = "four"
    di[5] = "five"
    di[6] = "six"
    di[7] = "seven"
    di[8] = "eight"
    di[9] = "nine"
    di[10] = "ten"
    di[11] = "eleven"
    di[12] = "twelve"
    di[13] = "thirteen"
    di[14] = "fourteen"
    di[15] = "fifteen"
    di[16] = "sixteen"
    di[17] = "seventeen"
    di[18] = "eighteen"
    di[19] = "nineteen"
    di[20] = "twenty"
    di[30] = "thirty"
    di[40] = "forty"
    di[50] = "fifty"
    di[60] = "sixty"
    di[70] = "seventy"
    di[80] = "eighty"
    di[90] = "ninety"
    for i in range(21, 100):
        if i%10==0:
            continue
        else:
            remainder = i%10
            di[i] = f"{di[i-remainder]}-{di[remainder]}"
    return di