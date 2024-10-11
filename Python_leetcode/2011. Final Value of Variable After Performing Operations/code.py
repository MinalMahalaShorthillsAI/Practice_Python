class Solution(object):
    def finalValueAfterOperations(self, operations):
        count=0
        for i in operations:
            if '-' in i:
                count-=1
            else:
                count+=1
        return count