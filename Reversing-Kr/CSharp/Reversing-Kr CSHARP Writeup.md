# Reversing-Kr CSHARP Writeup

> [题目及脚本](https://github.com/L1B0/CTF/tree/master/Reversing-Kr/CSHARP)

## 解题思路

题目是一个.net文件，运行一下。

![Q1fPAS.png](https://s2.ax1x.com/2019/12/04/Q1fPAS.png)
遇到.net类型的题目我一般都是丢进ILSpy反编译一波，看伪码。

关键函数如下

```c#
// CSharp.Form1
private static void MetMetMet(string sss)
{
	byte[] bytes = Encoding.ASCII.GetBytes(Convert.ToBase64String(Encoding.ASCII.GetBytes(sss))); // base64加密
    // 动态调用函数MetMet
	AssemblyName assemblyName = new AssemblyName("DynamicAssembly");
	TypeBuilder typeBuilder = AppDomain.CurrentDomain.DefineDynamicAssembly(assemblyName, AssemblyBuilderAccess.RunAndSave).DefineDynamicModule(assemblyName.Name, assemblyName.Name + ".exe").DefineType("RevKrT1", TypeAttributes.Public);
	MethodBuilder methodBuilder = typeBuilder.DefineMethod("MetMet", MethodAttributes.Private | MethodAttributes.Static, CallingConventions.Standard, null, null);
	TypeBuilder typeBuilder2 = AppDomain.CurrentDomain.DefineDynamicAssembly(assemblyName, AssemblyBuilderAccess.RunAndSave).DefineDynamicModule(assemblyName.Name, assemblyName.Name + ".exe").DefineType("RevKrT2", TypeAttributes.Public);
	typeBuilder2.DefineMethod("MetM", MethodAttributes.Private | MethodAttributes.Static, CallingConventions.Standard, null, new Type[]
	{
		typeof(byte[]),
		typeof(byte[])
	}).CreateMethodBody(Form1.bb, Form1.bb.Length);
	Type type = typeBuilder2.CreateType();
	MethodInfo method = type.GetMethod("MetM", BindingFlags.Static | BindingFlags.NonPublic);
	object obj = Activator.CreateInstance(type);
	byte[] array = new byte[] // 校验值
	{
		1,
		2
	};
	method.Invoke(obj, new object[] // 关键，回调函数MetMet
	{
		array, // 校验值
		bytes // 输入的base64编码
	});
	string str;
	if (array[0] == 1) // 校验正确与否
	{
		str = "Wrong";
	}
	else
	{
		str = "Correct!!";
	}
	ILGenerator iLGenerator = methodBuilder.GetILGenerator();
	iLGenerator.Emit(OpCodes.Ldstr, str);
	iLGenerator.EmitCall(OpCodes.Call, typeof(MessageBox).GetMethod("Show", new Type[]
	{
		typeof(string)
	}), null);
	iLGenerator.Emit(OpCodes.Pop);
	iLGenerator.Emit(OpCodes.Ret);
	Type type2 = typeBuilder.CreateType();
	MethodInfo method2 = type2.GetMethod("MetMet", BindingFlags.Static | BindingFlags.NonPublic);
	object obj2 = Activator.CreateInstance(type2);
	method2.Invoke(obj2, null);
}
```

当想查看函数`MetMett`的伪码时发现报错。

![Q1fHuq.png](https://s2.ax1x.com/2019/12/04/Q1fHuq.png)

这就很尴尬了，常用方法行不通。既然该函数是动态调用的那么就只能动态调试了。

网上查了下关于.net的动态调试工具，发现[dnspy](https://github.com/0xd4d/dnSpy/releases)不错。

在我的吾爱破解的xp虚拟机里发现也有这个工具，美滋滋。

那么接下来就开始动态调试。

## 动态调试.net

在`dnspy`工具中，常用命令如下。

> 单步步入：F11
>
> 单步步过：F10
>
> 执行至断点：shift+F11
>
> 下断点：F9

在关键函数`MetMetMet`下断点，运行，随便输入，然后check。

然后在下图`methon.invoke`处下断点，执行到此处时**单步步入**。

![Q1ht2j.png](https://s2.ax1x.com/2019/12/04/Q1ht2j.png)

继续步入，

![Q1hHRH.png](https://s2.ax1x.com/2019/12/04/Q1hHRH.png)

步入

![Q1hLQA.png](https://s2.ax1x.com/2019/12/04/Q1hLQA.png)

然后单步步过，经过一些检查环节后，执行到下图，**步入**。

![Q14KW4.png](https://s2.ax1x.com/2019/12/04/Q14KW4.png)

之后就也是步入步过，最后终于到达了函数`MetMett`，即校验环节。

![Q14gk8.png](https://s2.ax1x.com/2019/12/04/Q14gk8.png)

将数据异或回去即可:-)

以上。