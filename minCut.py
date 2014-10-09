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
        minCuts = [9223372036854775807] * (len(s))
        minCuts[-1] = 0

        for i in reversed(range(0, len(s))):
            for j in range(i, len(s) - 1):
                if j - i <= 2:
                    isPal[i][j] = s[i] == s[j]
                else:
                    isPal[i][j] = s[i] == s[j] and isPal[i + 1][j - 1]

                minCuts[i] = min(minCuts[i], minCuts[j + 1] + 1)

        return minCuts[0]


        # for length in range(0, len(s)): 
        #     for i in range(0, len(s) - length): 
        #         j = i + length  
        #         if length <= 2:
        #             isPal[i][j] = s[i] == s[j]
        #         else:
        #             isPal[i][j] = isPal[i + 1][j - 1] and s[i] == s[j]
        # print(isPal)

        # for i in range(1, len(s)): 
        #     if isPal[0][i]:
        #         minCuts[i] = 0
        #         continue
            
        #     for j in range(0, i): 
        #         if isPal[j + 1][i]: 
        #             minCuts[i] = min(minCuts[j] + 1, minCuts[i])
        
        # return(minCuts[len(s) - 1])

s = "aba"
print(s)
print(Solution().minCut(s))