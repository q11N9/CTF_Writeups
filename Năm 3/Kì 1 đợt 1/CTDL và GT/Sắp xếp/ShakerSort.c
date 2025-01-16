#include <stdio.h>
void shakerSort(int arr[], int n){
    int up = 0, down = n - 1, hv = 0;
    while (up < down)
    {
        for (int j = up; j < down; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                hv = j;
            }
            
        }
        down = hv;
        for (int  j = down; j > up; j--)
        {
            if (arr[j - 1] > arr[j])
            {
                int temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
                hv = j;
            }
            
        }
        up = hv; 
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
    shakerSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}