/*You are required to complete this method*/
 int max_path_sum(int A[], int B[], int l1, int l2)
{
//Your code here
int sum1=0,sum2=0, res=0;
int i=0,j=0;
while(i<l1 && j<l2)
{
    if(A[i]>B[j])
    {
        sum2+=B[j++];
    }
    else
    if(B[j]>A[i])
    {
        sum1+=A[i++];
    }
    else    //(A[i]==B[j])
    {
     if (sum1>sum2) 
     {
         res+=sum1;
     }
     else
        res+=sum2;
     sum1=0;sum2=0;
     while (i < l1 &&  j < l2 && A[i] == B[j])
            {
                res= res + A[i++];
                j++;
            }
    }
}
while(i<l1)
{
    sum1+=A[i++];
}

while(j<l2)
{
    sum2+=B[j++];
}   
res+=(sum1>sum2)?sum1:sum2;


return res;

    
}
