#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Bieu dien mang cua mot so nguyen co dang A[t- 1], A[t - 2], ... , A[0]
void Cong(int a[], int b[], int t, int W, int p)
{
    int epsilon = 0;
    int z[t];
    int module = pow(2, W);
    for (int j = 1; j <= t; j++)
    {
        int x = a[t - j] + b[t - j];
        z[t - j] = (x + epsilon) % module;
        if (x > module || x < 0)
            epsilon = 1;
        else
            epsilon = 0;
    }
    printf("Bieu dien qua mang c = a + b trong F_%llu voi W = %d la: (%d, (", p, W, epsilon);
    for (int i = 0; i < t; i++)
    {
        if (i != t - 1)
            printf("%d, ", z[i]);
        else
            printf("%d ))", z[i]);
    }
}
void Tru(int a[], int b[], int t, int W, int p){
    int epsilon = 0;
    int z[t];
    int module = pow(2, W);
    for (int j = 1; j <= t; j++)
    {
        int x = a[t - j] - b[t - j];
        z[t - j] = (x - epsilon) % module;
        if (z[t - j] < 0) z[t-j] += module;
        if (x > module || x < 0)
            epsilon = 1;
        else
            epsilon = 0;
    }
    printf("Bieu dien qua mang c = a - b trong F_%llu voi W = %d la: (%d, (", p, W, epsilon);
    for (int i = 0; i < t; i++)
    {
        if (i != t - 1)
            printf("%d, ", z[i]);
        else
            printf("%d ))", z[i]);
    }
}
void Nhan(int a[], int b[], int t, int W, int p){
    int z[2*t];
    for (int i = 0; i < t; i++){
        z[i] = 0;
    }
    unsigned long pow_of_2 = pow(2,15);
    for(int i = 0; i < t ; i++){
        int u = 0, v = 0;

        for (int j = 0; j < t; j++){
            unsigned long uv = a[t - i - 1]*b[t - i - 1 - j] + z[i] + u;
            unsigned long clone = pow_of_2;
            for (int k = 0; k < 8; k++){        // Tinh toan 8 bit dau va 8 bit sau cua uv
                u += ((int)uv/pow_of_2)*pow_of_2;
                pow_of_2 /= 2;
                uv -= u;
            }
            v = uv;
            z[i + j] = v;
        }
        z[i + t] = u;
    }
    printf("Bieu dien qua mang c = a - b trong F_%llu voi W = %d la: (", p, W);
    for (int i = 0; i < 2*t; i++)
    {
        if (i != t - 1)
            printf("%d, ", z[i]);
        else
            printf("%d ))", z[i]);
    }
}
int main()
{
    unsigned long long a, p;
    int W, m, t;
    printf("Nhap W: ");
    scanf("%d", &W);
    printf("Nhap p: ");
    scanf("%llu", &p);
    m = round(log2(p));
    t = ceil((float)m / W);
    int x[t], y[t];
    printf("Nhap bieu dien mang cua a: \n");
    for (int i = 0; i < t; i++)
    {
        scanf("%d", &x[i]);
    }
    printf("Nhap bieu dien mang cua b: \n");
    for (int i = 0; i < t; i++)
    {
        scanf("%d", &y[i]);
    }
    int choose = -1;
    while (choose != 0)
    {
        printf("Nhap lua chon cua ban: \n");
        printf("0.Thoat\n1. Cong\n2. Tru\n3. Nhan\n4. Chia\n5. Binh phuong\n6. Phep lay modulo\n");
        printf("Nhap lua chon cua ban: ");
        scanf("%d", &choose);
        switch (choose)
        {
        case 1:
            Cong(x, y, t, W, p);
            break;
        case 2:
            Tru(x,y,t, W, p);
            break;
        case 3:
            Nhan(x, y, W, t, p);
            break;
        case 4:
            break;
        case 5:
            break;
        default:
            break;
        }
    }

    return 1;
}