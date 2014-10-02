class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        possible = [False for _ in range(len(s) + 1)]
        possible[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if possible[j] == True and s[j:i] in dict:
                    possible[i] = True
                    break
        
        if not possible[len(s)]:
            return []
        
        solutions = [[] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if possible[j] == True and s[j:i] in dict:
                    # if empty
                    if not solutions[j]:
                        solutions[i].append(s[j:i])
                    else:
                        for solution in solutions[j]:
                            solutions[i].append(solution + " " + s[j:i])
        
        return solutions[len(s)]