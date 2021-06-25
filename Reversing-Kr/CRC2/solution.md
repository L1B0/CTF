# reversing-kr-CRC2

aaaaaaaaaaWWX

## check_length == 13

![2144_1](https://i.loli.net/2021/06/24/ZXo85Jvz9WEBTNO.png)

## check_input_type

输入为数字+大小写字母
![2146_1](https://i.loli.net/2021/06/24/TtLVDSF94fE8gqO.png)

## check_input_sum == 0x4D0

![2148_1](https://i.loli.net/2021/06/24/OBpxnm6C4bRadcA.png)

![2150_1](https://i.loli.net/2021/06/24/H8aAMdtqg6GmbnU.png)

## check

输入被嵌入一个key_map中。从0开始，每20个字节放入一个。
![2158_1](https://i.loli.net/2021/06/24/SkfZqR2a1n8KzsE.png)

接下来进行crc32计算，循环0x100次。
每次首先从key_map取下标为i的值，然后放入sub_4F12D0.
![2160_1](https://i.loli.net/2021/06/24/P9ODxhdJLwEK5iQ.png)

![2162_1](https://i.loli.net/2021/06/24/YThnJACxRvy2Iw8.png)

![2164_1](https://i.loli.net/2021/06/24/hlI1D9O8xsHzM6r.png)

![2166_1](https://i.loli.net/2021/06/24/29yEYPUm81lWkHv.png)

分析一下sub_4F12D0会发现它就是个异或。。。

```c
// a1 low 32bits
// a2 high 32bits
// a3 64bits
unsigned int __cdecl xor(unsigned int a1, unsigned int a2, __int64 a3)
{
  unsigned int a3_low; // ebx
  unsigned int esii; // edi
  unsigned int edii; // edx
  unsigned int bit_high; // esi
  unsigned int bit_low; // ecx
  unsigned int v8; // edi
  unsigned int v9; // ebx
  unsigned __int64 v10; // rax
  char *v11; // esi
  char edi_bit[64]; // [esp+10h] [ebp-188h]
  char a3_bit[64]; // [esp+50h] [ebp-148h]
  char edi_bit_reflect[64]; // [esp+90h] [ebp-108h]
  char v16[64]; // [esp+D0h] [ebp-C8h]
  char v17[64]; // [esp+110h] [ebp-88h]
  char a3_bit_reflect[64]; // [esp+150h] [ebp-48h]
  __int64 v19; // [esp+190h] [ebp-8h]
  unsigned int v20; // [esp+1A4h] [ebp+Ch]

  a3_low = a3;
  esii = a2;                                    // esi 高位
  edii = a1;                                    // edi 低位
  bit_high = 0;
  bit_low = 0;
  v20 = HIDWORD(a3);
  v19 = 0i64;
  do
  {
    if ( edii & 1 )
    {
      if ( bit_high || bit_low >= 0x40 )
      {
LABEL_31:
        __report_rangecheckfailure(bit_low);
        JUMPOUT(*(_DWORD *)algn_401488);
      }
      edi_bit_reflect[bit_low] = 0;
    }
    else
    {
      edi_bit_reflect[bit_low] = 1;
    }
    edi_bit[bit_low] = edii & 1;
    if ( a3_low & 1 )
    {
      if ( bit_high || bit_low >= 0x40 )
        goto LABEL_31;
      a3_bit_reflect[bit_low] = 0;
    }
    else
    {
      a3_bit_reflect[bit_low] = 1;
    }
    a3_bit[bit_low] = a3_low & 1;
    edii = __PAIR__(esii, edii) >> 1;
    a3_low = __PAIR__(v20, a3_low) >> 1;
    esii >>= 1;
    bit_high = (__PAIR__(bit_high, bit_low++) + 1) >> 32;
    v20 >>= 1;
  }
  while ( __PAIR__(bit_high, bit_low) < 0x40 );
  v8 = HIDWORD(v19);
  v9 = v19;
  v10 = 0i64;
  do
  {
    LOBYTE(bit_low) = edi_bit_reflect[v10];
    if ( (_BYTE)bit_low != a3_bit[v10] || (_BYTE)bit_low != 1 )
    {
      if ( v10 >= 0x40 )
        goto LABEL_31;
      v11 = &v16[v10];
      v16[v10] = 0;
    }
    else                                        // edi_bit_reflect[v10] == a3_bit[v10] == 1
    {
      v11 = &v16[v10];
      v16[v10] = 1;
    }
    LOBYTE(bit_low) = edi_bit[v10];
    if ( (_BYTE)bit_low != a3_bit_reflect[v10] || (_BYTE)bit_low != 1 )
    {
      if ( v10 >= 0x40 )
        goto LABEL_31;
      bit_low = (unsigned int)&v17[v10];
      v17[v10] = 0;
    }
    else                                        // edi_bit[v10] == a3_bit_reflect[v10] == 1
    {
      bit_low = (unsigned int)&v17[v10];
      v17[v10] = 1;
    }
    if ( *v11 == 1 || *(_BYTE *)bit_low == 1 )
      v8 |= 0x80000000;
    if ( v10 < 63 )
    {
      v9 = __PAIR__(v8, v9) >> 1;
      v8 >>= 1;
    }
    ++v10;
  }
  while ( v10 < 64 );
  return v9;
}
```

回到sub_401490。

```c
char __thiscall sub_401490(HANDLE hFile)
{
  int v1; // edi
  unsigned __int64 v2; // rax
  char *v3; // esi
  unsigned int v4; // kr00_4
  unsigned __int64 v5; // rdi
  unsigned int v6; // ebx
  unsigned __int8 v7; // al
  __int64 v8; // ST0A_8
  DWORD NumberOfBytesWritten; // [esp+26h] [ebp-1Ch]
  char v11[2]; // [esp+2Ah] [ebp-18h]
  char v12[18]; // [esp+2Ch] [ebp-16h]

  v1 = 0;
  WriteFile(hFile, "Input: ", 7u, &NumberOfBytesWritten, 0);
  sub_401740("%s", v11, 20);
  if ( &v11[strlen(v11) + 1] - &v11[1] == 13 )  // len(input) == 13
  {
    sub_401000();
    HIDWORD(v2) = 0;
    if ( &v12[strlen(v12) + 1] != &v12[1] )
    {
      v3 = byte_410F00;
      while ( 1 )
      {
        LOBYTE(v2) = v12[HIDWORD(v2)];
        if ( ((char)v2 < 48 || (char)v2 > '9') && ((char)v2 < 65 || (char)v2 > 'Z') && ((char)v2 < 97 || (char)v2 > 'z') )// input[i]
          break;
        LOBYTE(v2) = v12[HIDWORD(v2)];
        *v3 = v2;
        v1 += (char)v2;
        ++HIDWORD(v2);
        v3 += 20;
        v4 = strlen(v12);
        LOBYTE(v2) = v4;
        if ( HIDWORD(v2) >= v4 )
        {
          if ( v1 == 0x4D0 )                    // sum(input) == 0x4D0
          {
            v5 = 0i64;
            v6 = 0;
            do // CRC64
            {
              v7 = xor((unsigned __int8)byte_410F00[v6], 0, v5);// 每次取1个byte,input包含在里面
              HIDWORD(v8) = dword_411024[2 * v7];
              LODWORD(v8) = dword_411020[2 * v7];
              LODWORD(v2) = xor(v5 >> 8, v5 >> 8 >> 32, v8);
              ++v6;
              v5 = v2;
            }
            while ( v6 < 0x100 );
            if ( v2 == 0x81BAD8907DE045EBi64 )
              strcpy(aWrong, "Correct\n");
          }
          return v2;
        }
      }
    }
  }
  return v2;
}
```



## reverse

> CRC(X^Y) == CRC(X)^CRC(Y)



![image-20210624225727998](https://i.loli.net/2021/06/24/z5FQjZqAUBVKpSn.png)

参考后面链接的想法，程序会将flag嵌入一个长度为0x100的数组data里，于是利用crc的特性，将输入拆分为两个，一个是data数组原本（flag所在的位置0），另一个是（flag所在位不为空，其它都置0）。这样我们可以直接得到第一个data数组的crc，与最后比较的crc异或得到另一个数组也就是flag本身的crc。

接着，继续拆分，将flag的每一位（可见字符于是只有7位）独立出来成为一个数组，也就是13（flag长度）*7=91个数组的crc。

此时每一位对于每个数组来说，要么有，要么没有，那么可以抽象为一个长度为91的由0和1组成的数组与91个数组的crc的矩阵运算。

利用sage(见exp.sage)，得到解的27个基向量和1个特解，可以想象最后的解由特解和若干个基向量组成，由于输入需要由字母和数字组成，且和为0x4d0，于是继续爆破27个基向量的取舍，见exp3.c。

```shell
r11t@ubuntu:~/Desktop$ ./exp3
find
SdVaxWoWwJZfL
find
HyieDEHiNzOzv
find
goodRevKrF0rU // flag
find
PzmgIVfjkM5cs
find
6aNfexyvdUBxF
117440512
find
FDniQqtPKmgvT


```

![image-20210625161125348](https://i.loli.net/2021/06/25/MXEzc8uP2dyB7KA.png)

## references

https://int0h.wordpress.com/2009/12/24/the-power-of-wow64/

https://github.com/resilar/crchack

https://github.com/DoubleLabyrinth/reversing.kr/tree/master/CRC2