import array,sys
# sys.stdout.write('pl')
ar=array.array('i',[1,2,3])
# sys.stdout.write(map('str',ar[2]))
print(ar[1])

ar.append(4)
print(ar)
ar.insert(2,6) #at ith position
print(ar)
ar.pop(2) # at that index pop
print(ar)
ar.remove(1)  # REMOVE the first time that number appears
print(ar)
# print ("The occurrences of #2 in array is : ")
print(ar.count(2))  
ar.reverse()
print(ar)
