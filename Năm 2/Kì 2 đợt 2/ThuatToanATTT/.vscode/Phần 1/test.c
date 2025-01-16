#include<stdio.h>
#include<math.h>
int nhanBinhPhuong(int a, int k, int n){
    int b = 1;
    if (k == 0){
        return b;
    }
    int temp_k = k;
    int bin_k[32];
    int i = 0;
    while (temp_k >0)
    {
        bin_k[i] = temp_k % 2;
        temp_k = temp_k / 2;
        i++;
    }
    int len = 0;
    if (bin_k[len] == 0){
        b = a;
    } 
    for (len; len <= i; len++)
    {
        a = (a*a) % n;
        if (bin_k[len] == 1){
            b = (a*b) % n;
        } 
    }
    return b; 
}
int main(){
    int x, y, z; //x + 2y + 5z = 20
    printf("Cac bo tien 1000, 2000, 5000 thoa man la: \n");
    for (x = 0; x <= 20; x++){
        for(y = 0; y <= 10; y++){
            for (z = 0; z <= 4; z++){
                if (x + 2*y + 5*z == 20){
                    printf("[%d, %d, %d]     ", &x, &y, &z);
                }
            }
        }
    }
    return 0;
}