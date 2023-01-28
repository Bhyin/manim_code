# manim code
#### 用来保存一些manim项目的代码。

---

我惯用的manim版本是manimGL，但由于一些无法解决的问题而暂时改用manimCE，等到manimGL的1.7.0版本release之后会继续使用manimGL。

## 一些manim学习资料

### 官方文档

我不推荐到网上搜索教程，因为过时的教程太多了。

manim的最基本的配置和使用方法在官方文档中都有详细说明。

两个manim版本的官方文档路径：
- <a href="https://docs.manim.org.cn">manimGL官方中文文档</a>
- <a href="https://docs.manim.community">manimCE官方文档</a>

根据你选择的版本看对应文档查阅即可。不过无论使用哪个版本，两个文档都应该看看，一些内容可以互为补充。

### 源代码

manim中常用的类、方法和函数都有详细的docstring，点进源码就可以查看，十分便捷。

另外，学习一个Mobject如何使用，最好的办法就是把它在construct里实例化一个mobject，然后它add到Scene中，观察它的形状；或调用它的方法，观察它的行为；对于Animation，自然是要传进play方法里一览效果。

凭借实验的方式，学习效果绝对比只查文档和光看源码更好。

PS: manimGL 在1.6.1以前，类的的属性是靠一个CONFIG字典存储的，这导致manimGL的源码有些难读。不过去年十二月Grant把manimGL的CONFIG给Kill了，属性整合到__init__方法里，肉眼可见的可读性提升。辛苦Grant了。


### 其他学习资源
- <a href="https://github.com/3b1b/videos">3Blue1Brown的视频源代码</a>
- <a href="https://github.com/manim-kindergarten">manim-kindergarten的github主页</a>: manim-kindergarten是B站上一群热爱manim和科普的UP主建立的组织。
- <a href="https://www.bilibili.com/video/av331584599/?vd_source=a010c8b6df60731142f8ef398ab078d3">一个updater的教程</a>


---

要说的就这么多，我继续鸽了。

