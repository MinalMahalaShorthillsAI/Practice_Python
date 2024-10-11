class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0  # Initialize two pointers for s and t
    
    # Loop through the original string s
        while i < len(t) and j < len(s):
            # If the characters match, move the pointer for t
            if t[i] == s[j]:
                j += 1
            # Always move the pointer for s
            i += 1
    
    # If we've matched all characters of t, return True
        return j == len(s)
