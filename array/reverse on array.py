# reverse on array
arr=[4,5,2]
length=0
for i  in arr:
    length+=1
start=0
end=length-1

while start<end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start+=1
    end-=1
print("The reverse array is:",arr)