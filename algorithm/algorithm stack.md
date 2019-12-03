
## 用数组来完成堆栈
```c
	#define MaxSize 30
	typedef struct {
		ElementType Data[MaxSize];
		int Top;
	}Stack;
		//判断是否已满及压入
	void Push(Stack *PtrS, ElementType item){
		if(PtrS->Top == MaxSize-1){
			printf("堆栈满");
			return;
		}else {
			PtrS->Data[++(PtrS->Top)] = item;
			return;
		}
	}
		//判断是否为空及出栈
	ElementType Pop(Stack *PtrS){
		if(PtrS->Top == -1){
			printf("堆栈空");
			return ERROR;
		}else{
			return PtrS->Data[(PtrS->Top)--];
		}
	}
```
## 一个数组实现两个堆栈
```c
	#define MaxSize 30
	struct DStack {
		ElementType Data[MaxSize];
		int Top1;
		int Top2;
	}S;
	S.Top1 = -1;
	S.Top2 = MaxSize;
		//判断是否已满及压入
	void Push (struct DStack *PtrS, ElementType item, int Tag){
		if(PtrS->Top2 - PtrS->Top1 == 1){
			printf("堆栈满");
			return;
		}
		if(Tag == 1){
			PtrS->Data[++PtrS->Top1] = item;
		}else{
			PtrS->Data[--(PtrS->Top2)] = item;
		}
	}
		//判断是否为空及出栈
	ElementType Pop (struct DStack *PtrS, int Tag){
		if( Tag == 1){
			if(PtrS->Top1 == -1){
				printf("堆栈空");
				return NULL;
			}else{
				return PtrS->Data[(PtrS->Top1)--];
			}
		}else{
			if(PtrS->Top2 == MaxSize){
				printf("堆栈空");
				return NULL;
			}else{
				return PtrS->Data[(PtrS->Top2)++];
			}
		}
	}
```
## 堆栈的链式存储实现
```c
	typedef struct Node {
		ElementType Element;
		struct Node *Next;
	}LinkStack;
	LinkStack *Top;
		//构建一个堆栈的头结点，返回指针
	LinkStack *CreateStack(){
		LinkStack *S;
		S = (LinkStack *)malloc(sizeof(struct Node));
		S->Next = NULL;
		return S;
	}
		//判断堆栈S是否为空，空返回1，否则返回0
	int IsEmpty(LinkStack *S){
		return S->Next == NULL;
	}
		//将元素压入堆栈
	void Push (ElementType item,LinkStack *S){
		struct Node *TmpCell;
		TmpCell = (LinkStack *)malloc(sizeof(struct Node));
		TmpCell->Element = item;
		TmpCell->Next = S->Next;
		S->Next = TmpCell;
	}
		//删除并返回堆栈的栈顶元素
	ElementType Pop (LinkStack *S){
		struct Node *FirstCell;
		ElementType Topeleml;
		if(IsEmpty(S)){
			printf("堆栈空");
			return NULL;
		}else{
			FirstCell = S->Next;
			S->Next = FirstCell->Next;
			TopElem = FirstCell->Element;
			free(FirstCell);
			return TopElem;
		}
	}
```
