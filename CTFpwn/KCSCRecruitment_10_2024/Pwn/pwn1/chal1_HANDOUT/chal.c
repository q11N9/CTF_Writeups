#include<stdio.h>
#include<stdlib.h>

void init(){
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void win(){
    system("/bin/sh");
}
int main()
{
    init();
    char a[0x100];
    gets(a);
}