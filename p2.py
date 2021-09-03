def ex(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if j>i:
                if li[j]+li[i]==8:
                        s=str(li[i])+','+str(li[j])
                        return s
    return 'No Pairs found'

li=[int(i) for i in input().split()]
print(ex(li))

