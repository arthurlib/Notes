
## 插入排序
```c
	#include <stdio.h>
	#include <stdlib.h>
	
	void xuanze (int a[],int n)
	{
		for(int i=0;i<n-1;i++)
		{
			int min=i;
			for(int j=i+1;j<n;j++)
			{
				if(a[j]<a[min])
				{
					min=j;
				}
			}
			if(i!=min)
			{
				int temp=a[i];
				a[i]= a[min];
				a[min] = temp;
			}
		}
	}
```

## 堆排序
```c
	#include<stdio.h>
	
	void shift(int a[] , int i , int m)
	{
		int k , t;
	
	    t = a[i]; k = 2 * i + 1;
	    while (k < m)
	    {
	        if ((k < m - 1) && (a[k] < a[k+1])) k ++;
	        if (t < a[k]) {a[i] = a[k]; i = k; k = 2 * i + 1;}
	        else break;
	 	}
	    a[i] = t;
	}
	
	void dui(int a[] , int n)  //a 为排序数组，n为数组大小（编号0-n-1）
	{
		int i , k;
	
		for (i = n/2-1; i >= 0; i --)
			shift(a , i , n);
	    for (i = n-1; i >= 1; i --)
	    {
		 	k = a[0]; a[0] = a[i]; a[i] = k;
		 	shift(a , 0 , i);
	    }
	}
```
## 冒泡排序
```c
	#include <stdio.h>
	#include <stdlib.h>
	void maopao(int a[],int n)
	{
		for(int i=0;i<n-1;i++)
		{
			for(int j=0;j<n-i-1;j++)
			{
				if(a[j]>a[j+1])
				{
					int temp = a[j];
					a[j] = a[j+1];
					a[j+1] = temp;
				}
			}
		}
	}
	void maopaobetter(int a[],int n)
	{
		for(int i=0;i<n-1;i++)
		{
			bool isSort = true;
			for(int j=0;i<n-1-i;j++)
			{
				if(a[j]>a[j+1])
				{
					isSort = false;
					int temp = a[j];
					a[j] = a[j+1];
					a[j+1] = temp;
				}
			}
			if(isSort) break;
		}
	}
```
## 快速排序
```c
	#include <stdio.h>
	#include <stdlib.h>
	
	int partition(int arr[],int low,int high)
	{
		int key;
		key = arr[low];
		while(low<high)
		{
			while(low<high && arr[high]>=key)
				high--;
			if(low<high)
				arr[low++] = arr[high];
			while(low<high && arr[low]<=key)
				low++;
			if(low<high)
				arr[high--] = arr[low];
		}
		arr[low] = key;
		return low;
	}
	
	void kuaisu(int arr[],int start,int end)
	{
		int pos;
		if(start < end)
		{
			pos = partition(arr,start,end);
			kuaisu(arr,start,pos-1);
			kuaisu(arr,pos+1,end);
		}
	}
```
## 希尔排序
```c
	#include<stdio.h>
	#include<math.h>
	
	//根据当前增量进行插入排序
	void shellInsert(int array[],int n,int dk)
	{
	    int i,j,temp;
	    for(i=dk;i<n;i++)//分别向每组的有序区域插入
	    {
	        temp=array[i];
	        for(j=i-dk;(j>=i%dk)&&array[j]>temp;j-=dk)//比较与记录后移同时进行
	            array[j+dk]=array[j];
	        if(j!=i-dk)
	            array[j+dk]=temp;//插入
	    }
	}
	
	//计算Hibbard增量
	int dkHibbard(int t,int k)
	{
	    return int(pow(2,t-k+1)-1);
	}
	
	//希尔排序
	void xier(int array[],int n,int t)
	{
	    void shellInsert(int array[],int n,int dk);
	    int i;
	    for(i=1;i<=t;i++)
	        shellInsert(array,n,dkHibbard(t,i));
	}
	
	//此写法便于理解，实际应用时应将上述三个函数写成一个函数。
```
## 选择排序
```c
	#include <stdio.h>
	#include <stdlib.h>
	
	void xuanze (int a[],int n)
	{
		for(int i=0;i<n-1;i++)
		{
			int min=i;
			for(int j=i+1;j<n;j++)
			{
				if(a[j]<a[min])
				{
					min=j;
				}
			}
			if(i!=min)
			{
				int temp=a[i];
				a[i]= a[min];
				a[min] = temp;
			}
		}
	}
```
## 各排序算法比较
```c
	#include<stdlib.h>
	#include<stdio.h>
	#include<math.h>
	#include<time.h>/*用到了time函数，所以要有这个头文件*/
	#include"maopao.cpp"
	#include"charu.cpp"
	#include"xuanze.cpp"
	#include"kuaisu.cpp"
	#include"xier.cpp"
	#define MAX 100000
	#include"dui.cpp"
	void print(int num[])
	{
		int i;
		for(i=0;i<MAX;i++)
			printf("%d ",num[i]);
		printf("\n");
		
	}
	void suiji(int num[])
	{
		int i;
		srand((unsigned)time(NULL));/*播种子*/
		for(i = 0; i < MAX; i++)
		{
			num[i] = rand() % MAX;/*产生100以内的随机整数*/
			//printf("%d ",num[i]);
		}
		printf("\n");
	}
	int main(void)
	{
		clock_t start,stop;
		double duration;
		int num[MAX] = {0};
		double t[6];
		printf("将对%d个随机数进行排序\n",MAX);
	//冒泡
		suiji(num);
		start = clock();
		maopao(num,MAX);//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("冒泡排序时间：%f\n",duration);
		t[0]=duration;
	
	//插入
		suiji(num);
		start = clock();
		charu(num,MAX);//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("插入排序时间：%f\n",duration);
		t[1]=duration;
	//选择
		suiji(num);
		start = clock();
		xuanze(num,MAX);//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("选择排序时间：%f\n",duration);
		t[2]=duration;
	//快速
		suiji(num);
		start = clock();
		kuaisu(num,0,MAX-1);//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("快速排序时间：%f\n",duration);
		t[3]=duration;
	//希尔
		suiji(num);
		start = clock();
		xier(num,MAX,int(log(MAX+1)/log(2)));//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("希尔排序时间：%f\n",duration);
		t[4]=duration;
	//堆
		suiji(num);
		start = clock();
	//	BUILD(num);
		dui(num,MAX);//排序
		//print(num);
		stop = clock();
		duration = ((double)(stop - start))/CLK_TCK;
		printf("堆排序时间：%f\n",duration);
		t[5]=duration;
		putchar('\n');
		printf("冒泡排序时间：%f\n",t[0]);
		printf("插入排序时间：%f\n",t[1]);
		printf("选择排序时间：%f\n",t[2]);
		printf("快速排序时间：%f\n",t[3]);
		printf("希尔排序时间：%f\n",t[4]);
		printf("堆排序时间  ：%f\n",t[5]);
		system("pause");
		return 0;
	}
```
