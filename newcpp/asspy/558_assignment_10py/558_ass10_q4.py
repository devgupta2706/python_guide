import array
import random
even_count,odd_count=0,0
check=lambda x: x%2==0
arr=array.array('i',[])
for i in range(10):
    arr.insert(i,random.randint(0,9))
for i in range(10):
    if check(arr[i]):
        even_count+=1
    else:
        odd_count+=1
for i in range(10):
    print(arr[i],end=" ")
print("\nEven numbers:",even_count)
print("Odd numbers:",odd_count)