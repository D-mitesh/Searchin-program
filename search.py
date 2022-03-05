#Taking items from user and appending in a list
listem=[]
ran=int(input("Enter the range upto which you want to add data : "))
for i in range(ran):
    item=int(input("Enter number to add in list : "))
    listem.append(item)
li=listem

#linear searching program
def lise(li):
    var=int(input("Enter the number to be search="))
    count=0
    for i in range(len(li)):
        if var==li[i]:
            print("Element found ",var,"at index place ",i)
        else:
            count=count+1
            continue
    if count==len(li):
        print("Element not found")
    else:
        pass

#binary search program
def bise(li):
    li.sort()
    var=int(input("Enter the number to be search="))
    liste=[]
    l=(len(li))
    mid=int(l/2)
    if var==li[mid]:
        print("Element found ",var)
    elif var>li[mid] and (l!=1):
        for i in range(mid+1,l):
                liste.append(li[i])
        bise(liste)
    elif var<li[mid] and (l!=1):
        for i in range(mid):
            liste.append(li[i])
        bise(liste)
    else:
        print("not found")

#Giving option to user for search type
print("Enter which type of search you want to perform>>>")
opt=int(input("1>Linear Search 2>Binary Search : "))
if opt==1:
    lise(li)
elif opt==2:
    bise(li)
else:
    print("There is no such option available!")