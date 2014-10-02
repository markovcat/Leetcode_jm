class Solution:
    def isPalindrome(self, s):
        if not s:
            return False
        if len(s) == 1:
            return True
        
        start, end = 0, len(s) - 1
        while s[start] == s[end] and start < end:
            start += 1
            end -= 1
        if start >= end:
            return True
        else:
            return False
            
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if s is None:
            return []

        # DP 
        results = [[] for _ in range(len(s) + 1)]
        results[0] = [[]]
        
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                # print(s[j:i + 1])
                if self.isPalindrome(s[j:i]):
                    if not results[j]:
                        results[i] = [[s[j:i]]]
                        continue
                    for result in results[j]:
                        results[i].append(result + [s[j:i]])

        return results[len(s)]


s = "aab"
print(Solution().isPalindrome(s))
print(Solution().partition(s))