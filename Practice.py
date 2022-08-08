class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Listt:
    def __init__(self):
        self.head=None

l1=Listt()
l1.head=Node(2)
l2=Node(4)
l3=Node(5)
l1.head.next=l2
l2.next=l3
#traverse
# temp=l1.head
# while temp:
#     print(temp.data,end=" ")
#     temp=temp.next

#insertion at first postion
l4=Node(7)
# l4.next=l1.head
# l1.head=l4

# at last pos
# temp=l1.head
# while temp.next:
#     temp=temp.next
# temp.next=l4

# in middle
# temp=l1.head
# while temp.next.data != 4:
#     temp=temp.next
# l4.next=temp.next
# temp.next=l4

# delete at first post
# l4.next=l1.head.next
# l1.head=l4

# del at last pos 
# temp=l1.head
# while temp.next.next:
#     temp=temp.next
# temp.next=l4

# del at middle

temp=l1.head
while temp.next.data != 4:
    temp=temp.next
l4.next=temp.next.next
temp.next=l4

temp=l1.head
while temp:
    print(temp.data,end=" ")
    temp=temp.next