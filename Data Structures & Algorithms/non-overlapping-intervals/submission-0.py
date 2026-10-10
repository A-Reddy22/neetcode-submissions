class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we need to basically chose the end value that ends the shortest
        #so as we do not have to pop from the array instead what we do is we keep track of the end times using a variable
        #first we sort
        ans=0
        intervals.sort()
        trackend=intervals[0][1]

        for start,end in intervals[1:]:
            if start>= trackend:
                trackend=end
            else:
                ans+=1
                #here start is less than the end time of the previous so we remove the interval with the smallest end time we do that by essentially making the comparator the minimuimum end time of both 

                trackend=min(end,trackend)
        return ans