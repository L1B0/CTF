# Reversing-Kr HateIntel Writeup

> [题目及脚本]( https://github.com/L1B0/CTF/tree/master/Reversing-Kr/HateIntel)
>
> 调了一天的Twist1没调出来，我好菜。
>
> 刚看到这题也挺多人做的就下下来看了看，发现之前好像见过。。。
>
> （好像去信工所ctf机试的时候有道re和这题一模一样，就数据改了

## 解题思路

题目是一个mach架构的文件，通过ida32位可以打开。

程序逻辑非常简单，输入key，经过加密函数后与一串数据进行比较，相同输出`Correct Key!`。

主函数伪码如下

```c++
int sub_2224()
{
  char input; // [sp+4h] [bp-5Ch]
  int round; // [sp+54h] [bp-Ch]
  int v3; // [sp+58h] [bp-8h]
  int i; // [sp+5Ch] [bp-4h]
  char vars0; // [sp+60h] [bp+0h]

  round = 4;
  printf("Input key : ");
  scanf("%s", &input);
  v3 = strlen(&input);
  encrypt((signed __int32)&input, round);
  for ( i = 0; i < v3; ++i )
  {
    if ( *(&vars0 + i - 92) != data[i] )
    {
      puts("Wrong Key! ");
      return 0;
    }
  }
  puts("Correct Key! ");
  return 0;
}
```

encrypt函数伪码如下，key就是经过了4轮的循环左移变换。

```c++
signed __int32 __fastcall encrypt(signed __int32 result, int a2)
{
  int round; // [sp+0h] [bp-14h]
  char *v3; // [sp+4h] [bp-10h]
  int i; // [sp+8h] [bp-Ch]
  signed __int32 j; // [sp+Ch] [bp-8h]

  v3 = (char *)result;
  round = a2;
  for ( i = 0; i < round; ++i )
  {
    for ( j = 0; ; ++j )                        // for j in range(len(input))
    {
      result = strlen(v3);
      if ( result <= j )
        break;
      v3[j] = cycle_left(v3[j], 1);
    }
  }
  return result;
}
```

cycle_left函数伪码如下

```c++
int __fastcall cycle_left(unsigned __int8 a1, int a2)
{
  int v3; // [sp+8h] [bp-8h]
  int i; // [sp+Ch] [bp-4h]

  v3 = a1;
  for ( i = 0; i < a2; ++i )
  {
    v3 *= 2;
    if ( v3 & 0x100 ) // 大于等于0x100即256时，加一
      v3 |= 1u;
  }
  return (unsigned __int8)v3; // 返回值&0xff，控制在0-256之间
}
```

## 解题脚本

```python
data = [0x44, 0xF6, 0xF5, 0x57, 0xF5, 0xC6, 0x96, 0xB6, 0x56, 0xF5,
  0x14, 0x25, 0xD4, 0xF5, 0x96, 0xE6, 0x37, 0x47, 0x27, 0x57,
  0x36, 0x47, 0x96, 0x03, 0xE6, 0xF3, 0xA3, 0x92]
flag = [ ((i&0xf)<<4)+(i>>4) for i in data]
print ''.join(map(chr,flag)
```

