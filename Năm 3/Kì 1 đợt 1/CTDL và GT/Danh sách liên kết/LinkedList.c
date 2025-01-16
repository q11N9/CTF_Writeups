#include <stdio.h>
#include <stdlib.h>

typedef int DataType;

typedef struct Node{
    DataType data;
    struct Node *next;
}Node;

typedef Node* LinkedNode;
 
typedef struct LinkedList
{
    LinkedNode Head;
    LinkedNode Tail;
}LinkedList;

LinkedList* createLinkedList();
void destroyLinkedList(LinkedList *list);
void insertNode(LinkedList *list, DataType data);
int searchNode(LinkedList *list, DataType data);
void deleteNode(LinkedList *list, DataType data);
void addTail(LinkedList *list, DataType data);
void printList(const LinkedList *list);
void addHead(LinkedList *list, DataType data);
void addAfter(LinkedList *list, DataType target, DataType data);


void _addTail(LinkedList *list, LinkedNode newNode);
void _addHead(LinkedList *list, LinkedNode newNode);
LinkedNode _createNode(DataType data);
void _insertNode(LinkedList *list, LinkedNode newNode);
int _searchNode(const LinkedList *list, DataType data);
int _deleteNode(LinkedList *list, DataType data);
int _addAfter(LinkedList *list, LinkedNode targetNode, DataType data);

LinkedList* createLinkedList() {
    LinkedList *list = (LinkedList *)malloc(sizeof(LinkedList));
    if (!list) {
        return NULL; 
    }
    list->Head = list->Tail = NULL;
    return list;
}

void destroyLinkedList(LinkedList *list) {
    if (list->Head) {
        free(list->Head);
    }
    free(list);
}

int main() {
    LinkedList *list = createLinkedList();
    if (list) {
        destroyLinkedList(list); 
    }
    return 0;
}