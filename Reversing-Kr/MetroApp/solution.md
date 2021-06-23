# reversing-kr-MetroApp

## 运行配置
```
PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy Unrestricted                                               
执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): y
PS C:\WINDOWS\system32> Add-AppxPackage D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\MetroApp_1.0.0.5_Win32.appx
Add-AppxPackage : 部署失败，原因是 HRESULT: 0x800B0109, 已处理证书链，但是在不受信任提供程序信任的根证书中终止。
错误 0x800B0109: 应用包或捆绑包中的签名的根证书必须是受信任的证书。
注意: 有关其他信息，请在事件日志中查找 [ActivityId] 80077177-633c-0004-886b-13803c63d701，或使用命令行 Get-AppPackageLo
g -ActivityID 80077177-633c-0004-886b-13803c63d701
所在位置 行:1 字符: 1
+ Add-AppxPackage D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\Metro ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (D:\\日常学习\逆向练....0.5_Win32.appx:String) [Add-AppxPackage], Exc
eption
    + FullyQualifiedErrorId : DeploymentError,Microsoft.Windows.Appx.PackageManager.Commands.AddAppxPackageCommand

PS C:\WINDOWS\system32> D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\Add-AppDevPackage.ps1                Found package: D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\MetroApp_1.0.0.5_Win32.appx
Error: No certificate found in the script directory.  Please make sure the certificate used to sign the package you are installing is placed in the same directory as this script.
按 Enter 键继续...: y
PS C:\WINDOWS\system32> D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\Add-AppDevPackage.ps1
Found package: D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\MetroApp_1.0.0.5_Win32.appx
Found certificate: D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\MetroApp_1.0.0.5_Win32.cer
Error: The developer certificate "D:\\日常学习\逆向练习\reversing-kr-MetroApp\MetroApp\MetroApp_1.0.0.5_Win32.cer" has expired. One possible cause is the system clock isn't set to the correct date and time. If the system settings are correct, contact the package owner to re-create a package with a valid certificate.
按 Enter 键继续...:
```

提示依赖失败，于是手动运行dependency的appx，然后再次安装就成功了。

修改系统时间为此时间段内。
![2180_1](https://i.loli.net/2021/06/23/2CEURkc89LAxVPj.png)

![2182_1](https://i.loli.net/2021/06/23/Jmq36KUYSfXTvrB.png)

## 静态分析

翻了下manifest文件，发现里面有字符串correct和wrong。
![2170_1](https://i.loli.net/2021/06/23/nPd7XZFTKj6vlsm.png)

把MetroApp_1.0.0.5_Win32.appx解压缩后里面有个exe，拖进ida搜一下字符串，会发现其实搜不到，随便翻翻发现有OK_button，并且还间隔了0x00。

![2186_1](https://i.loli.net/2021/06/23/RlfBN2at6gcw8Yu.png)

于是去在010editor里搜C,0x00,r,0x00，然后到ida里找偏移。

![2188_1](https://i.loli.net/2021/06/23/3ETIyVNHdsPYF9o.png)

![2172_1](https://i.loli.net/2021/06/23/8CIVO4YUL6W9mXP.png)

![2176_1](https://i.loli.net/2021/06/23/Z8gEkX6eIhAuwfJ.png)

![2174_1](https://i.loli.net/2021/06/23/ixko4RBILFA2Psn.png)

![2178_1](https://i.loli.net/2021/06/23/n8qFaDjsy6iQpXP.png)

## 动态分析（x32dbg）

olldbg附加的时候找不到该进程。。。于是使用x32dbg。
程序一开始先比较输入是否位“MERONG”，但这并不会跳入correct，之后会对输入进行校验，以input[0]为例，首先计算input[0]&0x7，然后将input[0]与该结果进行循环左移，之后以下标0为偏移，在0x407a8处拿出一个byte，与之前循环左移后的结果进行异或，并将该结果与input[1]比较是否相等。

![2184_1](https://i.loli.net/2021/06/23/le5PBVtMJRouOSn.png)

README提示输入由大写字母和数字组成，爆破所有可能的结果，一个一个溯源找即可。
```
import string

data = [0x77, 0xAD, 0x07, 0x02, 0xA5, 0x00, 0x29, 0x99, 0x28, 0x29, 
  0x24, 0x5E, 0x2E, 0x2A, 0x2B, 0x3F, 0x5B, 0x5D, 0x7C, 0x5C, 
  0x2D, 0x7B, 0x7D, 0x2C, 0x3A, 0x3D, 0x21, 0x0A, 0x0D, 0x08]

str_map = string.ascii_uppercase + string.digits
print(str_map)

def rol(a,n):

    a = (bin(a)[2:]).rjust(8,'0')
    a = eval('0b'+a[n:]+a[:n])

    return a
    

for j in str_map:
    a = ord(j)
    b = ord(j)
    a = a&0xf
    a = a&0x7
    #print(b,a)
    b = rol(b,a)
    #print(b)

    for i in range(8):
        a = data[i]
        #print(b)
        c = b^a
        #print(c,i)
        if chr(c) in str_map:
            print(i,j,chr(c))
        

```
结果
```
6 C 3
0 D 3
2 D C
3 D F
5 D D
7 E 1
4 F 4
2 H O
3 H J
5 H H
4 I 7
3 K X
5 K Z
7 M 0
4 N 6
2 P W
3 P R
5 P P
2 R N
3 R K
5 R I
1 S 7
0 T 2
2 T B
3 T G
5 T E
7 U 3
1 V 8
4 V 0
7 W 2
3 X Z
5 X X
0 0 G
2 0 7
3 0 2
5 0 0
6 1 K
7 2 Q
1 3 4
0 4 4
2 4 D
3 4 A
5 4 C
1 7 6
0 8 O
5 8 8 D34DF4C3
```

