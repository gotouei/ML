def shortestPalindrome(s: str) -> str:
    i = 0
    n = len(s)
    right = ''
    for i in range(n):
        t = s[:n - i]#abcd ->abc
        #print(t)
        print(t[::-1])#inveres dcba ->cba
        if t == t[::-1]:
            break
        right += t[n - i - 1]
        #print(right)
    return right + s


class Solution(object):
    def shortestPalindrome(self, s):
        s_len=len(s)
        right=""
        #tmp2=[]
        for i in range(s_len):
            t=s[:s_len-i]
            #print(tmp)
            #print(tmp[::-1])
            if t==t[::-1]:
                break
            right+=t[s_len-i-1]
            #print(right)
        return right+s
'''
        1. Shrink from right to left to get the longest palindrome and the inverse of right part string
        2. add the right part in front of the original string

        e.g.
        step 1. aacecaaab                 right:''
        step 2. aacecaaab -> aacecaaa b   right:'b'
        step 3. aacecaaab -> aacecaa  ab  right:'ba'
        step 4. ab + aacecaaab = baaacecaaab
        
'''

aa=shortestPalindrome("sffsfeee")
print(aa)