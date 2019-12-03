# Reversing-Kr WindowsKernel Writeup

> [题目及脚本](https://github.com/L1B0/CTF/tree/master/Reversing-Kr/WindowsKernel)
>
> 做完这题到2k分了:-)

![QKcEHs.png](https://s2.ax1x.com/2019/12/03/QKcEHs.png)



## 解题思路

题目给了一个exe和一个sys驱动，均为32位。注意程序应放到**x86系统**运行，不然驱动无法加载成功。

先运行一下，当驱动加载成功后如下图。要进行输入需先点击`Enable`按钮。

![QKcYU1.png](https://s2.ax1x.com/2019/12/03/QKcYU1.png)

然后进行输入，按键时会明显发现有一定的延迟，结合提示`keyboard`可以猜测驱动获取了键盘输入进行处理。

![QKcLGV.png](https://s2.ax1x.com/2019/12/03/QKcLGV.png)

接下来用ida进行分析，首先看下`WindowKernel.exe`。

由于之前上病毒课有一些分析这种加载驱动的exe的经验，分析起来没之前那么难了。

sub_401310函数主要进行了启动驱动的操作，关键函数在sub_401110。

```c
HWND __thiscall sub_401110(HWND hDlg)
{
  HWND v1; // edi
  HWND result; // eax
  HWND v3; // eax
  HWND v4; // eax
  HWND v5; // eax
  WCHAR String; // [esp+8h] [ebp-204h]

  v1 = hDlg;
  GetDlgItemTextW(hDlg, 1003, &String, 512);
  if ( lstrcmpW(&String, L"Enable") )           // 不是enable
  {
    result = (HWND)lstrcmpW(&String, L"Check");
    if ( !result )
    {
      if ( sub_401280(v1, 0x2000u) == 1 )       // 校验
        MessageBoxW(v1, L"Correct!", L"Reversing.Kr", 0x40u);
      else
        MessageBoxW(v1, L"Wrong", L"Reversing.Kr", 0x10u);
      SetDlgItemTextW(v1, 1002, &word_4021F0);
      v5 = GetDlgItem(v1, 1002);
      EnableWindow(v5, 0);
      result = (HWND)SetDlgItemTextW(v1, 1003, L"Enable");
    }
  }
  else if ( sub_401280(v1, 0x1000u) )           // 开启虚拟盘符，发送控制码至驱动，开始记录
  {
    v3 = GetDlgItem(v1, 1002);
    EnableWindow(v3, 1);
    SetDlgItemTextW(v1, 1003, L"Check");
    SetDlgItemTextW(v1, 1002, &word_4021F0);
    v4 = GetDlgItem(v1, 1002);
    result = SetFocus(v4);
  }
  else
  {
    result = (HWND)MessageBoxW(v1, L"Device Error", L"Reversing.Kr", 0x10u);
  }
  return result;

```

其中的关键在sub_401280，它主要调用了函数`DeviceIoControl`与驱动进行交互，如下

```c
DeviceIoControl(v2, dwIoControlCode, 0, 0, &OutBuffer, 4u, &BytesReturned, 0)
```

当控制码为`0x1000`时开始记录，为`0x2000`时进行校验。

那么就需要分析驱动`WinKer.sys`了。

hook键盘获取键盘记录的函数在sub_00113E8，主要通过api`HalGetInterruptVector`，获取中断向量。

```c
void __stdcall hookKeyboard(struct _KDPC *Dpc, PVOID DeferredContext, PVOID SystemArgument1, PVOID SystemArgument2)
{
  int v4; // esi // Reference: https://ezbeat.tistory.com/301
  unsigned __int8 v5; // al
  int v6; // eax
  int KINTERRUPT_ADDR; // eax
  char v8[6]; // [esp+4h] [ebp-10h]
  KAFFINITY Affinity; // [esp+Ch] [ebp-8h]
  KIRQL Irql; // [esp+13h] [ebp-1h]

  v4 = KeGetCurrentProcessorNumber();
  v5 = HalGetInterruptVector(Isa, 0, 1u, 1u, &Irql, &Affinity);
  __sidt(v8);
  v6 = *(unsigned __int16 *)(*(_DWORD *)&v8[2] + 8 * v5) | (*(unsigned __int16 *)(*(_DWORD *)&v8[2] + 8 * v5 + 6) << 16);
  if ( MajorVersion < 6 )                       // windows xp
    KINTERRUPT_ADDR = v6 - 0x3C;                // //获取管理中断的中断对象（KINTERRUPT）的地址
  else                                          // windows 7
    KINTERRUPT_ADDR = v6 - 0x58;
  _disable();
  *((_DWORD *)P + v4) = *(_DWORD *)(KINTERRUPT_ADDR + 12);
  *(_DWORD *)(KINTERRUPT_ADDR + 12) = sub_1108C;
  _enable();
}
```

接收exe发送的控制码并进行分析的函数在sub_0011288。

```c
int __stdcall important(int a1, PIRP Irp)
{
  int v2; // edx
  _IRP *v3; // eax

  v2 = *(_DWORD *)(Irp->Tail.Overlay.PacketType + 12);
  v3 = Irp->AssociatedIrp.MasterIrp;
  if ( v2 == 0x1000 ) // 
  {
    *(_DWORD *)&v3->Type = 1;
    dword_13030 = 1;
    num = 0;
    dword_13024 = 0;
    flag = 0;
  }
  else if ( v2 == 0x2000 )
  {
    dword_13030 = 0;
    *(_DWORD *)&v3->Type = dword_13024; // dword_13024为最终校验值
  }
  Irp->IoStatus.Status = 0;
  Irp->IoStatus.Information = 4;
  IofCompleteRequest(Irp, 0);
  return 0;
}
```

监听键盘的函数在sub_0011266，通过端口`0x60`读取值，再调用sub_00111DC即processFromKeyboard进行处理。

```c
void __stdcall listenKeyboard(struct _KDPC *Dpc, PVOID DeferredContext, PVOID SystemArgument1, PVOID SystemArgument2)
{
  char v4; // al

  v4 = READ_PORT_UCHAR((PUCHAR)0x60);
  processFromKeyboard(v4);
}
```

sub_00111DC函数即对键盘记录进行判断，逻辑较为简单（逐位校验），一开始让我困扰的是为什么只校验**奇数位**的值。

```c
int __stdcall processFromKeyboard(char a1)
{
  int result; // eax
  bool v2; // zf

  result = 1;
  if ( flag != 1 )
  {
    switch ( num )
    {
      case 0:
      case 2:
      case 4:
      case 6:
        goto LABEL_3;
      case 1:
        v2 = a1 == 0xA5u;
        goto LABEL_6;
      case 3:
        v2 = a1 == 0x92u;
        goto LABEL_6;
      case 5:
        v2 = a1 == 0x95u;
LABEL_6:
        if ( !v2 )
          goto LABEL_7;
LABEL_3:
        ++num;
        break;
      case 7:
        if ( a1 == 0xB0u )
          num = 100;
        else
LABEL_7:
          flag = 1;
        break;
      default:
        result = sub_11156(a1);
        break;
    }
  }
  return result;
}
```

后来猜测是键的按下与弹起均有相应的值，百度搜到了一个[表](https://blog.csdn.net/firas/article/details/26267573)。

一一对应就能得到最后的key了（里面的e值有误），有一个坑是case 203别漏了，值和case 205一样。

```c
int __stdcall sub_110D0(char a1)
{
  int result; // eax
  char v2; // cl
  bool v3; // zf

  result = num - 200;
  v2 = a1 ^ 5;
  switch ( num )
  {
    case 200:
    case 202:
    case 204:
    case 206:
      goto LABEL_2;
    case 201:
      v3 = v2 == 0xB4u;
      goto LABEL_4;
    case 203: // 和case 205一样！！！
    case 205:
      v3 = v2 == 0x8Fu;
```



## windbg调试过程 

其实这题一开始是用windbg+双机（win10+winxp）联调做的，但不知道为啥win10在驱动中下的断点一直进不去，遂放弃了。。。

这里还是记录一下过程，关于双机配置什么的就跳过了，因为这环境是上学期病毒课配的，太久也忘了233。

windbg调试的命令如下

> p: 单步步过
>
> t: 单步步入
>
> g: 执行到断点
>
> .reload: 重新加载
>
> lm: ls modules
>
> !drvobj name: 查看驱动对象name的信息

在被调试机（winxp）中下断点在`bp 401280`，即最终调用`DeviceIoControl`的函数入口，`g`一下。

在点击Enable之后再`g`一下，变成check后回到调试机（win10）。

启动windbg，可以看到已经attach上了。

![QKo4fJ.png](https://s2.ax1x.com/2019/12/03/QKo4fJ.png)

`.reload`一下

```
kd> .reload
Connected to Windows XP 2600 x86 compatible target at (Tue Dec  3 11:54:38.786 2019 (UTC + 8:00)), ptr64 FALSE
Loading Kernel Symbols
...............................................................
...........................................................
Loading User Symbols

Loading unloaded module list
............................................
```

`lm`一下，如下，无关紧要的信息都略去了。

```
kd> lm
start    end        module name
804d7000 806d0680   nt         (pdb symbols)          f:\大三下\2019.4.17计算机病毒与防治\symbols\ntkrnlpa.pdb\7E4571CB945F42D182C86ABEBEA8E44D1\ntkrnlpa.pdb         
f791d000 f7923000   WinKer     (deferred)           
      

Unloaded modules:
edc86000 edcb1000   kmixer.sys
f78bd000 f78c3000   WinKer.sys
```

可以看到驱动`WinKr.sys`的起始地址为`0xf791d000`，加上想要断的函数偏移，比如函数`processFromKeyboard`的偏移是0x1DC，那么就`bp f791d1dc`。



## 参考链接

[1] [IDT挂接注意事项](https://ezbeat.tistory.com/301)

[2] [动态获取中断向量值（APIC描述。）](https://ezbeat.tistory.com/302)

[3] [keyboard scan code 表](https://blog.csdn.net/firas/article/details/26267573)

[4] [malwareAnalysis-Lab10-kernel-debug](https://github.com/L1B0/malwareAnalysis/tree/master/Lab_10)

