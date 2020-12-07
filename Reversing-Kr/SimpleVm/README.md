# Reversing-Kr-SimpleVm writeup

> 题目地址：http://reversing.kr/download.php?n=17
> 这题做了一周，哭了

## 静态分析

题目是一个32位的ELF文件
```
SimpleVM: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, stripped
```
用ida打开瞅瞅发现报错，并且看不到什么有用的东西，于是用gdb跑一下。
![Dvwlvt.png](https://s3.ax1x.com/2020/12/07/Dvwlvt.png)

## 动态调试

> 需要注意的是SimpleVM文件需要用管理员权限（root）运行。

### gdb - dump程序动态加载的代码
start一下，程序停在0xc023DC，就是ida报错的那个入口点。
![Dvwg54.png](https://s3.ax1x.com/2020/12/07/Dvwg54.png)
gdb使用的指令如下
> b *0xc01d27
> c
> b *0xc033cf
> c
> n

在到达0xc033cf后，一直next，会发现到达一个循环。ecx为循环的次数，随着loop指令的执行会减小，这个循环的作用就是给0x80开头的地址内容赋值0。
![Dv0HO0.png](https://s3.ax1x.com/2020/12/07/Dv0HO0.png)
此外在程序执行时可以看到创建了一个新的进程。
> pwndbg> c
Continuing.
Input : [New process 10628]
 
于是将程序直接执行，然后使用gdb attach上相应进程，dump内存。
* 窗口1执行
> sudo ./SimpleVM
* 窗口2执行
> ps -A | grep SimpleVM
> sudo gdb attach pid
> gcore

生成的core文件就可以丢到ida分析了。
在string窗口可以看到`Input`字样，跟进去，查看调用的函数如下，里面的函数和变量名我已经改成有意义的字符串了。
> 如何根据调用的函数地址查询其在so文件里对应的名字？
> https://libc.blukat.me/这个网站可以根据函数地址的后三位及名字（猜一猜）查询到对应的so

sub_8048556函数的大致流程如下
* 首先通过getuid检查是否为root运行
* 然后通过pipe建立两个管道
* 创建管道成功后创建一个子进程，用来与主进程交互（发送和接收消息）

```
// write access to const memory has been detected, the output may be wrong!
void sub_8048556()
{
  char v0; // al
  int v1; // [esp+1Ch] [ebp-3Ch]
  int v2; // [esp+20h] [ebp-38h]
  char v3; // [esp+24h] [ebp-34h]
  int i; // [esp+2Ch] [ebp-2Ch]
  unsigned int v5; // [esp+30h] [ebp-28h]
  char v6; // [esp+36h] [ebp-22h]
  char v7; // [esp+37h] [ebp-21h]
  int v8; // [esp+38h] [ebp-20h]
  int v9; // [esp+3Ch] [ebp-1Ch]
  __int16 v10; // [esp+40h] [ebp-18h]
  int input; // [esp+42h] [ebp-16h]
  int v12; // [esp+46h] [ebp-12h]
  __int16 v13; // [esp+4Ah] [ebp-Eh]
  unsigned int v14; // [esp+4Ch] [ebp-Ch]

  v14 = __readgsdword(0x14u);
  if ( getuid() )                               // Access Denied
  {
    v7 = 0;
    for ( i = 1; i <= 14; ++i )
    {
      v6 = accessDenied[i - 1] ^ i;
      write(1, &v6, 1u);
    }
  }
  else
  {
    write(1, "Input : ", 8u);
    if ( pipe((int)&v1) != -1 && pipe((int)&v3) != -1 )
    {
      v5 = fork();                              // create a child process!
      if ( v5 == -1 )
      {
        v7 = 0;
        for ( i = 1; i <= 6; ++i )
        {
          v6 = error[i - 1] ^ i;                // Error
          write(1, &v6, 1u);
        }
      }
      else if ( v5 )                            // child process
      {
        input = 0;
        v12 = 0;
        v13 = 0;
        read(v1, (int)&input, 9);
        read(v1, (int)&opcode, 200);
        for ( i = 0; i <= 199; ++i )
          *(_BYTE *)(i + 0x804B0A0) ^= 0x20u;
        opcode = input;                         // opcode[:8] = input[:]
        dword_804B0A4 = v12;
        for ( i = 0; i <= 199; ++i )
          *(_BYTE *)(i + 0x804B0A0) ^= 0x10u;
        if ( sub_8048C6D() == 1 )               // Wrong
        {
          v7 = 0;
          for ( i = 1; i <= 6; ++i )
          {
            v6 = *((_BYTE *)&Wrong + i - 1) ^ i;
            write(1, &v6, 1u);
          }
        }
        else
        {
          v7 = 0;
          for ( i = 1; i <= 6; ++i )
          {
            v6 = *((_BYTE *)&Wrong + i - 1) ^ i;
            write(1, &v6, 1u);
          }
        }
      }
      else                                      // parent process
      {
        v8 = 0;
        v9 = 0;
        v10 = 0;
        read(0, (int)&v8, 10);
        if ( (_BYTE)v10 )
        {
          v7 = 0;
          for ( i = 1; i <= 6; ++i )
          {
            v6 = *((_BYTE *)&Wrong + i - 1) ^ i;
            write(1, &v6, 1u);
          }
        }
        else
        {
          write(v2, &v8, 9u);
          for ( i = 0; i <= 199; ++i )
          {
            v0 = sub_80489AA(*(unsigned __int8 *)(i + 0x804B0A0), 3);
            *(_BYTE *)(i + 0x804B0A0) = v0;
          }
          sub_8048410();
          write(v2, &opcode, 0xC8u);
        }
      }
    }
    else
    {
      v7 = 0;
      for ( i = 1; i <= 6; ++i )
      {
        v6 = error[i - 1] ^ i;
        write(1, &v6, 1u);
      }
    }
  }
  if ( __readgsdword(0x14u) != v14 )
    sub_8048420();
}
```

### ida调试-dump opcode内容

可以看到函数sub_8048556有这么一行代码`read(v1, (int)&opcode, 200);`，这个opcode的内容我通过ida调试获得。
![Dvcy4K.png](https://s3.ax1x.com/2020/12/07/Dvcy4K.png)

###  vm算法分析

vm的算法位于sub_8048C6D函数，这里分析需要结合伪代码（辅助）和汇编指令（主要）一起。

输入input的长度为8，但是实际只用了前7位。
关键在case 6和case 7，其中case 6进行了一个异或加密，case 7对输入异或后的结果进行校验。
所以将这两步的结果输出出来，就可以进行逆向得到flag了。

```
opcode = [

    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x45, 

  0x45, 0xC4, 0xC4, 0x04, 0x04, 0x65, 0x44, 0xE4, 0x08, 0xC4, 

  0x04, 0xE4, 0x44, 0xE4, 0x25, 0xE4, 0x04, 0xE4, 0x25, 0x44, 

  0x44, 0xE4, 0xC8, 0xC4, 0x24, 0xE4, 0x44, 0xE4, 0x44, 0xE4, 

  0x24, 0xE4, 0x25, 0x44, 0x44, 0xE4, 0xA6, 0xC4, 0x44, 0xE4, 

  0x44, 0xE4, 0xC0, 0xE4, 0x44, 0xE4, 0x25, 0x44, 0x44, 0xE4, 

  0xE4, 0xC4, 0x64, 0xE4, 0x44, 0xE4, 0xA1, 0xE4, 0x64, 0xE4, 

  0x25, 0x44, 0x44, 0xE4, 0x8D, 0xC4, 0x84, 0xE4, 0x44, 0xE4, 

  0x40, 0xE4, 0x84, 0xE4, 0x25, 0x44, 0x44, 0xE4, 0x68, 0xC4, 

  0xA4, 0xE4, 0x44, 0xE4, 0xE4, 0xE4, 0xA4, 0xE4, 0x25, 0x44, 

  0x44, 0xE4, 0x0B, 0xC4, 0xC4, 0xE4, 0x44, 0xE4, 0x06, 0xE4, 

  0xC4, 0xE4, 0x25, 0x44, 0x44, 0x04, 0x24, 0x65, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 

  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04

    ]

dword_804B18c, dword_804B190, dword_804B194, dword_804B198, dword_804B19c = 0,0,0,0,0

def string_decode(a):
    #a = 
[0x40,0x61,0x60,0x61,0x76,0x75,0x27,0x4C,0x6C,0x64,0x62,0x69,0x69,0x0440,0x61,0x60,0x61,0x76,0x75,0x27,0x4C,0x6C,0x64,0x62,0x69,0x69,0x04]
    a = [ (i+1)^a[i] for i in range(len(a))]
    #print(a)
    a = ''.join(map(chr,a))
    print(a)
    
def opcode_init(input):

    global opcode

    # sub_80489AA 

    opcode = [ (((i<<3)&0xff)|(i>>5)) for i in opcode ]

    #print(opcode)



    opcode = [ i^0x20 for i in opcode]

    opcode[:8] = input

    #opcode = [ i for i in opcode]

    print(opcode)



def sub_8048a48():



    global opcode, dword_804B190

    

    # opcode[9] is the index

    # dword_804B190 is the opcode[index] and then index ++

    dword_804B190 = opcode[(opcode[9])]

    opcode[9] = ((opcode[9])+1)

    

def vm():



    global opcode, dword_804B18c, dword_804B190, dword_804B194, dword_804B198, 
dword_804B19c

    

    while 1:

        sub_8048a48()

        print("dword_804B190 = %d"%dword_804B190)

        #print("opcode[9] = %d"%opcode[9])

        #print(opcode)

        if dword_804B190 == 2:

            # i = opcode[9]

            # opcode[opcode[i]] = opcode[i+1]

            sub_8048a48()

            dword_804B198 = dword_804B190

            sub_8048a48()

            dword_804B194 = dword_804B190



            opcode[dword_804B198] = dword_804B194

            print("opcode[%d] = %d"%(dword_804B190,dword_804B198))

            

        elif dword_804B190 == 6:

            # i = opcode[9]

            # opcode[opcode[i]] = opcode[opcode[i]]^opcode[opcode[i+1]]

          

            sub_8048a48()

            dword_804B18c = dword_804B190



            sub_8048a48()

            #dword_804B194 = opcode[dword_804B190] # 0-'a' 7

            #dword_804B190 = opcode[dword_804B18c]

            dword_804B198 = opcode[dword_804B18c]^opcode[dword_804B190]

print("opcode[%d]^opcode[%d]=%d^%d=%d"%(dword_804B18c,dword_804B190,opcode[dword_804B18c],opcode[dword_804B190],dword_804B198))

            #dword_804B190 = dword_804B18c



            opcode[dword_804B18c] = dword_804B198

            #print("opcode[%d] = %d"%(dword_804B18c,dword_804B190))

            

        elif dword_804B190 == 7:

            # i = opcode[9]

            # opcode[opcode[i]] ?== opcode[opcode[i+1]]

            sub_8048a48()

            dword_804B190 = opcode[dword_804B190]

            print("opcode[%d] = %d"%(7, opcode[7]))

            dword_804B198 = dword_804B190



            sub_8048a48()

            print(dword_804B190)

            dword_804B190 = opcode[dword_804B190]

            dword_804B194 = dword_804B190



            print(" %d == %d?"%(dword_804B194,dword_804B198))

            if dword_804B194 == dword_804B198:

                dword_804B198 = 1

            else:

                dword_804B198 = 1 # patch, make it continue.



            opcode[8] = dword_804B198 # check_flag

            

            

        elif dword_804B190 == 9:



            sub_8048a48()



            if opcode[8] == 0: # not equal, next step is break

                opcode[9] = (opcode[0xa]+dword_804B190)

            

        elif dword_804B190 == 10:



            sub_8048a48()

            opcode[9] = (opcode[0xa] + dword_804B190)

            print("opcode[%d] = %d"%(9,opcode[9]))

            

        elif dword_804B190 == 11:

            

            #dword_804B190 = 0

            #dword_804B190 = opcode[0]

            #dword_804B198 = dword_804B190



            #dword_804B190 = 1

            #dword_804B190 = opcode[1]

            #dword_804B194 = dword_804B190



            #dword_804B190 = dword_804B198

            #dword_804B198 = dword_804B194

            print("nothing.")

        else:

            break

        

input = 'abcdefgh'

opcode_init([ord(i) for i in input])

vm()


```

## 参考资料

1. https://github.com/DoubleLabyrinth/reversing.kr/tree/master/SimpleVM
2. Reversing.kr题目之SimpleVM详解：https://www.freebuf.com/news/164664.html
3. ida+虚拟机-调试elf：https://blog.csdn.net/abc_670/article/details/80066817