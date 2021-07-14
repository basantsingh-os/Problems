def triplets(arr:[int],target:int):
    sum=[]
    result=[]
    arr.sort()
    for i in range(0,len(arr)):
        left=i+1
        right=len(arr)+-1
        while(left<right):
            sum=arr[i]
            sum+=arr[left]
            sum+=arr[right]
            if (target==sum):
                result.append([arr[i],arr[left],arr[right]])
                left+=1
                right-=1
            elif (target> sum):
                left+=1
            elif (target < sum):
                right-=1
    return result                   



arr=[1,2,3,4,5,6,7,8,9,15]
target=18
print(triplets(arr,target))



