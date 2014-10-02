class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        print(candies)
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(ratings[i + 1] + 1, candies[i])

        print(candies)
        return sum(candies)

ratings = [2, 3, 2]

print(Solution().candy(ratings))
