# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=1
        curr=head
        while curr and curr.next:
            curr=curr.next
            length+=1
        

        curr1=head
        x=length-n
        counter=0

        if head.next==None and n==1:
            return None
        if x==0:
            return head.next

        while curr1 and curr1.next:
            if counter+1==x and curr1.next.next:
                curr1.next=curr1.next.next
                break
            elif counter+1==x and not curr1.next.next:
                curr1.next=None
                break
            else:
                curr1=curr1.next
                counter+=1
        return head
            


        

        
        