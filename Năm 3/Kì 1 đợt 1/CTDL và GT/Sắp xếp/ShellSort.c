#include <stdio.h>
#include <stdlib.h>
int* generateGaps(int n, int* size){
    int k = 0;
    int* gaps = NULL;
    while (n > 1)
    {
        n /= 2;
        gaps = (int*)realloc(gaps, (k + 1) * sizeof(int));
        if (gaps == NULL) {
            perror("Realloc failed");
            exit(EXIT_FAILURE);
        }
        gaps[k++] = n;
    }
    if (gaps[k-1] != 1) {
        gaps = (int*)realloc(gaps, (k + 1) * sizeof(int));
        if (gaps == NULL) {
            perror("Realloc failed");
            exit(EXIT_FAILURE);
        }
        gaps[k++] = 1;
    }
    *size = k;
    return gaps;
    
}
void shellSort(int arr[], int n){
    int h_size;
    int* h = generateGaps(n, &h_size);
    for (int i = 0; i < h_size; i++)
    {
        int gap = h[i];
        for (int j = gap; j < n; j++)
        {
            int temp = arr[j];
            int k = j;
            while (k >= h[i] && arr[k - gap] > temp)
            {
                int x = arr[k];
                arr[k] = arr[k - gap];
                arr[k - gap] = x;
                k = k - gap;
            }  
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
    shellSort(arr, n);
    printf("Mang sau khi da sap xep la: " );
    for (int i = 0; i < n; i++)
    {
        printf("%d   ", arr[i]);
    }
    return 0;
}