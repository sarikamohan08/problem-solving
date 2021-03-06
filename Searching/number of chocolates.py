def upperBound(arr,n,target):
    low=0
    high=n
    while(low<high):
        mid=low+(high-low)//2
        
        if(arr[mid]<=target):
            low=mid+1
            
        else:
            high=mid
    return low


def main():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr)
    q=int(input())
    while(q>0):
        ele=int(input())
        print(upperBound(arr,n,ele))
        q=q-1
    
main()
