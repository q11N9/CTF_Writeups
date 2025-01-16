#include <stdio.h>

void quickSort(int arr[], int left, int right){
    int mid = (left + right) / 2;
    int x = arr[mid];
    int i = left, j = right;
    while (i < j)
    {
        while (arr[i] < x) i += 1;
        while (arr[j] > x) j -= 1;
        if (i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i += 1; 
            j -= 1;
        }
        

    }
    if (j > left) quickSort(arr, left, j);
    if (right > i) quickSort(arr, i + 1, right);
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
    quickSort(arr, 0, n - 1);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}