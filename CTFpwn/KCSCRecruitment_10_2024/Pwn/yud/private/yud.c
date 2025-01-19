#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#include<string.h>
#include <stdint.h>


void setup()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

char* hexlify(const char* bytes, const size_t numBytes) {
    // first of all, allocate the new string
    // a hexadecimal representation works like "every byte will be represented by two chars"
    // additionally, we need to null-terminate the string
    char* hexlified = (char*) calloc((2 * numBytes + 1), sizeof(char));

    for (size_t i = 0; i < numBytes; i++) {
        char buffer[3];
        sprintf(buffer, "%02x", (unsigned char) bytes[i]);
        strcat(hexlified, buffer);
    }

    return hexlified;
}

char key[8];

void gen_key()
{
    srand(time(0));
    for(int i = 0; i < 8; i++)
        key[i] = (char)rand();
}

void gen_key2()
{
    int fd;
    fd = open("/dev/urandom", O_RDONLY);
    if(fd < 0)
    {
        puts("[-]Cannot open file");
        exit(-1);
    }
    read(fd, key, 8);
    close(fd);
}

void encode_func(char in[], char out[], size_t n)
{
    for(int i = 0; i < n; i++)
        out[i] = in[i] ^ key[i % 8];
}

void win()
{
    system("cat flag");
}

int get_choice()
{
    char buf[0x10];
    int n;
    puts("1. Set data");
    puts("2. Get data");
    puts("3. Exit");
    printf(">> ");
    n = read(0, buf, sizeof(buf));
    if(buf[n - 1] == '\n')
        buf[n - 1] = '\0';
    return atoi(buf);
}
int main()
{
    setup();
    gen_key2();
    //encode = hexlify(key, 8);
    //puts(encode);
    //puts(hexlify(key, 8));
    int len;
    char data[0x100], encode[0x100];
    while(1)
    {
        int choice = get_choice();
        switch (choice)
        {
        case 1:
            printf("Length: ");
            scanf("%d", &len);
            if((short)len >= 0x100)
            {
                puts("Invalid length");
                break;
            }
            printf("Data: ");
            len = read(0, data, len);
            encode_func(data, encode, len);
            puts("Done!");
            break;
        case 2:
            write(1, data, len);
            break;
        case 3:
            goto exit;
        default:
            puts("Invalid choice!");
            break;
        }
    }
exit:
    return 0;
}