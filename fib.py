i= int(input("enter the limit of fibonacci series:"))
x=0
y=1
print(x,",",y,end=",")

for j in range(2,i):
    sum=x+y
    print(sum,end=",")
    x=y
    y=sum
