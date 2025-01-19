#include <stdio.h>
#include <stdlib.h>
void init(){
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}
int main()
{
    init();
    char a[0x50];
    read(0,&a,0x50);
    printf(a);
}