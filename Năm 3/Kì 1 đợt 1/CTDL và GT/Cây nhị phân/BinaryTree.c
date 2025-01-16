#include <stdio.h>

typedef int DataType;

typedef struct Node{
    DataType data;
    Node* left;
    Node* right;    
}Node;

typedef struct BinaryTree{
    Node* root;
}BinaryTree;

BinaryTree* createBinaryTree();
void destroyBinaryTree(BinaryTree *tree);
Node *createNode(DataType data);
void destroyNode(Node* node);

// Function definitions
BinaryTree* createBinaryTree() {
    BinaryTree *tree = (BinaryTree *)malloc(sizeof(BinaryTree));
    if (!tree) {
        return NULL; 
    }
    tree->root = NULL;
    return tree;
}

void destroyBinaryTree(BinaryTree *tree) {
    if (tree->root) {
        destroyNode(tree->root);
    }
    free(tree);
}

Node *createNode(DataType data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        return NULL;
    }
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

void destroyNode(Node* node) {
    if (node) {
        if (node->left) {
            destroyNode(node->left);
        }
        if (node->right) {
            destroyNode(node->right);
        }
        free(node);
    }
}
int main() {
    BinaryTree *tree = createBinaryTree();
    if (tree) {
        
        destroyBinaryTree(tree);
    }
    return 0;
}