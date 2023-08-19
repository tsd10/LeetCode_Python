class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def reverseList(self, head):

        if head==None:
            return None
        elif head!=None and head.next==None:
            return head
        
        else:
            temp=None
            next_node=None
            while head!=None:
                next_node=head.next
                head.next=temp
                temp=head
                head=next_node

            return temp


head=ListNode(None)
e1=ListNode(10)
head.next=e1
e2=ListNode(20)
e3=ListNode(30)

return_list=Solution.reverseList(e1,e3)

print(return_list.val)

print(e1.val)