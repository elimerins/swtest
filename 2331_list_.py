v,c = map(int,input().split())
a = [v]
while 1:
    v=sum([int(i)**c for i in str(v)])
    if v in a:
        print(a.index(v))
        break
    else:
        a.append(v)
