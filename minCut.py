class Solution:
    # def isPalindrome(self, s):
    #     if not s:
    #         return False
    #     if len(s) == 1:
    #         return True
        
    #     start, end = 0, len(s) - 1
    #     while s[start] == s[end] and start < end:
    #         start += 1
    #         end -= 1
    #     if start >= end:
    #         return True
    #     else:
    #         return False
            
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s:
            return None
        
        isPal = [[False for _ in range(len(s))] for _ in range(len(s))]
        for length in range(0, len(s)): # max length is len(s) - 1
            for i in range(0, len(s) - length): # max i is len(s) - length - 1
                j = i + length  # max j is len(s) - 1
                if length <= 2:
                    isPal[i][j] = s[i] == s[j]
                else:
                    isPal[i][j] = isPal[i + 1][j - 1] and s[i] == s[j]

        print(isPal)

        minCuts = [9223372036854775807] * (len(s))
        minCuts[0] = 0
        for i in range(1, len(s)): # max i is len(s) - 1
            if isPal[0][i]:
                minCuts[i] = 0
                continue
            
            for j in range(0, i): # max j is i
                if isPal[j + 1][i]: # s[j:i + 1] is Pal
                # if self.isPalindrome(s[j:i]):
                    minCuts[i] = min(minCuts[j] + 1, minCuts[i])
        
        return(minCuts[len(s) - 1])

s = "ab"
# print(Solution().isPalindrome(s))
print(s)
print(Solution().minCut(s))