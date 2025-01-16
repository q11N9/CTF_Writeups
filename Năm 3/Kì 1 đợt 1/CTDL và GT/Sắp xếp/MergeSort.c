#include <stdio.h>
#include <stdlib.h>
void merge(int arr[], int left, int mid, int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int l[n1], r[n2];
    for (int i = 0; i < n1; i++)
    {
        l[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++)
    {
        r[j] = arr[mid + 1 + j];
    }
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
    {
        if (l[i] <= r[j])
        {
            arr[k] = l[i];
            i += 1;
        }
        else{
            arr[k] = r[j];
            j += 1;
        }
        k += 1;
    }
    while (i < n1)
    {
        arr[k] = l[i];
        i += 1;
        k += 1;
    }
    while (j < n2)
    {
        arr[k] = r[j];
        j += 1;
        k += 1;
    } 
    
    
}
void mergeSort(int arr[], int left, int right){
    if (left < right){
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
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
    mergeSort(arr, 0, n - 1);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}