We got a binary file. Decompile it: 

![image](https://hackmd.io/_uploads/H14JWnyH1l.png)

Get into the `calc()`: 

```c
unsigned int calc()
{
  int count[101]; // [esp+18h] [ebp-5A0h] BYREF
  char s[1024]; // [esp+1ACh] [ebp-40Ch] BYREF
  unsigned int v3; // [esp+5ACh] [ebp-Ch]

  v3 = __readgsdword(0x14u);
  while ( 1 )
  {
    bzero(s, 1024);
    if ( !get_expr((int)s, 1024) )
      break;
    init_pool(count);
    if ( parse_expr((int)s, count) )
    {
      printf("%d\n", count[count[0]]);
      fflush(stdout);
    }
  }
  return __readgsdword(0x14u) ^ v3;
}
```

We get some function here: `get_expr()`, `init_pool()` and `parse_expr()`.
Let's go for the first one:

```c
int __cdecl get_expr(char *str, int length)
{
  int v2; // eax
  char input; // [esp+1Bh] [ebp-Dh] BYREF
  int v5; // [esp+1Ch] [ebp-Ch]

  v5 = 0;
  while ( v5 < length && read(0, (int)&input, 1) != -1 && input != 10 )
  {
    if ( input == '+' || input == '-' || input == '*' || input == '/' || input == '%' || input > '/' && input <= '9' )
    {
      v2 = v5++;
      str[v2] = input;
    }
  }
  str[v5] = 0;
  return v5;
}
```

It reads maximum `1024` bytes from input, only allow numbers and operations then saved it into our `str` or `s` in `calc()` function .
Next, it calls `init_pool()`, take a array `count` with 101 elements as parameter: 

```c
int *__cdecl init_pool(int *a1)
{
  int *result; // eax
  int i; // [esp+Ch] [ebp-4h]

  result = a1;
  *a1 = 0;
  for ( i = 0; i <= 99; ++i )
  {
    result = a1;
    a1[i + 1] = 0;
  }
  return result;
}
```

It inits 100 value 0 for the array. But if we see where is the `count()` array: 

![image](https://hackmd.io/_uploads/r1859Ngrkx.png)

it's right above some variable. But we'll talk about it later. 
If initialized successfull, it checks a condition with return value of `parse_expr()`:

```c
int __cdecl parse_expr(int expr, int *count)
{
  int v3; // eax
  _BYTE *v4; // [esp+20h] [ebp-88h]
  int i; // [esp+24h] [ebp-84h]
  int j; // [esp+28h] [ebp-80h]
  int v7; // [esp+2Ch] [ebp-7Ch]
  char *s1; // [esp+30h] [ebp-78h]
  int v9; // [esp+34h] [ebp-74h]
  char s[100]; // [esp+38h] [ebp-70h] BYREF
  unsigned int v11; // [esp+9Ch] [ebp-Ch]

  v11 = __readgsdword(0x14u);
  v4 = (_BYTE *)expr;
  j = 0;
  bzero(s, 100);
  for ( i = 0; ; ++i )
  {
    if ( *(char *)(i + expr) - (unsigned int)'0' > 9 )
    {
      v7 = i + expr - (_DWORD)v4;
      s1 = (char *)malloc(v7 + 1);
      memcpy(s1, v4, v7);
      s1[v7] = 0;
      if ( !strcmp(s1, &zeroCheck) )
      {
        puts("prevent division by zero");
        fflush(stdout);
        return 0;
      }
      v9 = atoi(s1);
      if ( v9 > 0 )
      {
        v3 = (*count)++;
        count[v3 + 1] = v9;
      }
      if ( *(_BYTE *)(i + expr) && (unsigned int)(*(char *)(i + 1 + expr) - 48) > 9 )
      {
        puts("expression error!");
        fflush(stdout);
        return 0;
      }
      v4 = (_BYTE *)(i + 1 + expr);
      if ( s[j] )
      {
        switch ( *(_BYTE *)(i + expr) )
        {
          case '%':
          case '*':
          case '/':
            if ( s[j] != '+' && s[j] != '-' )
              goto LABEL_14;
            s[++j] = *(_BYTE *)(i + expr);
            break;
          case '+':
          case '-':
LABEL_14:
            eval(count, s[j]);
            s[j] = *(_BYTE *)(i + expr);
            break;
          default:
            eval(count, s[j--]);
            break;
        }
      }
      else
      {
        s[j] = *(_BYTE *)(i + expr);
      }
      if ( !*(_BYTE *)(i + expr) )
        break;
    }
  }
  while ( j >= 0 )
    eval(count, s[j--]);
  return 1;
}
```

It set 0 for a 100-char string, then checks if our input has any operation:

![image](https://hackmd.io/_uploads/r1_diVgHyx.png)

If exists, it calculates the length of string to that operation, malloc a chunk then copy all things from our input to that operation into a chunk: 

![image](https://hackmd.io/_uploads/SyO6j4lrke.png)

![image](https://hackmd.io/_uploads/BkmCsVgH1x.png)

And it also does not allow 0 before any operations. Then it converts that data in the chunk into integer, then saves it into `count` array: 

![image](https://hackmd.io/_uploads/B1aL2EgSJe.png)

Then it will checks if there is any operation after a operation, the program will exit if our input contains like this: `++`

![image](https://hackmd.io/_uploads/S1ui2Elrye.png)

Next, it uses `v4` to save the next char after the operation

![image](https://hackmd.io/_uploads/HJJ76NxSJx.png)

For the condition, it checks the `s[j]` was zero or not. If it's not null, it will execute a switch-case. Otherwise, it saves the recent operation into it: 

![image](https://hackmd.io/_uploads/H1xhTNeHke.png)

For switch-case: It will call `eval`. Before that, it will check the value in `expr[i]` is a operation or not. 
`eval()` function: 
```c
int *__cdecl eval(int *count, char operation)
{
  int *result; // eax

  if ( operation == '+' )
  {
    count[*count - 1] += count[*count];
  }
  else if ( operation > 43 )
  {
    if ( operation == '-' )
    {
      count[*count - 1] -= count[*count];
    }
    else if ( operation == '/' )
    {
      count[*count - 1] /= count[*count];
    }
  }
  else if ( operation == '*' )
  {
    count[*count - 1] *= count[*count];
  }
  result = count;
  --*count;
  return result;
}
```
It is just calculate between `count[i - 1]` and `count[i]` and then saved it to `count[i - 1]`. Then return the `count[i]`
But you remember `var_59C` before? Because it initialize the `count`, it will change that array too. And this code in `parse_expr()`

![image](https://hackmd.io/_uploads/HJJeGrlrke.png)

Showed that the `count` array is actually worked from index 1, or index 0 of `var_59C`. So we can call `var_59C` as `Number` array. After changes, you can see the different in `calc()` function: 

![image](https://hackmd.io/_uploads/r1dozrgrkx.png)

So what do we do now? It seems like there's no bug overflow or anything. Buttt

![image](https://hackmd.io/_uploads/HJ_e4Bgrke.png)

This code in `parse_expr()` get an error. Because there is no check if expression starts with operation. If it happens, like `+5`, then what will it do? 

![image](https://hackmd.io/_uploads/ryWi9Hxr1l.png)

It returns 0. And more example: 

![image](https://hackmd.io/_uploads/B1335HlBJg.png)

Let's analyze the flow code here. First with `+5`, it pass the condition check operation, because there is no character before the operation, then `s1` will be 0. `v9` is either. 

![image](https://hackmd.io/_uploads/HyfmiBxHye.png)

Then `v4` will contains `5`. Next, it saves `+` to `s[j]` then call `eval()`. Because it will calculate `count[*count-1] += count[*count]`, it is the same as `Number[count-2] += Number[count-1]`, then it reduces `count`. So the result will be saved in `Number[count-1]`. So if we add `+5+6`, it can change the value in `Number[count-1]`, and also change `count[count]`. 
But i'm struggling with understanding the payload while reading writeups. For more information, you can read [here](https://github.com/johnathanhuutri/CTFWriteup/blob/master/online/pwnable.tw/calc/solve.py) 
