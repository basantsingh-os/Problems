def pairSum(arr,sum):
    s=set()
    for i in range(0,len(arr)):
        result=[]
        temp=sum-arr[i]
        if (temp  in s):
            result.append(arr[i])
            result.append(temp)
            return result    
        s.add(arr[i])  
    return []      



    

arr=[10,5,2,3,-6,9,11]
s=4

if (len(pairSum(arr,s))==0):
    print("Empty list")
else:
    print(pairSum(arr,s))