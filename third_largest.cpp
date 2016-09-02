 /*you are required to complete this function*/

int thirdLargest(int a[],int n)
{
    //Your code here
    
  int f=a[0],s=-1,t=-1;
    for (int i=1;i<n;i++)
    {
        if (a[i]>f)
        {
            t=s;
            s=f;
            f=a[i];
           
        }
        else if(a[i]>s)
            {
               t=s;
               s=a[i];
              
            }
            else
                t=a[i];
    }
  return t;
}
