class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
            
        start = 0
        end = len(s) - 1
        
        while start < end:
            while start < len(s) - 1 and not (s[start].isalpha() or s[start].isdigit()):
                start += 1
            while end > 0 and not (s[end].isalpha() or s[end].isdigit()):
                end -= 1
            
            if start >= end:
                return True
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True