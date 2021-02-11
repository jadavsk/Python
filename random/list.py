# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:18:27 2020

@author: Sanjay
"""


inp = [7,1,1,1,5,2,6,8,5,2]
din = []
#print(len(inp))
for x in range(0,len(inp)):
    f = 1
    for y in range(0,len(inp)):    
        if inp[x] == inp[y] and x !=y:
            #print("false")
            f = 2
    if f == 1:
        din.append(inp[x])
       
  
print(dict(zip(inp, inp)).keys())

    