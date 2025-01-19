The program gives us a binary file with the **main()** function as follows:

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  unsigned int seed; // eax
  int bank_limit; // [rsp+8h] [rbp-18h] BYREF
  int bet_amount; // [rsp+Ch] [rbp-14h] BYREF
  __gid_t rgid; // [rsp+10h] [rbp-10h]
  int v7; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v8; // [rsp+18h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  rgid = getegid();
  setresgid(rgid, rgid, rgid);
  seed = time(0LL);
  srand(seed);
  setup_alarm(180LL);
  bank_limit = 100;
  puts("Welcome to the Rigged Slot Machine!");
  puts("You start with $100. Can you beat the odds?");
  while ( 1 )
  {
    while ( 1 )
    {
      bet_amount = 0;
      printf("\nEnter your bet amount (up to $%d per spin): ", 100LL);
      v7 = __isoc99_scanf("%d", &bet_amount);
      if ( v7 == 1 )
        break;
      puts("Invalid input! Please enter a numeric value.");
      clear_input();
    }
    if ( bet_amount > 0 && bet_amount <= 100 )
    {
      if ( bet_amount <= bank_limit )
      {
        play((unsigned int)bet_amount, &bank_limit);
        if ( bank_limit > 133742 )
          payout(&bank_limit);
      }
      else
      {
        printf("You cannot bet more than your current balance of $%d!\n", (unsigned int)bank_limit);
      }
    }
    else
    {
      printf("Invalid bet amount! Please bet an amount between $1 and $%d.\n", 100LL);
    }
  }
}
```

We have a fixed amount of money 100 at the start, and bet an amount between [1, 100]. It will spin and the multiplier will depend on that to calculate whether we lose or win:

```c
unsigned __int64 __fastcall play(int a1, unsigned int *a2)
{
  int v3; // [rsp+1Ch] [rbp-14h]
  int v4; // [rsp+20h] [rbp-10h]
  int v5; // [rsp+24h] [rbp-Ch]
  unsigned __int64 v6; // [rsp+28h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  v4 = rand() % 100;
  if ( v4 )
  {
    if ( v4 > 9 )
    {
      if ( v4 > 14 )
      {
        if ( v4 > 19 )
          v3 = v4 <= 29;
        else
          v3 = 2;
      }
      else
      {
        v3 = 3;
      }
    }
    else
    {
      v3 = 5;
    }
  }
  else
  {
    v3 = 100;
  }
  v5 = v3 * a1 - a1;
  if ( v5 <= 0 )
  {
    if ( v5 >= 0 )
      puts("No win, no loss this time.");
    else
      printf("You lost $%d.\n", (unsigned int)(a1 - v3 * a1));
  }
  else
  {
    printf("You won $%d!\n", (unsigned int)v5);
  }
  *a2 += v5;
  printf("Current Balance: $%d\n", *a2);
  if ( (int)*a2 <= 0 )
  {
    puts("You're out of money! Game over!");
    exit(0);
  }
  return v6 - __readfsqword(0x28u);
}
```
And if our bank is greater than 133742, we will have a flag. In this article, I think about setting the time to match **srand(time(Null))** on the server, then send the bet amount.
although it is an easy challenge, but i've not solved it =w=. 
