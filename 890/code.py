class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def flatten(s):
            mapping = {}
            code = []
            next_code = 0
            
            for char in s:
                if char not in mapping:
                    mapping[char] = next_code
                    next_code += 1
                code.append(mapping[char])
            
            return code
        num=[]
        for i in words:
            if flatten(i)==flatten(pattern):
                num.append(i)
        return num
        
        