class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]

        for start,end in intervals[1:]:
            node=ans[-1][1]

            if start<=node:
                ans[-1][1]=max(node,end)
            else:
                ans.append([start,end])
        return ans


        