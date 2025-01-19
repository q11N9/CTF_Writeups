We get libc 2.23 and binary file. Checksec: 

![image](https://hackmd.io/_uploads/H12oON5ryg.png)

FullRO, so we cannot overwrite .got. And static binary address. 
Decompile binary file:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  int boss_hp; // [esp+0h] [ebp-3Ch] BYREF
  const char *boss_name; // [esp+4h] [ebp-38h]
  char bullet[48]; // [esp+8h] [ebp-34h] BYREF
  int v8; // [esp+38h] [ebp-4h]

  init_proc();
  v8 = 0;
  memset(bullet, 0, sizeof(bullet));
  boss_hp = 2147483647;
  boss_name = "Gin";
  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        while ( 1 )
        {
          menu(boss_hp, boss_name);
          v3 = read_int();
          if ( v3 != 2 )
            break;
          power_up(bullet);
        }
        if ( v3 > 2 )
          break;
        if ( v3 != 1 )
          goto LABEL_15;
        create_bullet(bullet);
      }
      if ( v3 == 3 )
        break;
      if ( v3 == 4 )
      {
        puts("Don't give up !");
        exit(0);
      }
LABEL_15:
      puts("Invalid choice");
    }
    if ( beat(bullet, &boss_hp) )
      return 0;
    puts("Give me more power !!");
  }
}
```
We got a boss fighting program, with powering bullet. 
`create_bullet`:
```c
int __cdecl create_bullet(Bullet *bullet)
{
  int power; // [esp+0h] [ebp-4h]

  if ( bullet->name[0] )
    return puts("You have been created the Bullet !");
  printf("Give me your description of bullet :");
  read_input(bullet, 48);
  power = strlen(bullet);
  printf("Your power is : %u\n", power);
  bullet->power = power;
  return puts("Good luck !!");
}
```
Struct `Bullet`: 

![image](https://hackmd.io/_uploads/rkTo5NcHkx.png)

So it will read our input, also nulldify the last byte 

![image](https://hackmd.io/_uploads/ByH09N5S1l.png)

And it takes `strlen` of our description as power. 

`power_up()`
```c
int __cdecl power_up(Bullet *bullet)
{
  char v2[48]; // [esp+0h] [ebp-34h] BYREF
  int v3; // [esp+30h] [ebp-4h]

  v3 = 0;
  memset(v2, 0, sizeof(v2));
  if ( !bullet->name[0] )
    return puts("You need create the bullet first !");
  if ( bullet->power > 47u )
    return puts("You can't power up any more !");
  printf("Give me your another description of bullet :");
  read_input(v2, 48 - bullet->power);
  strncat(bullet, v2, 48 - bullet->power);
  v3 = strlen(v2) + bullet->power;
  printf("Your new power is : %u\n", v3);
  bullet->power = v3;
  return puts("Enjoy it !");
}
```
It limits our `bullet->power` under 48, and plus new strlen using `strncat`. But `strncat` put a terminating null character at the end. 

![image](https://hackmd.io/_uploads/HJk5XdjSJl.png)

So if we first create a bullet with 47 power, and power 1 more, it will overflow null byte to `bullet->power`, then it count the length of new input string, which is 1, plus with current `bullet->power`, which is 0. So the `bullet->power` is now 0. We can overflow more data from that!
`beat()` function:
```c
int __cdecl beat(Bullet *bullet, Wolf *wolf)
{
  if ( bullet->name[0] )
  {
    puts(">----------- Werewolf -----------<");
    printf(" + NAME : %s\n", wolf->name);
    printf(" + HP : %d\n", wolf->power);
    puts(">--------------------------------<");
    puts("Try to beat it .....");
    usleep(1000000);
    wolf->power -= bullet->power;
    if ( wolf->power <= 0 )
    {
      puts("Oh ! You win !!");
      return 1;
    }
    else
    {
      puts("Sorry ... It still alive !!");
      return 0;
    }
  }
  else
  {
    puts("You need create the bullet first !");
    return 0;
  }
}
```
It subtracts `wolf->power` with `bullet->power`. Nothing special in here. 
Because we got overflow bug, we can change the return address of puts.got to puts.plt to leak the libc. 

![image](https://hackmd.io/_uploads/BJ8ZYdoSke.png)

Now our power is enough to beat the werewolf. After powerup, our stack will be like this 

![image](https://hackmd.io/_uploads/BJBH3_sryx.png)

`main` is the return address of `puts`, next is the parameter of `puts`. 
To get shell, we just need to change `main` to exit, puts.plt to `system` and `puts.got` to `sh`'s address

![image](https://hackmd.io/_uploads/SyuspOjrye.png)

Script: [solve.py](https://github.com/q11N9/CTF_Writeups/new/main/CTFpwn/pwnable.tw/SilverBullet/solve.py)
