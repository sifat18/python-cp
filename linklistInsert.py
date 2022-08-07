# creating data and next property
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# creating head property
class Linlisk:
    def __init__(self):
        self.head=None


l=Linlisk()
l.head=Node(2)
l2=Node(11)
l3=Node(23)
l.head.next=l2
l2.next=l3
# # traverse

# temp=l.head #at the end it will contain the last node 
# while(temp):
#     print(temp.data,end=" ")
#     temp=temp.next
# output 2,11,23

l4=Node(42)
#insert at first pos push method 
# l4.next=l.head
# l.head=l4
# insert at middle insert method 
# l4.next=l2.next
# l2.next=l4

# traverse
temp=l.head #at the end it will contain the last node 
while(temp):
    print(temp.data,end=" ")
    temp=temp.next
    # print(temp.data)
# output 42,2,11,23 for insert first 
# output 2,11,42,23 for insert first 
# output 2,11,23,42 for insert first 

# insert at last --> traverse first and find the last node in temp
#traverse by checking next node is available or not
temp2=l.head #at the end it will contain the last node 
while(temp2.next):
    print(temp2.data,end=" ")
    temp2=temp2.next
temp2.next=l4
temp3=l.head #at the end it will contain the last node 
print('insert at last')
while(temp3):
    print(temp3.data,end=" ")
    temp3=temp3.next