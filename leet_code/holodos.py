list_of = ['anton','sdfsfsfsfsdfsdfsdfsdf','aiiiniiitiiio','asfsdfsfndadtasdadoadadsn']
anton = ['a','n','t','o','n']
for index,string  in enumerate(list_of):
    count = 0
    slice_of = string
    for i in range(len(anton)):
        found = slice_of.find(anton[i])
        if found  !=-1:
            slice_of = slice_of[found +1:]
            count+=1
        else:break
    if count>= len(anton):
        print(index+1,end=' ')
  