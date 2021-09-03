li=[]
for i in range(65,91):
    li.append(chr(i))
l=[int(i) for i in input().split(',1,')]
for i in l:
    print(li[i-1],end='')
