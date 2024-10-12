class Solution(object):
    def maximumWealth(self, accounts):
        max_count=0
        i=0
        j=0
        for i in range(len(accounts)):
            count=0
            for j in range(len(accounts[0])):
                count+=accounts[i][j]
            if count>max_count:
                max_count=count
        return max_count
