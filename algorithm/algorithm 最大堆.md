
## 最大堆

```c
	//最大堆的建立
	//方法1：将N个元素一个个相继插入到一个初始为空的堆去
	//方法2：将N个元素按输入顺序存入，再进行调整（利用删除的策略）
	//  方法2自己写一个
	typedef struct HeapStruct *MaxHeap;
	struct HeapStruct {
		ElementType *Elements;
		int Size;
		int Capacity;
	};
	
	//最大堆的创建
	MaxHeap Create (int MaxSize)
	{
		MaxSize H = malloc(sizeof(struct HeapStruct));
		H->Elements = malloc((MaxSize+1) * sizeof(ElementType));
		H->Size = 0;
		H->Capacity = MaxSize;
		H->Elements[0] = MaxData;//定义哨兵，为大于堆中所有可能值
		return H;
	}
	
	//最大堆的插入
	void Insert (MaxHeap H,ElementType item)
	{
		int i;
		if(IsFull(H)){
			printf("最大堆已满");
			return;
		}
		i = ++H->Size;
		for(;H->Elements[i/2]<item;i/=2){
			H->Elements[i]=H->Elements[i/2];
		}
		H->Elements[i] = item;
	}
	
	//最大堆的删除
	ElementType DeleteMax (MaxHeap H)
	{
		int Parent,Child;
		ElementType Maxitem,temp;
		if(IsEmpty(H)){
			printf("最大堆已空");
			return;
		}
		Maxitem = H->Elements[1];
		temp = H->Elements[H->Size--];
		for(Parent=1;Parent*2<=H->Size;Parent=Child){
			Child = Parent * 2;
			if(Child!=H->Size)&&(H->Elements[Child]<H->Elements[Child+1])
				Child++;
			if(temp >= H->Elements[Child])
				break;
			else
				H->Elements[Parent] = H-Elements[Child];
		}
		H->Elements[Parent] = temp;
		return Maxitem;
	}
	

```