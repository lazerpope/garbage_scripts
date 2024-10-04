import string


phone_number = '3662277'
words = ['foo','bar','baz','foobar','emo','cap','car','cat']
# words = ['foo','bar','foobar','emo','cap','car']
words_numbers = []
translation = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o':6,'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

for i,word in enumerate(words):   
    sting = ''
    for symbol in word:
        sting+=str(translation[symbol])
    if phone_number.find(sting)!=-1:
        print(words[i], end=' ')
            
    