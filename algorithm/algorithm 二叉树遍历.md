
## 先序遍历
```c
	void PreOrderTraversal (BinTree BT)
	{
		if ( BT )
		{
			printf("%d", BT->Data);
			PreOrderTraversal( BT->Left );
			PreOrderTraversal( BT->Right );
		}
	}
```
## 中序遍历
```c
	void PreOrderTraversal (BinTree BT)
	{
		if ( BT )
		{
			PreOrderTraversal( BT->Left );
			printf("%d", BT->Data);
			PreOrderTraversal( BT->Right );
		}
	}
```
## 后序遍历
```c
	void PreOrderTraversal (BinTree BT)
	{
		if ( BT )
		{
			PreOrderTraversal( BT->Left );
			PreOrderTraversal( BT->Right );
			printf("%d", BT->Data);
		}
	}
```
## 中序遍历非递归（使用栈）
```c
	void InOrderTraversal (BinTree BT)
	{
		BinTree T = BT;
		Stack S = CreatStack(MaxSize);//创建初始化栈S
		while( T || !IsEmpty(S))
		{
			while(T)
			{
				Push(S,T);//压栈的是地址
				T = T->Left;
			}
			if(!IsEmpty(S))
			{
				T = Pop(S);
				printf("%d",T->Data);
				T = T->Right;
			}
		}
	}
```
## 先序遍历非递归（使用栈）
```c
	void InOrderTraversal (BinTree BT)
	{
		BinTree T = BT;
		Stack S = CreatStack(MaxSize);//创建初始化栈S
		while( T || !IsEmpty(S))
		{
			while(T)
			{
				printf("%d",T->Data);
				Push(S,T);//压栈的是地址
				T = T->Left;
			}
			if(!IsEmpty(S))
			{
				T = Pop(S);
				T = T->Right;
			}
		}
	}
```
## 层序遍历
```c
	void LevelOrederTraversal (BinTree BT)
	{
		Queue Q;
		BinTree T;
		if( !BT ) return;
		Q = CreatQueue( MacSize);
		AddQ( Q, BT );
		while (!IsEmptyQ(Q))
		{
			T = DeleteQ(Q);
			printf("%d\n",T->Left);
			if (T-Left)
				AddQ(Q,T-Left);
			if(T->Right)
				AddQ(Q,T-Right);
		}
	}
```