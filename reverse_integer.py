class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            x = -x
            flag_neg = 1
        else:
            flag_neg = 0
        
        s = 0
        while x != 0:
            s = s * 10 + x % 10
            x = x // 10
            
        if flag_neg:
            return -s
        else:
            return s

def main():
    SolutionA = Solution()
    print SolutionA.reverse(123)

if __name__ == '__main__':
    main()