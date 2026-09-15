class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        p0=0
        p1=len(heights)-1
        max_area=0
        while p0<p1:
            area=(min(heights[p0],heights[p1]))*(p1-p0)
            max_area=max(max_area,area)
            if heights[p0]>heights[p1]:
                p1-=1
            elif heights[p0]<=heights[p1]:
                p0+=1
        return max_area
        