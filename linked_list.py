class ListNode(object):
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution(object):
    def hasCycle(self, head):
        if head==None:
            return False
        else:
            fast=head
            slow=head

            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
                if fast==slow:
                    break

            if fast ==None or fast.next==None:
                return False
            elif fast==slow:
                return True

            return False      


e1=ListNode(10)
e2=ListNode(20)
e3=ListNode(30)

e1.next=e2
e2.next=e3
e3.next=e1

check_status=Solution.hasCycle(e1,e2)

print(check_status)    
