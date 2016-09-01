#code
n = int(raw_input().strip())
for i in range(n):
    sz = int(raw_input().strip())
    arr= raw_input().strip().split()
    arr = map(int, arr)
    
    m = 0
    r = 0
    for i in range(0, sz):
		r = r + arr[i]
		if r < 0:
			r = 0
		
		if (m < r):
			m = r
			
    if m==0:
        maxi=arr[0]
        for i in range(1,sz):
            if maxi<arr[i]:
                maxi=arr[i]
        print maxi
    else:
        print m
