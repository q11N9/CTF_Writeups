#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int isPrime(unsigned long long x){
    for(unsigned long long i = 2; i*i <= x; i++){
        if (x%i == 0) return 0;
    }
    return 1;  
}
int main(){
    int N;
    printf("Nhap N: ");
    scanf("%d", &N);
    int count = 0;
    for(unsigned long long i = pow(10,N-1); i <= pow(10,N); i++){
        if(isPrime(i)){
            count++;
            printf("%-15llu", i);
        }
        if (count == 5){
            count = 0;

        }
    }

}