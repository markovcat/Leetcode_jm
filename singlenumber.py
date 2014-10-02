## LeetCode OJ Single Number

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	result = A[0];
    	for num in A[1:]:
    		result ^= num
    	return result

def main():
	test_list = [12, 1, 23, 23, 1]
	Solution_a = Solution()
	print Solution_a.singleNumber(A=test_list)


if __name__ == '__main__':
	main()