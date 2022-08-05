# first import os, io
import io,os,sys
# to enable faster input redefine input and this is better for large input data from judges file
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# s=input().decode() 

# for small input we can write
ss=sys.stdin.readline()
# for faster output fast convert it to string
# sys.stdout.write(s)
sys.stdout.write(ss)

# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
 
# Printing the Output to output.txt file
sys.stdout = open('output.txt', 'w')