#code
t=int(raw_input().strip())
for i in range(t):
    n,m =map(int, raw_input().strip().split())
    one_round= n*(n+1)/2;
    after_rounds=m%one_round
    #print 'after_rounds',after_rounds
    left=after_rounds
    for j in range(n):
        o_left=left
        left =left-j-1
        #print 'left: ',left
        if left<0:
            print o_left
            break
        if left==0:
            print left
            break
