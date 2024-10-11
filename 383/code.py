class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        lst=[]
        for i in range(0, len(magazine)):
            lst.append(magazine[i])
        for i in range(0,len(ransomNote)):
            if ransomNote[i] in lst:
                lst.remove(ransomNote[i])
            else:
                return False
        return True
        