#code
n=int(raw_input().strip())
for i in range(n):
    sz=int(raw_input().strip())
    arr= map(int,raw_input().strip().split())
    k=int(raw_input().strip())
    #print arr
    for j in range(0,sz,k):
        s=j
        
        if (j+k)<sz:
            e=j+k-1
        else:
            e=sz-1
        for l in range(s,e):
            if l<e-l+s:
                temp=arr[l]
                arr[l]=arr[e-(l-s)]
                arr[e-(l-s)]=temp
            
    
    print ' '.join(str(a) for a in arr)
