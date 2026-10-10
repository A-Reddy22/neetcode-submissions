"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #basically what I want to do is sort the start times and end times
        #start times say when meeting started and end is when meetings end
        #I will have a vounter of number of meeting started and every time we iterate start I increase 
        counter=0
        ans=[]
        starts=[]
        ends=[]
        ans=0
        for i in range (len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        l=0
        r=0
        while l<len(starts) and r<len(ends):
            if starts[l]<ends[r]:
                counter+=1
                ans=max(counter,ans)
                l+=1
            elif ends[r]<=starts[l]:
                r+=1
                counter-=1
        return ans
