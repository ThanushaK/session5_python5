# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:25:58 2019

@author: thanusha
"""

#problem statement 1
def Error():         #defining a function
    try:           # try block to perform operation
       a=5/0
       print(a)
        
    except:          # exception  block to catch the zero division error
        print("its a zero division error") 

Error()   #fuction call





#problem statement 2

subjects=['Americans','Indians']     #declaring the lists
verbs=['play','watch']
objects=["Baseball","Cricket"]
for i in subjects:                  #nesting for loops to iterate over the lists to get the resultant output
   for j in verbs :
      for k in objects :
            print (i,j,k)
