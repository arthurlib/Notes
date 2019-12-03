
```c

//01背包问题模板
# include <stdio.h>  
# include <stdlib.h>  
# include <string.h>  
# define max(x,y) x>y?x:y;  
int v[1001];//价值  
int w[1001];//重量  
int dp[1001][1001];  
int main()  
{  
    int n,m;  
    while(scanf("%d%d",&m,&n)!=EOF)  
    {  
        memset(dp,0,sizeof(dp));//初始化  
        for(int i=1; i<=n; i++)  
            scanf("%d%d",&w[i],&v[i]);  
        for(int i=1; i<=n; i++) // 物品数  
            for(int j=m; j>=w[i]; j--) //放入背包  
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);// 与前面对比  
        printf("%d\n",dp[n][m]);  
    }  
}  
  
//01背包第K优解问题  
struct pack  
{  
    int v;//体积  
    int w;//价值  
}node[length];  
  
for(i = 0;i<n;i++)  
{  
    for(j = v;j>=node[i].v;j--)  
    {  
        for(d = 1;d<=k;d++)  
        {  
            a[d] = dp[j-node[i].v][d] + node[i].w;  
            b[d] = dp[j][d];  
        }  
        x = y = z = 1;  
        a[d] = b[d] = -1;  
        while(z<=k && (x<=k || y<=k))  
        {  
            if(a[x]>b[y])  
            dp[j][z] = a[x++];  
            else  
            dp[j][x] = b[y++];  
            if(dp[j][z]!=dp[j][z-1])  
            z++;  
        }  
    }  
}  
//dp[v][k]为第K优解，例题：HDU2639  

```