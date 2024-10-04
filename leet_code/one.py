sub = ["arp", "live", "strong"]

string = ["lively", "alive", "harp", "sharp", "armstrong"]

g = []
for i in sub:
    for j in string:
        if i in j :
            g.append(i)
            break
           

print(g)