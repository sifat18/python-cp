# review
import os, sys, io
import array
ar=array.array('i',[1,2,3,4])
a=sys.stdin.readline()
sys.stdout.write(a)
print(ar[2])

# linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linlis:
    def __init__(self):
        self.head=None
# creating a head
l=Linlis()
# setting value to head
l.head=Node(2)
# creating other datas but not connected
sec=Node(3)
thrid=Node(1)
# creating connection
l.head.next=sec
sec.next=thrid
# traversal
temp=l.head
while(temp):
    print(temp.data)
    temp=temp.next