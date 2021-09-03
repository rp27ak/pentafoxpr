s=input()
st=input()
fi=''
f=''
if len(s)==len(st):
    for i in range(len(s)):
        if not s[i]==st[i]:
            fi=fi+s[i]
            f=f+st[i]
fi=fi+f
print(fi)