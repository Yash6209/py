lst= eval(input("enter the list:"))
length=len(lst)
found=0
for i in range(0,length-1):
    if lst[i]>0:
        print(lst[i])
    else:
        continue
