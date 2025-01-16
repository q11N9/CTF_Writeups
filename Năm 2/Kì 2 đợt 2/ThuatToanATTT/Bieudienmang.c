#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    unsigned long long a,b;
    printf("Nhap a va b: ");
    scanf("%llu %llu", &a, &b);
    printf("a = %llu, b = %llu\n", a, b);
    int W = 8, t = 4, m = 31;
    unsigned long long p = 2147483647;
    int u[t], y[t];
    for (int j = 0; j < t; j++)
    {
        unsigned long long x = pow(2, W *(t - j - 1));
        u[j] = round(a / x);
        y[j] = round(b / x);
        a -= x * u[j];
        b -= x * y[j];
    }
    printf("Bieu dien qua mang a trong F_%llu voi W = %d la: (", p, W);
    for (int j = 0; j < t; j++)
    {
        if (j != t)
            printf("%d, ", u[t]);
        else
            printf("%d)\n", u[t]);
    }

    printf("Bieu dien qua mang b trong F_%llu voi W = %d la: (", p, W);
    for (int j = 0; j < t; j++)
    {
        if (j != t)
            printf("%d, ", y[t]);
        else
            printf("%d)\n", y[t]);
    }
    return 0;
}