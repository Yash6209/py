lst= eval(input("enter the list:"))
length=len(lst)
for i in range(0,length-1):
    if lst[i]>0:
        print(lst[i])
    else:
        continue
