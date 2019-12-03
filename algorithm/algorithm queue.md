
## Queue的数组定义
```c
	//队列  数组实现
	#define MaxSize 100
	typedef struct {
		ElementTyPe Data[MaxSize];
		int front;
		int rear;
	}Queue;
	
	//入队列
	void AddQ(Queue *PtrQ,ElementTyPe item){
		if((PtrQ->rear+1) % MaxSize == PtrQ->front){
			printf("队列满");
			return;
		}
		PtrQ->rear = (PtrQ->rear + 1) % MaxSize;
		PtrQ->Data[PtrQ->rear] = item;
	}
	
	//出队列
	ElementTyPe DeleteQ(Queue *PtrQ){
		if(PtrQ->front == PtrQ-rear){
			printf("队列空");
			return ERROR;
		}else{
			PtrQ->front = (PtrQ->front + 1)% MaxSize;
			return PtrQ->Data[PtrQ->front];
		}
	}
```

## Queue的链表定义
```c
	//链表实现  尾进  头出
	typedef struct Node{
		ElementTyPe Data;
		struct Node *Next;
	}QNode;
	typedef struct{
		QNode *front;//指向对头
		QNode *rear;//指向队尾
	}LinkQueue;
	LinkQueue *PtrQ;
	
	//不带头结点的链式队列出队操作的示例
	ElementTyPe DeleteQ( LinkQueue *PtrQ){
		QNode *FrontCell;
		ElementTyPe FrontElem;
		
		if(PtrQ->front == NULL){
			printf("队列空")；
			return ERROR;
		}
		FrontCell = PtrQ->front;
		if(PtrQ->front == PtrQ->rear)
			PtrQ->front = PtrQ->rear = NULL;
		else {
			PtrQ->front = PtrQ->front->Next;
		}
		FrontElem = FrontCell->Data;
		free(FrontCell);
		return FrontElem;
	}
```
