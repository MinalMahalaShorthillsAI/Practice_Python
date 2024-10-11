class Solution(object):
    def findTheDifference(self, s, t):
        n=len(s)
        lst=[]
        for i in range(0,n):
            lst.append(s[i])
            
        o=len(t)

        for i in range(0,o):
            if t[i] in lst:
                lst.remove(t[i])
            else:
                return t[i]
        
        