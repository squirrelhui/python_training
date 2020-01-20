

# Python DevWeb 

# Python DevWeb Day01

自学网站：w3school.com.cn

web开发：

前端：在用户一侧、渲染的部分。HTML+CSS+JS

后端：在服务一侧执行。Python + PHP + JAVA

## 一、HTML快速入门

### （一）HTML概述

#### 1、超文本

• Web 是一个超文本文件的集合
• 超文本文件是 Web 的基本组成单元,也称为网页或HTML文档、Web页等,通常是以.html或.htm为后缀的文件
• Web页之间通过超文本中的超级链接组织在一起



#### 2、HTML概念

• HTML(HyperText Markup Language):超文本标记语言,一种纯文本类型的语言
– 使用带有尖括号的“标记”将网页中的内容逐一标识出来
• 用来设计网页的标记语言
• 用该语言编写的文件,以 .html 或者 .htm 为后缀
• 由浏览器解释执行
• HTML 页面上,可以嵌套用脚本语言编写的程序段,如:VBScript,JavaScript

### （二）HTML基础语法

#### 1、标记语法

• HTML 用于描述功能的符号称为“标记”,比如“<p>、<h1>”等

– 标记在使用时必须使用尖括号括起来
– 有封闭类型标记,也有非封闭类型的标记

```html
Some text here.
<h1>Some text here.</h1>
```

• 封闭类型标记(也叫双标记):必须成对出现
– <标记>内容</标记>
• 封闭类型的标记必须成对出现
– 如果一个应该封闭的标记没有被封闭,则会产生意料不到的错误

```html
<!---双标记>
<p>段落一</p>
<h1>另一个标题,忘了结束</h1>
<p>还是普通段落吗?</p>
```

• 非封闭类型标记,也叫做空标记,或者单标记
– <标记 />
– 或者
– <标记>
• 不能包含内容

```html
<!---单标记>
普通文本一<br/>普通文本二
普通文本三<br>普通文本四
```



#### 2、元素

• 元素,即标记
• 每一对尖括号包围的部分
– 如 <body></body>包围的部分就叫做 body 元素
– 元素就像是小标签,用于标识网页文档的不同部分
• 元素可以包含文本内容和其他元素,也可以是空的,比如前面所述的空标记

#### 3、元素嵌套

• 元素之间可以相互嵌套,形成更为复杂的语法
• 在嵌套元素时需要注意标记的嵌套顺序



#### 4、元素属性和值

元素可以设置属性，但是大多数的属性应该通过CSS样式表来设置

• 属性用来修饰元素
– 属性的声明必须位于开始标记里
– 一个元素的属性可能不止一个,多个属性之间用空格隔开
– 多个属性之间不区分先后顺序
• 每个属性都有值
– 属性和属性的值之间用等号连接
– 属性的值包含在引号中

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>动嗨</title>
</head>
<body bgcolor="silver" text="#00008b">
<h1>中超联赛</h1>
<hr color="red">广州恒大
<h2>CBA</h2>
<hr>广东宏远
</body>
</html>
```



#### 5、标准属性

• 每个元素都有自己所特有的属性
• 有些属性是绝大多数元素都支持的属性,称为标准属性(或通用属性)
– id
– title
– class
– style

#### 6、注释

• 为代码添加适当的注释是一种良好的编码习惯
• 注释只在编辑文档情况下可见,在浏览器展示页面时
并不会显示
• 添加注释的语法如下:
– <!-- 注释的文本内容 -->

1、“<!--”和“-->”之间的任何内容都不会显示在浏览器中
2、注释不可以嵌套在其他注释中
3、注释不可以位于嵌在 <>中



### （三）文档结构

基础html样式

```html
<!DOCTYPE html>    <!--声明文档类型-->
<html lang="en">   <!--html是根标记，其他类绒必须在html标记中-->
<head>             <!--用于声明一些说明内容-->
    <meta charset="UTF-8">   <!--元数据-->
    <title>Title</title>     <!--网页标题-->
</head>
<body>    <!--浏览器窗体中显示的内容， 都要放到body中-->

</body>
</html>
```



## 二、基本标签用法

### （一）使用文本标记

#### 1、文本与特殊字符

• 文本是网页上的重要组成部分
– 直接书写的文本会用浏览器默认的样式显示
– 包含在标记中的文本则会被显示为标记所拥有的样式
• 空格折叠
– 多个空格或制表符压缩成单个空格,即只显示一个空格
• 特殊字符(如空格),需要进行转义(使用字符实体)

```html
The &lt;p&gt; element.&nbsp;&nbsp;&nbsp;<br>
    &lt;p&gt;&lt;;&gt;<br>
    hello&nbsp;&nbsp;world!<br>
    &copy; 2011 by tarena <br>
    &aacute;&beta;&circeq;
```

浏览器显示效果

The <p> element.  
    <p><;>
    hello world!
    © 2011 by tarena 
    áβ≗

#### 2、文本样式

• 文本样式的作用是对文本进行修饰,如加粗、倾斜等

```html
– <b>...</b>:加粗
– <i>...</i>:倾斜
– <u>...</u>:下划线
– <s>...</s>:删除线
– <sup>...</sup>:上标
– <sub>...</sub>:下标
<b>粗体</b>文本
<i>斜体</i>文本
<u>下划线</u>文本
<s>删除线</s>文本
<sub>下标</sub>文本
<sup>上标</sup>文本
```



#### 3、标题元素 <hn>

• 标题元素让文字以醒目的方式显示,往往用于文章的标题
• 基本语法:<h#> ... </h#>
– #=1, 2, 3, 4, 5, 6
– 从<h1>到<h6>,即 标题1-标题6

```html
<h1>h1 text</h1>
<h2>h2 text</h2>
```

#### 4、段落元素 <p>

• <p> 元素提供了结构化文本的一种方式
• <p> 元素中的文本会用单独的段落显示
– 与前后的文本都换行分开
– 添加一段额外的垂直空白距离,作为段落间距
– 常用属性: align

```html
<p>The first paragraph.</p>
<p align="right">The second paragraph.</p>
```

#### 5、换行元素 <br>

• 使用#<br> 元素在任何地方创建手工换行
– 空标记

```html
<p>This is a <br/> paragraph.</p>
```



#### 6、分区元素 <span> 和 <div>

• 分区元素用于为元素分组,常用于页面布局
• 块分区元素:<div></div>
• 行内分区元素:<span></span>
– 设置同一行文字内的不同格式

```html
<div style="color:blue;">
<p>first</p>
<p>second</p>
</div>
<p>
一周畅销<span style="color:red;">榜</span>
</p>
```



#### 7、行内元素与块级元素

• 块级元素
– 默认情况下,块级元素会独占一行,即元素前后都会自动换行
– 如:<p>、<div>、<hn>
• 行内元素
– 不会换行,可以和其他行内元素位于同一行
– 如:<span>、<b>、<i>、<u>

#### 8、分隔线元素 <hr>



### （二）图像和链接

#### 1、URL

• URL (Uniform Resource Locator) :统一资源定位器,用来标识网络中的任何资源
– 文本、图片、音视频文件,段落,或其他超文本
• 即路径,指从当前位置到目标位置所经过的路线
• Web 页面常用 URL 形式:
– 绝对路径
– 相对路径

静态文件的位置

一般会在网站的目录下建立

```shell
(nsd1908) [student@room9pc01 day01]$ mkdir -p static/{imgs,js,css}
(nsd1908) [student@room9pc01 day01]$ ls
day01.py  html5.html  myhtml.html  static
(nsd1908) [student@room9pc01 day01]$ ls static/
css  imgs  js
```



#### 2、图像元素<img>

• 使用 <img> 元素将图像添加到页面
– 空标记
• 必须属性:src
• 常用属性:width、height

```html
<img width="100" src="image/rose.jpg" />
```



#### 3、链接元素<a>

• 使用 <a> 元素创建一个超级链接,语法如下:
• <a href="" target="">文本</a>
– href 属性:链接 URL
– target 属性:目标,可取值为 _blank、_self 等
– name 属性:锚点名称

```html
<a href="http://www.google.com.hk">To Google</a>
<br />
<a href="teacher/teacher.asp" target="_blank">
To other page
</a>
```



#### 4、链接的表现形式

• 目标文档为下载资源

```html
<a href="DAY02.zip">下载</a>
```

• 电子邮件链接

```html
<a href="mailto:tarena@tarena.com.cn">联系我们</a>
```

• 返回页面顶部的空链接

```html
<a href="#">...</a>
```

• 链接到JavaScript

```html
<a href="javascript : ...">JS 功能</a>
```

#### 5、锚点

• 锚点是文档中某行的一个记号
– 用于链接到文档中的某个位置
• 使用方式
– 1、定义锚点

```html
<a name=”anchorname1”>锚点一</a>
```

– 2、链接到锚点:在锚点名前加上#

```html
<a href="#anchorname1">...</a>  如果文本/图像与锚点存在同一页面

<a href="页面URL#anchorname1">...</a>   如果文本/图像与锚点存在不同页面


<a name="here"></a>      <!--定义锚点-->
<br /><br />
<br /><br />
<br /><br />
<a href="#here">Return to top</a>     <!--使用链接,导航到锚点 -->
```



### （三）使用文本标记



### （四）图像和链接



### （五）表格

#### 1、创建表格

• 定义表格:使用成对的 <table></table> 标记
• 创建表行:使用成对的 <tr></tr> 标记
• 创建单元格:使用成对的 <td></td> 标记

```html
<table border="1">
<tr>
<td>第1行,第1列</td>
<td>第1行,第2列</td>
</tr>
<tr>
<td>第2行,第1列</td>
<td>第2行,第2列</td>
</tr>
</table>
```



#### 2、表格的常用属性

• <table>元素
– width,设置表格宽度
– height,设置表格高度
– align,设置表格对齐方式(left|center|right)
– border,设置表格边框宽度
– cellpadding,设置内边距(单元格边框与内容之间的距离)
– cellspacing,设置外边距(单元格之间的距离)
– bgcolor,设置表格背景颜色

• <tr>元素
– align,设置水平对齐方式(left|center|right)
– valign,设置垂直对齐方式(top|middle|bottom)
• <td>元素
– align,设置水平对齐方式(left|center|right)
– valign,设置垂直对齐方式(top|middle|bottom)
– width,设置宽度
– height,设置高度
– colspan,设置单元格跨列
– rowspan,设置单元格跨行

#### 3、不规则表格

• 设置单元格 <td> 的跨行或者跨列属性
• 跨列:colspan
– 水平方向延伸单元格,值为一正整数,代表此单元格水平延伸的单元格数
• 跨行:rowspan
– 垂直方向延伸单元格,值为一正整数,代表此单元格S垂直延伸的单元格数

### （六）列表

#### 1、列表的作用

• 列表是指将具有相似特征或者具有先后顺序的几行文字进行对齐排列

• 所有的列表都由列表类型和列表项组成
– 列表类型:有序列表<ol>和无序列表<ul>
– 列表项:<li>,用于指示具体的列表内容

#### 2、有序列表 <ol>

• <ol> 元素编写有序列表,用于列出页面上有特定次序的一些项目
• <ol> 元素中只能包含列表项元素 <li>

```HTML
<ol type="列表类型" start="起始编号">
<li>...</li>
<li>...</li>
...
</ol>
```

• type 属性值
– 1,数字(默认)
– a,小写字母
– A,大写字母
– i,小写罗马数字
– I,大写罗马数字

```HTML
<ol type="A" start="3">
<li>MySQL</li>
<li>MS SQL Server</li>
<li>Oracle</li>
<li>Sysbase</li>
<li>Informix</li>
</ol>
```



#### 3、无序列表 <ul>



#### 4、列表嵌套



## 三、From表单及控件

### （一）表单概述

#### 1、表单的作用

• 表单用于显示、收集信息,并提交信息到服务器
• 表单有两个基本部分
– 实现数据交互的可见的界面元素,比如文本框或按钮
– 提交后的表单处理
• 界面元素
– 使用 <form> 元素创建表单
– 在 <form> 元素中添加其他表单可以包含的控件元素

#### 2、表单元素<form>

• 定义表单:使用成对的 <form></form> 标记
• 主要属性
– action:定义表单被提交时发生的动作,通常包含服务方脚本的URL(比如JSP、PHP)
– method:指出表单数据提交的方式,取值为 get 或者post
– enctype:表单数据进行编码的方式
– name:表单名称

#### 3、表单控件

• 表单可以包含很多不同类型的表单控件
• 表单控件元素是包含在表单元素中具有可视化外观的
HTML元素,用于访问者输入信息
• 表单控件元素有
– input元素:文本输入控件、按钮、单选和复选按钮、选项
框、文件选择框和隐藏控件等
– textarea元素
– select和option元素
– 其他元素

### （二）<input> 元素

#### 1、<input> 元素

• <input> 元素用于收集用户信息
• 该元素是一个单标记,语法为:<input />
• 主要属性
– type:根据不同的 type 属性值,可以创建各种类型的输入字段,比如文本框、复选框等
– value:控件的数据
– name:控件的名称
– disabled:禁用控件

#### 2、文本框与密码框

• 文本框:<input type =“text" />
• 密码框:<input type =“password"/>
• 主要属性
– name:名称
– value :由访问者自由输入的任何文本
– maxlength :限制输入的字符数
– readonly :设置文本控件只读

#### 3、单选框和复选框

• 文本框:<input type =“text" />
• 密码框:<input type =“password"/>
• 主要属性
– name:名称
– value :由访问者自由输入的任何文本
– maxlength :限制输入的字符数
– readonly :设置文本控件只读

```html
姓名:<input type="text" name="username"
value="mary" maxlength="6" />
<br /><br />
密码:<input type="password" name="pwd" />
```

• 单选框: <input type="radio"/>
• 复选框: <input type="checkbox" />
• 主要属性
– name:设置名称,并用于分组,一组单选框或者复选框的名称必须相同
– value:文本,当提交 form 时,如果选中了此单选按钮,那么 value 就被发送到服务器
– checked: 设置默认被选中

```html
性别:
<input type="radio" name="sex" value="0"/>男
<input type="radio" name="sex" value="1"/>女
<input type="radio" name="sex" value="2" checked="checked"/>保密
<br /><br />
喜欢的城市:
<input type="checkbox" name="cities" value="1"/>北京
<input type="checkbox" name="cities" value="2"/>厦门
<input type="checkbox" name="cities" value="3"/>敦煌
<input type="checkbox" name="cities" value="4" checked="checked"/>
杭州
```



#### 4、按钮

• 提交按钮: <input type="submit"/>
– 传送表单数据给服务器端或其它程序处理
• 重置按钮: <input type="reset" />
– 清空表单的内容并把所有表单控件设置为最初的默认值
• 普通按钮: <input type="button" />
– 用于执行客户端脚本
• 主要属性
– name:名称
– value:按钮的标题文本

#### 5、隐藏域和文件选择框

• 隐藏域: <input type="hidden"/>
– 在表单中包含不希望用户看见的信息
– name 属性:名称
– value 属性:值
• 文件选择框: <input type="file" />
– name 属性:名称

### （三）其它控件

#### 1、<label> 元素

• 语法: <label>文本</label>
• 主要属性:
– for:表示与该元素相联系的控件的 ID 值
• 作用:
– 将文本与控件联系在一起后,单击文本,效果就同单击控件一样

```html
<input type="checkbox" name="chkHid" id="chkHid" />
<label for="chkHid" >不要公开我的信息</label>
```



#### 2、选项框

• 两种:下拉选项框和滚动列表
• <select>:创建选项框
– name:选项框命名
– size:大于 1 ,则为滚动列表
– multiple:设置多选
• <option>:选项
– value:选项的值
– selected:预选中

```html
选择课程:
<select>
<option value="1">Java</option>
<option value="2">C++</option>
<option value="3">PHP</option>
</select>
选择课程:<br />
<select size="4" >
<option value="1">Java</option>
<option value="2">C++</option>
<option value="3">PHP</option>
</select>
```



#### 3、<textarea> 元素

• 多行文本输入框
– <textarea>文本</textarea>
• 主要属性:
– name:名称
– cols:指定文本区域的列数
– rows:指定文本区域的行数
– readonly:只读

```html
多行文本框:<br />
<textarea name="txtInfo" rows="4" cols="20"></textarea>
```





## 三、CSS概述

### （一）CSS 概述

#### 1、CSS 的作用

#### 2、什么是 CSS

• CSS(Cascading Style Sheets):层叠样式表,又叫级联样式表,简称样式表
• 用于 HTML 文档中元素的样式定义
– 实现了将内容与表现分离
– 提高代码的可重用性和可维护性

#### 3、CSS 与 HTML 之间的关系

• HTML 用于构建网页的结构
• CSS 用于构建 HTML 元素的样式
• HTML 是页面的内容组成,CSS 是页面的表现

#### 4、HTML 属性与 CSS 样式的使用原则

• W3C 建议尽量使用 CSS 样式取代 HTML 属性
– 实现内容和表现的分离
– 如果为 HTML 所特有的属性,则使用 HTML 属性

### （二）使用 CSS 样式表

#### 1、使用 CSS 样式表的方式

• 内联方式
– 样式定义在单个的 HTML元素中，与元素属性一样使用。内容与形式混杂载一起，不推荐
• 内部样式表
– 样式定义在 HTML 页的头元素中，将样式统一声明到head中的style标签中
• 外部样式表
– 将样式定义在一个外部的 CSS 文件中(.css 文件)
– 由 HTML 页面引用样式表文件

#### 2、内联方式使用 CSS

• 样式定义在 HTML 元素的标准属性 style 里
• CSS 语法
– 只需要将分号隔开的一个或者多个属性/值对作为元素的style 属性的值
– 属性和属性值之间用:连接
– 多对属性之间用;隔开

```html
<h1 style =“background-color : silver ; color : blue ;”>
文本
</h1>
```



#### 3、内部样式表

• 样式表规则位于文档头元素中的 <style> 元素内
– 在文档的 <head> 元素内添加 <style> 元素
– 在 <style> 元素中添加样式规则

```html
<html>
<head>
<style type="text/css">
h1 { 
    color : blue ;
    }
</style>
</head>
<body>
<h1>文本1</h1>
<h1>文本2</h1>
</body>
</html>
```

• 在 <style> 元素中添加样式规则
– 可以定义多个样式规则
– 每个样式规则有两个部分:选择器和样式声明
• 选择器:决定哪些元素使用这些规则
• 样式声明:一对大括号,包含一个或者多个属性/值对

```html
<head>
<style type="text/css">

h1
{
    color : blue ;
}
</style>
</head>

样式声明
```



#### 4、外部样式表

• 第一步:创建一个单独的样式表文件用来保存样式规则
– 一个纯文本文件,文件后缀为 .css
– 该文件中只能包含样式规则
– 样式规则由选择器和样式声明组成

• 第二步:在需要使用该样式表文件的页面上,使用<link> 元素链接需要的外部样式表文件
– 在文档的 <head> 元素内添加 <link> 元素

```html
<html>
<head>
<link rel="stylesheet" type="text/css" href="myStyle.css" />
</head>
<body>
<h1>1号标题</h1>
<p>段落</p>
<span>其他文本</span>
</body>
</html>
```



# Python DevWeb Day02

## 一、CSS 基础语法

### （一）CSS 语法规范

#### 1、CSS 语法规范总结

• 内联样式:由样式声明组成

```html
<h1 style=“background-color:silver;color:blue;”>文本</h1>
```

• 样式表(内部样式表或者外部样式表)
– 由多个样式规则组成
– 每个样式规则有两个部分:选择器和样式声明

#### 2、CSS 样式表特征

• 继承性
– 大多数 CSS 的样式规则可以被继承
• 层叠性
– 可以定义多个样式
– 不冲突时,多个样式表中的样式可层叠为一个
• 优先级
– 样式定义冲突时,按照不同样式规则的优先级来应用样式

#### （二）CSS 基础选择器

#### 1、通用选择器

• 通用选择器,显示为一个星号(*)
– 可以与任何元素匹配
– 常用于设置一些默认样式,比如设置整个文档的文本的默认字体和大小

```html
*
{
    font-size : 9pt;
    font-family : "Times New Roman";
}
```



#### 2、元素选择器

• html 文档的元素就是选择器
– 比如 <p>、<h1> 等

```html
html
{
color : black ;
}
h1
{
color : blue ;
}
h2
{
color : silver ;
}
```



#### 3、类选择题

• 语法为:.className { color:red;}
– 类名称不能以数字开头
• 所有能够附带class属性的元素都可以使用此样式声明
– 将元素的 class属性的值设置为样式类名

样式表中:声明一个样式类

```html
.myClass
{
background-color : Pink;
font-size : 35pt;
}
```

html 文档中:将元素的 class 属性的值设置为样式类的名称

```html
<h2 class="myClass">h2文本</h2>
<p class="myClass">段落文本</p>
```

• 可以将多个类选择器应用于同一个元素(多类选择器)
– HTML 元素的 class 属性的值中可能包含一个词列表
– 各个词之间用空格分隔,每个词都是一个类选择器

```html
样式表中:声明两个样式类
.important {
font-weight : bold;
}
.warning {
color : red;
}

html 文档中:将元素的 class 属性的值设置为多个样式类名的列表
<p class="warning">警告</p>
<p class="important">重要</p>
<p class="important warning">哈哈</p>
```

• 可以将类选择器和元素选择器结合起来使用,以实现对某种元素中不同样式的细分控制(分类选择器)
• 语法为:元素选择器 .className { }
– 先声明一个元素选择器
– 然后使用一个点号(.)代表将使用类选择器
– 然后声明一个类的名称
– 最后使用一对大括号声明样式规则
• 将样式规则与附带 class 属性的某种元素匹配
– 元素的 class 属性的值为分类选择器中指定的样式类名

```html
样式表中:定义一个分类选择器
p.important
{
color : red ;
font-size : 20pt;
border:1px solid black;
}

html 文档中:将元素的 class 属性的值设置为样式类的名称
<h2 class="important">h2文本</h2>
<p class="important">段落文本</p>
```

class为c3的元素：p.c3

p元素中的c4: p .c4

#### 4、id 选择器

• id 选择器以一种独立于文档元素的方式来指定样式
• 它仅作用于 id 属性的值
• 语法为:
– 选择器前面需要有一个 # 号
– 选择器本身则为文档中某个元素的 id 属性的值

```html
样式表中:定义一个 id 选择器
#mostImportant
{
color:red;
background:yellow;
}
html 文档中:将元素的 id 属性的值设置为选择器的名称
<h1 id="mostImportant">This is important!</h1>
<h1 >This is important!</h1>
```



#### 5、群组选择器

• 选择器声明为以逗号隔开的选择器列表
– 将一些相同的规则作用于多个元素

```html
样式表中:定义选择器分组
h2, p.important
{
color:green;
font-size:20pt;
border:1px solid red;
}

html 文档中:
<p class="important">p text</p>
<h2>h2 text</h2>
```



#### 6、伪类选择器

• 伪类用于向某些选择器添加特殊的效果
• 使用冒号(:)作为结合符,结合符左边是其他选择器,右边是伪类
– 选择器 : 伪类选择器
• 链接伪类
– : link ,适用于尚未访问的链接(访问前)
– : visited ,适用于访问过的链接（访问后）
• 动态伪类,用于呈现用户操作
– :hover,适用于鼠标悬停在 HTML 元素时
– :active,适用于 HTML 元素被激活时
– :focus,适用于 HTML 元素获取焦点时

## 二、尺寸与框模型

### （一）尺寸

#### 1、尺寸单位

• %:百分比
• in:英寸
• cm:厘米
• mm:毫米
• pt:磅(1pt等于1/72英寸)
• px:像素(计算机屏幕上的一个点)
• em:1em等于当前的字体尺寸,2em等于当前字体尺寸的两倍,继承父级元素的字体大小
• rem:与em类似,但是相对于根元素设置字体尺寸的倍数

#### 2、颜色单位

使用RGB颜色，每种颜色都使用8位2进制数表示，表示成10进制数为0-255，表示成16进制数位00-FF。

颜色的数值越小，表示该颜色越暗

• rgb(x,x,x):RGB 值,如 rgb(255,0,0)
• rgb(x%,x%,x%):RGB百分比值,如rgb(100%,0%,0%)
• #rrggbb:十六进制数,如#ff0000
• #rgb:简写的十六进制数,如#f00
• 表示颜色的英文单词,如 red

#### 3、尺寸

• 尺寸属性是用于设置元素的宽度和高度
– 单位一般为像素或百分比
• 宽度属性
– width
– max-width
– min-width
• 高度属性
– height
– max-height
– min-height

### （二）框模型

#### 1、边框

网页内一切皆框

某一元素载页面上所占有的宽度是：元素宽度+左右内边距+左右边框+左右外边距

• 简写方式
– border:width style color;
• 单边定义
– border-left/right/top/bottom:width style color;
• border-width
– border-left/right/top/bottom-width
• border-style
– border-left/right/top/bottom-style
• border-color
– border-left/right/top/bottom-color





#### 2、框模型

• 框模型(Box Model)定义了元素框处理元素内容、内边距、边框和外边距的方式

![image-20200120114726174](/home/student/.config/Typora/typora-user-images/image-20200120114726174.png)

• width 和 height 指内容区域的宽度和高度
• 增加内边距、边框和外边距不会影响内容区域的尺寸,但是会增加元素框的总尺寸

#### 3、什么是外边距

• 围绕在元素边框周围的空白区域是外边距
– 会在元素外创建额外的空白
– 外边距是透明的

#### 4、外边距 margin

• 外边距:与下一个元素之间的空间量
– margin:value;
• 单边设置
– margin-top/right/bottom/left:value;
• 外边距的属性值可能为px(像素),百分比(%)或自动(auto),也可以为负值

• 默认情况下,以下 HTML 块级元素都存在外边距
– body
– h1,h2,h3,h4,h5,h6
– p...
• 声明 margin 属性,可以覆盖默认样式

• margin 可取值为 auto,由浏览器计算外边距– 实现水平方向居中显示的效

#### 5、什么是内边距

• 内边距:内容区域和边框之间的空间
– 会扩大元素边框所占用的区域

#### 6、内边距 padding

• 内边距:内容与框线之间的距离
– padding:value;
• 内边距属性值可以为像素、百分比,但不能为负数
• 单边设置
– padding-top/right/bottom/left:value;

## 三、常用样式属性

### （一）背景属性

#### 1、背景色 background-color

• background-color 属性用于为元素设置背景色
– 接受任何合法的颜色值
– 可取值为 transparent
• 为元素背景设置一种纯色
– 会填充元素的内容、内边距和边框区域
– 如果边框有透明部分,会透过这些透明部分显示出背景色。

```html
div
{
border:2px dashed black;
width:200px;
height:50px;
background-color:#ccc;
}
```



#### 2、背景图片 background-image

• 默认值是 none,表示背景上没有放置任何图像
• 如果需要设置一个背景图像,需要用起始字母 url 附带一个图像的 URL 值
– 可以是相对 URL 或者绝对 URL

```html
body
{
background-image: url("image/bg_01.gif");
}

```



### （二）字体属性

#### 1、控制字体

• 指定字体
– font-family : value1,value2;
• 字体大小
– font-size : value;
• 字体加粗
– font-weight : normal/bold/value;
• 字体样式
– font-style : normal/italic;
• 小型大写字母显示
– font-variant : normal/small-caps;

```html
样式表中:
p {
    font-family : Times, 'New York', serif ;
    font-size : 14pt ;
    font-weight : bold ;
    font-style : italic;
    font-variant : small-caps;
}

html 文档中:
<p>this is a paragraph.</p>
```



#### 2、字体属性 font

• 字体属性 font 用于把所有针对字体的属性设置在一个声明中
• 为简写属性,包含6个值,可以按顺序设置
– font : font-style font-variant font-weight font-size font-family;
– 不设置的值,则使用默认设置

#### 3、控制文本格式

• 文本颜色 color : value;
• 文本排列 text-align : left/right/center;
• 文字修饰 text-decoration : none/underline;
• 行高 line-height : value;



### （三）显示方式

#### 1、显示方式

#### 2、display属性

```html

```





## 四、Bootstrap起步

### （一）基本概念

#### 1、什么是Bootstrap

#### 2、构成

#### 3、Bootstrap目录说明

#### 4、Bootstrap相关技术

