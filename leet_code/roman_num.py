letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


input_string = ['XXI', 'MCMXC' , 'MDCLXVI' , 'MMVIII' ,'IVXLCDM', 'MMXVIII']



for str in input_string:
    num = 0
    for i in range(len(str)):
        x = i+1
        if i+1 == len(str):
            x = i
        if letters[str[i]] >= letters[str[x]]:
            num += letters[str[i]]
            continue
        num -= letters[str[i]]  

    print(num)