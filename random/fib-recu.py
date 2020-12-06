        
def fun():
      a, b = 1,1
      while 1:
          yield a
         # print(a,b)
          a,b = b, a+b
      #return(a)

c= 0 
for x in fun():
   # print(x)
    c +=1
    if c==10:
        break
    
    
    
def fib(n):
     
    if n==0:
        pass
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        #print(fib(n-1) + fib(n-2))
        return fib(n-1) + fib(n-2)

for x in range():
    print(fib(x))
