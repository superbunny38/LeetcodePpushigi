# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head):
        
        #check size
        size = 0
        cur_node = head
        while cur_node:
            size += 1
            cur_node = cur_node.next
        
        #merge
        def merge(node1,node2):
            cur1,cur2 = node1,node2
            head = None
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    connect_node = cur1
                    cur1 = cur1.next
                else:
                    connect_node = cur2
                    cur2 = cur2.next
                if head == None:
                    head = connect_node
                    prev_connect_node = head
                else:
                    prev_connect_node.next = connect_node
                    prev_connect_node = connect_node
            while cur1:
                prev_connect_node.next = cur1
                prev_connect_node = cur1
                cur1 = cur1.next
            while cur2:
                prev_connect_node.next = cur2
                prev_connect_node = cur2
                cur2 = cur2.next
            return head

        #divide
        def divide(head, size):
            if head.next == None:
                return head
            left = int(size//2)
            left_node = head
            disconnect_node = head

            for _ in range(left-1):
                disconnect_node = disconnect_node.next
            right_node = disconnect_node.next
            disconnect_node.next = None

            left_s = divide(left_node,int(size//2))
            right_s = divide(right_node,size-int(size//2))
            
            return merge(left_s,right_s)
        
        print("head:",head.val)
        print("size:",size)
        return divide(head,size)

n4 = ListNode(val=4)
n5 = ListNode(val=5)
n2 = ListNode(val=2)
n1 = ListNode(val=1)
n3 = ListNode(val = 3)
n4.next = n1
n1.next = n2
n2.next = n5
n5.next = n3
#4->1->2->5->3

s = Solution()
sorted_head = s.sortList(n4)

while sorted_head:
    print(sorted_head.val)
    sorted_head = sorted_head.next