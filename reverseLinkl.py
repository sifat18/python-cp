class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class list:
    def __init__(self):
        self.head=None
l1=list()
l1.head=Node(21)
l2=Node(11)
l3=Node(215)
l1.head.next=l2
l2.next=l3

# temp=l1.head
# while temp:
#     print(temp.data,end=" ")
#     temp=temp.next

# reverse print
temp=l1.head
prev=None
nex=None
while temp:
    nex=temp.next
    temp.next=prev
    prev=temp
    temp=nex
    # print(temp.data,end=" ")
l1.head=prev

temp=l1.head
while temp:
    print(temp.data,end=" ")
    temp=temp.next
