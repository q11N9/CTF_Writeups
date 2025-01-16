#include <stdio.h>

void selectionSort(int arr[], int n){
    for (int i = 0; i < n - 1; i++)
    {
        int k = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[k] > arr[j])
            {
                k = j;
            }
            
            
        }
        if (k != i){
                int temp = arr[k];
                arr[k] = arr[i];
                arr[i] = temp;
            }
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
    selectionSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}