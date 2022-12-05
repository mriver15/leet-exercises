# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Michael Rivera

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Cycle through linked list building a new list that can be ranged
def getMiddleOfLinkedList(head):
    t = []
    c = head
    while(c):
        t.append(c.val)
        c = c.next

# Get middle of the List
    m = int(len(t) / 2)
    print(m)
    
    if not len(t) % 2:
        m = int((len(t) + 1) / 2)

# cycle through second half 
    mt = t[m:]
    
    nh = {}
    nhc = {}

    for i,v in enumerate(mt):
        nhc = nh
        if i == 0:
            nh = ListNode(v,next=None)
        else:
            nhc.next = ListNode(v,next=None)
    return nh
            

def main():
    c = ListNode(1,next=None)
    r = c
    for i in range(2,10,1):
        r.next = ListNode(i,next=None)

    m = getMiddleOfLinkedList(c)
    mc = m
    while(mc):
        print(mc.val)
        mc = mc.next
    

if __name__ == "__main__":
    main()