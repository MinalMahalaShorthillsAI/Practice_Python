class Solution(object):
    def getSneakyNumbers(self, nums):
        abc={}
        lst=[]
        for i in nums:
            if i in abc:
                abc[i]+=1
                lst.append(i)
            else:
                abc[i]=1
        return lst