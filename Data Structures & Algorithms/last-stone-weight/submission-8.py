import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #make a max heap
        #grab the two heaviest stone subtrack them from each other and then append it to the end of the array
        #first make max heap

        for i in range(len(stones)):
            stones[i]=-stones[i]
        
        heapq.heapify(stones)
        value=0
        if len(stones)==1:
            return -(stones[0])

        
        while len(stones)>1:
            

            a=-(heapq.heappop(stones))
            b=-(heapq.heappop(stones))
            value=a-b
            if value>0:
                heapq.heappush(stones,(-value))
            if len(stones)==1:
                return -(stones[0])
        if len(stones)==0:
                return 0
        


        