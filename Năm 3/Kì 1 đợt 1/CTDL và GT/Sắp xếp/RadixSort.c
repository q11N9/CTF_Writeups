#include <stdio.h>
#include <math.h>
int digit(int n, int k){
    int value = 1;
    for (int i = 0; i < k; i++)
    {
        value *= 10;
    }
    return (n / value) % 10;
    
}
int getMax(int arr[], int n){
    int max = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (max < arr[i]) max = arr[i];
    }
    int d = 0;
    while (max > 0)
    {
        max /= 10;
        d += 1;
    }
    return d;
}
void radixSort(int arr[], int n, int k){
    int b[10];
    for (int t = 0; t < k; t++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            b[digit(arr[j], t)] = arr[j];
        }
        int idx = 0;
        for (int h = 0; h < 9; h++)
        {
            arr[idx] = b[h];
            idx += 1;
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
    int k = getMax(arr, n);
    radixSort(arr, n, k);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}