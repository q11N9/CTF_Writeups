#include <stdio.h>
#include <stdlib.h>
int isQPrime(int x){
    int uoc = 2;
    for(int i = 2; i < x; i++){
        if (x%i == 0) uoc++;
        if (uoc > 4) return 0;
    }
    return uoc == 4;
}
int main()
{
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);
    if ( n < 6) printf("Khong co so Q-prime nao!");
    else{
        printf("Cac so Q-prime be hon hoac bang n la: \n");
        int xuongdong = 0;
        for(int i = 6; i <= n; i++ ){
            if(isQPrime(i)){
                xuongdong++;
                printf("%-5d", i);
            }
            if (xuongdong == 5){
                xuongdong = 0;
                printf("\n");
            }
        }
    }
    return 0;
}
