#include <stdio.h>
#include <stdlib.h>
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
    printf("%d", k);
    return 0;
}