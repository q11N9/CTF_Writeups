// heap: ordered binary tree
// max heap: parent > child 

#include <stdio.h>
#include <stdlib.h>

void insertHeap(int arr[], int left, int right){
    int p = 2*left + 1;
    if (p > right) return;
    if (p < right && arr[p] < arr[p + 1]) p += 1 ;
    if (arr[left] < arr[p]){
            int temp = arr[left];
            arr[left] = arr[p];
            arr[p] = temp;
            insertHeap(arr, p, right);
        }  
    return;
}
void createHeap(int arr[], int n){
    for (int i = n/2 - 1; i >= 0; i--)
    {
        insertHeap(arr, i ,n - 1);
    }
    return;
}
void heapSort(int arr[], int n){
    createHeap(arr,n);
    for (int i = n - 1; i > 0; i--)
    {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        insertHeap(arr, 0, i - 1);
    }
    return;
}

int main(){
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);
    int arr[n];
    printf("Nhap gia tri cac phan tu cua mang: \n");
    for (int i = 0; i < n; i++)
    {
        printf("a[%d] = ", i);
        scanf("%d", &arr[i]);
    }
    heapSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}