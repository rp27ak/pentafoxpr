def ex(s):
    c=0
    st=''
    for i in range(len(s)):
        if c==0:
            st=st+s[i]
        if i<=len(s)-2 and s[i]==s[i+1]:
            c=c+1
        if i<=len(s)-2 and not c==0 and not s[i]==s[i+1]:
            st=st+str(c+1)
            c=0
    if c>0:
        st=st+str(c+1)
    return st

s=input()
s1=s.split()
for i in s1:
    print(ex(i),end=' ')