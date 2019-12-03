
```c++

# include<stdio.h>
# include<math.h>
# include<string.h>
int f[105],V;

inline int max(int a,int b)
{
    return a>b?a:b;
}

void ZeroOnePack(int cost,int weight)   //01背包
{
   int v;
   for(v=V;v>=cost;v--)
     f[v]=max(f[v-cost]+weight,f[v]);
}

void CompletePack(int cost,int weight)   //完全背包
{
   int v;
   for(v=cost;v<=V;v++)
     f[v]=max(f[v-cost]+weight,f[v]);
}

void MultipelePack(int cost,int weight,int amount)  //多重背包
{
  int k;
  if(cost*amount>=V)
  {
     CompletePack(cost,weight);
     return;
  }
  for(k=1;k<amount;k*=2)
  {
     ZeroOnePack(k*cost,k*weight);
     amount=amount-k;
  }
  ZeroOnePack(amount*cost,amount*weight);
}

int main()
{
   int t,i,n,cost,weight,amount;
   scanf("%d",&t);
   while(t--)
   {
      memset(f,0,sizeof(f));
      scanf("%d%d",&V,&n);
      for(i=1;i<=n;i++)
      {
         scanf("%d%d%d",&cost,&weight,&amount);
         MultipelePack(cost,weight,amount);
      }
      printf("%d\n",f[V]);
   }
   return 0;
}

```