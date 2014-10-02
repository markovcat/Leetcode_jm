class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total = 0
        net = [0] * len(gas)
        for i in range(len(gas)):
            net[i] = gas[i] - cost[i]
            total += net[i]
        if total < 0:
            return -1
        
        start = 0
        current = 0
        local_total = 0
        while current < len(gas):
            local_total += net[current]
            if local_total >= 0:
                current += 1
            else:
                start = current
                current = start
                local_total = 0
            
        return start

print(Solution().canCompleteCircuit([1,2], [2,1]))