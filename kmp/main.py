

def makeprefix(pattern,prefix,n):
    len =0
    i=1
    prefix[0]=0
    while i<n:
        if pattern[len]==pattern[i]:
            len+=1
            prefix[i]=len
            i += 1
        else:
            if len>0:
                len =prefix[len-1]
            else:#len
                prefix[i]=0
                i+=1
    return prefix

def kmp(src,dest):
    destlen=len(dest)
    dessrc=len(src)
    if  dessrc>destlen:
        print("dessrc>destlen:")
        return -1
    print(dessrc)
    prefix1 = [None] * dessrc
    prefix2 = makeprefix(src, prefix1, dessrc)
    prefix2=move_prefix(prefix2,dessrc)
    print(prefix2)
    i=0
    j=0
    while i<destlen:
        if destlen-i<dessrc:
            print("failed")
            #return -1
        if src[j] == dest[i]:
            i += 1
            j += 1
        else:
            j = prefix2[j]
            if j ==-1:
                i+=1
                j+=1
        if (j == dessrc - 1) and (src[j] == dest[i]):
            print(i-dessrc+1)
            j=prefix2[j]

def move_prefix(prefix,n):
    i=n-1
    tmp=[None] * n
    for index in range(i, 0, -1):
        #print(index)
        tmp[index]=prefix[index-1]
    #print(tmp)
    tmp[0]=-1
    return tmp

str1="abab"
dest1="abaaababsabab"
# len=len(str)
# print(len)
# #prefix[len]
# prefix =[None] * len
# prefix=makeprefix(str,prefix,len)
# print(prefix)

# len=len(str1)
# prefix1 =[None] * len
# prefix1=makeprefix(str1,prefix1,len)
# print(prefix1)
# aa=move_prefix(prefix1,len)
# print(aa)
ans=kmp(str1,dest1)
#print(ans)