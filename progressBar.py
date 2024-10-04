def progress_bar(now,total):
    percent = 100*((now+1)/float(total))
    int_percent = int(percent)
    bar = '█' * int_percent + '-' * (100-int_percent)
    print(f'\r|{bar}| {percent:.2f}%',end='\r')
    if int_percent == 100:
        print(f'\r|{bar}| {percent:.2f}% DONE')


