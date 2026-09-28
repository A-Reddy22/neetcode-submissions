class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #i am going to loop through each row, basically check if the first index is less than the target or greater than the target if it is we continue

        for i in range(len(matrix)):

            if matrix[i][0]> target or matrix[i][-1]< target:
                continue

            l=0
            r=len(matrix[0])-1
            while l<=r:
                mid=(l+r)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]> target:
                    r=mid-1
                elif matrix [i][mid]<target:
                    l=mid+1
        return False