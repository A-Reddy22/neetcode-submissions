# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1=[]
        nums2=[]
        curr1=l1
        curr2=l2
        nums=[]
        while curr1:
            nums1.append(curr1.val)
            curr1=curr1.next
        while curr2:
            nums2.append(curr2.val)
            curr2=curr2.next
        nums1=nums1[::-1]
        nums2=nums2[::-1]
        s=""
        s1=""
        for i in range(len(nums1)):
            s+=str(nums1[i])
        for i in range(len(nums2)):
            s1+=str(nums2[i])
        s=int(s)
        s1=int(s1)
        ans=s+s1
        for digit in str(ans):
            nums.append(int(digit))
        nums=nums[::-1]
        head=ListNode(nums[0])
        curr=head
        for i in range(1,len(nums)):
            curr.next=ListNode(nums[i])
            curr=curr.next
        return head
        