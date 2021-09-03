day=5
hours=5
sub=['s1','s2','s3','s4','s5']
#s=set(sub)
r=0
print('   ',' ',' ','H1','H2','H3','H4','H5')
for i in range(day):
    print('Day',i+1,':',end=' ')
    for j in range(i,day):
        print(sub[j],end=' ')
        r=j
    for k in range(0,day-hours):
        print(sub[k],end=' ')
    hours-=1
    print()