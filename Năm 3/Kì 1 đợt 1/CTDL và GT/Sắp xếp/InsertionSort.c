#include <stdio.h>
void insertionSort(int arr[], int n){
    for (int i = 1; i < n; i++)
    {
        int x = arr[i];
        int j = i - 1;
        while (x < arr[j] && j >=0)
        {
            int temp = arr[j + 1];
            arr[j + 1] = arr[j];
            arr[j] = temp;
            j -= 1;
        }
        arr[j + 1] = x;
        
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
    insertionSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}