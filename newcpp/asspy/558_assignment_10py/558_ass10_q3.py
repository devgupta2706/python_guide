term= lambda x,y: x+y 
f0,f1=0,1
n=int(input("Enter the number "))
print("Fibonacci series:",end=" ")
print(f0,end=" ")
while n>1:
    print(f1,end=" ")
    f2=f1
    f1=term(f1,f0)
    f0=f2
    n=n-1

