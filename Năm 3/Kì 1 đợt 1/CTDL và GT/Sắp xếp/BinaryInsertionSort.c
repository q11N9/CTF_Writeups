#include<stdio.h>
int bSearchForPosition(int arr[], int i, int x){
    int low = 0, high = i - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] < x)
        {
            low = mid + 1;
        }
        else high = mid - 1;
        
    }
    return low;

}
void bInsertionSort(int arr[], int n){
    for (int i = 1; i < n; i++)
    {
        int x = arr[i];
        int k = bSearchForPosition(arr,i, x);
        for (int j = i; j > k; j--)
        {
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
        }
        arr[k] = x;
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
    bInsertionSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}