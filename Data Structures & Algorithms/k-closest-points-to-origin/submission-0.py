class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #find the distance for the points
        # then append it to a minheap
        # then heapify it
        # then we need to return k points os until k is 0 we just keep going
        minHeap=[]

        for x,y in points:
            distance=((x**2)+(y**2))
            minHeap.append([distance,x,y])
        heapq.heapify(minHeap)
        result=[]
        while k>0:
            ditance,x,y= heapq.heappop(minHeap)
            result.append([x,y])
            k-=1
        return result
        