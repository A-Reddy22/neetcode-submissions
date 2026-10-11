class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #so what we do here is basically we have to calculate the cost to get to that stair at every point
        #then from there we take the minimum for example [1,2,3]
        # cost to get to 1 is 0 and cost to get to 2 is 0 now to get to three the minimum is one, not to get to the level after that is is 2 becaue 2 gets you to the next step

        array=[0,0]
        n=len(cost)
        for i in range(2,n+1):
            x=min((array[i-2]+cost[i-2]),(array[i-1]+cost[i-1]))
            array.append(x)
        return array[-1]
        