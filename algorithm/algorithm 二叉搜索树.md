
## 二叉搜索树的查找操作（尾递归）

```c
	Position find (ElementType X,BinTree BST)
	{
		if(!BST)
			return NULL;
		if(X > BST->Data)
			return Find(X,BST->Right);
		else if (X < BST->Data)
			return find(X,BST->Left);
		else
			return BST;
	}

```
## 二叉搜索树的查找操作（尾递归）改写成迭代函(效率更高)

```c
	Position Iterfind (ElementType X,BinTree BST)
	{
		while(BST)
		{
		if(X > BST->Data)
			BST = BST->Right;
		else if (X < BST->Data)
			BST = BST->Left;
		else
			return BST;
		}
	}

```
## 二叉搜索树查找最小元素

```c
	Position FindMin (BinTree BST)
	{
		if(!BST)
			return NULL;
		else if(!BST->Left)
			return BST;
		else
			return FindMin (BST->Left);
	}

```
## 二叉搜索树查找最大元素

```c
	Position FindMan (BinTree BST)
	{
		if(BST)
			while (BST->Right) 
				BST = BST->Right;
		return BST;
	}

```
## 二叉搜索树的插入算法

```c
	BinTree Insert (ElementType X,BinTree BST)
	{
		if(!BST)
		{
			BST = malloc(sizeof(struct TreeNode));
			BST->Data = X;
			BST->Left = BST->Right = NULL;
		} else 
		{
			if(X < BST->Data)
				BST->Left = Insert(X,BST->Left);
			else if(X>BST->Data)
				BST->Right = Insert(X,BST->Right);
		}
		return BST;
	}

```
## 二叉搜索树的删除算法

```c
	BinTree Delete (ElementType X,BinTree BST)
	{
		Position Tmp;
		if(!BST)
			printf("要删除的元素为找到");
		else if (x<BST->Data)
			BST->Left = Delete(X,BST->Left);
		else if (x>BST->Data)
			BST->Right = Delete(X,BST->Right);
		else
		{
			if(BST->Left && BST->Right)//有左右子树
			{
				Tmp = FindMin (BST->Right);
				BST->Data = Tmp->Data;
				BST->Right = Delete(BST->Data,BST->Right);
			} else {
				Tmp = BST;
				if(!BST->Left)
					BST = BST->Right;
				else if( !BST->Right)
					BST = BST->Left;
				free(Tmp);
			}
		}
		return BST;
	}

```	

