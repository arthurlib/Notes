
```c

//多重背包问题模板
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cctype>
#include <cstring>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>

using namespace std;
//Constant Declaration
/*--------------------------*/ 
//#define LL long long 
#define LL __int64
const int M=110;
const int INF=1<<30;
const double EPS = 1e-11;
const double PI = acos(-1.0);
/*--------------------------*/
// some essential funtion
/*----------------------------------*/
void Swap(int &a,int &b){ int t=a;a=b;b=t; }
int Max(int a,int b){ return a>b?a:b; }
int Min(int a,int b){ return a<b?a:b; }
int Gcd(int a,int b){ while(b){b ^= a ^=b ^= a %= b;} return a; }
/*----------------------------------*/
//for (i = 0; i < n; i++)
/*----------------------------------*/

int c[M], w[M], n1[M];//c:费用 w:价值 n1:数量
int f[M];//f[与V有关],c和w[与n]有关
int v, V, V1;//V:容量 V1:容量2

//01背包
void ZeroOnePack(int c, int w)
{
    for (int v = V; v >= c; v--)
    {
        f[v] = Max(f[v], f[v-c] + w);
    }
}

//完全背包
void CompletePack(int c, int w)
{
    for (int v = c; v <= V; v++)
    {
        f[v] = Max(f[v], f[v-c] + w);
    }
}

//多重背包，二进制。
void MultiplePack(int c, int w, int n1)
{
    if (c * n1 >= V)
    {
        CompletePack(c, w); 
    }
    else
    {
        int k = 1;
        while (k < n1)
        {
            ZeroOnePack(k*c, k*w);
            n1 -= k;
            k <<= 1;
        }
        ZeroOnePack(n1*c, n1*w);
    }
}

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t, case1 = 0;
    scanf("%d", &t);
    int n, m;//n:物品种数
    int i, j;

    //scanf("%d%d", &n, &m);
    while (t--)
    {
        scanf("%d%d", &V, &n);
        for (i = 1; i <= n; i++)
        {
            scanf("%d%d%d", &c[i], &w[i], &n1[i]);

        }

        memset(f, 0, sizeof(f));

        for (i = 1; i <= n; i++)
        {
            MultiplePack(c[i], w[i], n1[i]); 
        }

        printf("%d\n", f[V]);

    }

    return 0;
}

```