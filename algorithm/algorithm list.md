
## List的数组定义
```c
	//线性表数组定义
	typedef struct{
		ElementType Data[MAXSIZE];
		int Last;
	}List;
	List L,*PtrL;
	
	//线性表数组建立
	List *MakeEmpty(){
		List *PtrL;
		PtrL = (List *)malloc(sizeof(List));
		PtrL->Last = -1;
		return PtrL;
	}
	
	//线性表数组查找
	int Find(ElementType X,List *PtrL){
		int i = 0;
		while( i <= PtrL->Last && PtrL->Data[i]!= X ){
			i++;
		}
		if( i > PtrL-Last)
			return -1;
		else
			return i;//这里i返回的是下标
	}
	
	//线性表数组插入
	//这里的i是第几个元素
	void Insert(ElementType X,int i,List *PtrL){
		int j;
		if(PtrL-Last == MAXSIZE-1){
			printf("表满");
			return;
		}
		if(i < 1 || PtrL->Last+2){
			printf("位置不合法");
			return;
		}
		for(j = PtrL->Last;j >= i-1;j--){
			PtrL->Data[j+1] = PtrL->Data[j];
		}
		PtrL->Data[i-1] = X;
		PtrL->Last++;
		return;
	}
	
	//线性表数组删除
	//这里的i是第几个元素
	void Delete( int i,List *PtrL){
		int j;
		if( i<1 || i > PtrL->Last+1){
			printf("不存在第%d个元素"，i);
			return;
		}
		for(j = i;j<=PtrL->Last;j++){
			PtrL->Data[j-1] = PtrL->Data[j];
		}
		PtrL->Last--;
		return;
	}
```


## List的链表定义

```c
	//线性表链表定义
	typedef struct Node {
		ElementType Data;
		struct Node *Next;
	}List;
	List L,*PreL;
	
	//线性表链表表长
	int Length(List *PreL){
		List *p = PreL;
		int j = 0;
		while(p){
			p = p->Next;
			j++;
		}
		return j;
	}
	
	//线性表链表查找
	//按序号
	List *FindKth(int K,List *PreL){
		List *p = PreL;
		int i = 1;
		while (p!=NULL && i<K){
			p = p->Next;
			i++;
		}
		if(i==K)return p;
		else return NULL;
	}
	//按值
	List *Find(ElementType X,List *PreL){
		List *p = PreL;
		while (p!=NULL && p->Data != X){
			p = p-Next;
		}
		return p;
	}
	
	//线性表链表插入
	List *Insert(ElementType X,int i,List *PreL){
		List *p,*s;
		if(i==1){
			s = (List *)malloc(sizeof(List));
			s->Data = X;
			s->Nextj = PreL;
			return s;
		}
		p = FindKth(i-1,PreL);//查找第i-1个节点
		if(p == NULL){
			printf("参数i错");
			return NULL;
		}else{
			s = (List *)malloc(sizeof(List));
			s->Data = X;
			s->Next = p->Next;
			p->Next = s;
			return PreL;
		}
	}
	
	//线性表链表删除
	List *Delete(int i,List *PreL){
		List *p,*s;
		if(i == 1){
			s = PreL;
			if(PreL!=NULL)
				PreL = PreL->Next;
			else 
				return NULL;
			free(s);
			return PreL;
		}
		p = FindKth(i-1,PreL);
		if(p == NULL){
			pirntf("第%d个节点不存在",i-1);return NULL;
		}else if(p-Next == NULL){
			pirntf("第%d个节点不存在",i);return NULL;
		}else{
			s = p-Next;
			p-Next = s->Next;
			free(s);
			return PreL;
		}
	}
```
