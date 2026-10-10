class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #merging is basially done when the start of one inerval is before the ending of another
        #so what I will do is first sore the array and in the res what i will do is I will store the first start time then from there I shall move
        intervals.sort(key=lambda i:i[0])
        ans=[intervals[0]]

        for start,end in intervals[1:]:
            lastEnd=ans[-1][1]

            if start<=lastEnd:
                ans[-1][1]=max(end,lastEnd)
            else:
                ans.append([start,end])
        return ans
        