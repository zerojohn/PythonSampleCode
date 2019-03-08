from string import Template
from math import pi

tmpl = Template("Hello ,$who! $what enough for ya?")
tmpl.substitute(who="Mars", what="Dusty")


#编写新代码时，应选择使用字符串方法format

#1 极简模式
print("{},{} and {}".format("first","second","third"))

#2 索引配置模式
print("{1},{2},{0}".format("first", "second", "third","forth"))

#3 命名字段配置模式
print("{name} is approximately {value:.2f}".format(value=pi, name="π"))

#4 一种简写的命名字段配置模式
name = 'zhuangzhenlong'
print(f"{name} is approximately {pi}")

#5 替换字段名
#5.1 自动匹配
print("{foo} {} {bar} {}".format(1,2,foo="long",bar="shao"))

#5.1 手动匹配
print("{foo} {1} {bar} {0}".format(1,2,foo="long",bar="shao"))

#要么全是自动匹配，要么全是手动匹配，否则会变得混乱不堪

#6 替换字段名中的一部分
fullname = ['zhuang','zhen',"long"]
print("{name[1]}".format(name=fullname))
print(f"{fullname[1]}")


#7 基本转换
print("{pi!s} {pi!a} {pi!r}".format(pi="π"))
print("{pi:.2f}".format(pi=pi))

#8 字符串方法
#8.1 center 通过在两边填充字符让字符串居中
a8 = "zh"
print(a8.center(5))

print("zh" in a8)

#8.2 find方法 可以指定起点和终点，但是在查找的时候不包括终点

a8_2 = "zhuangzhenlong"
print(a8_2.find("zh",3))

#8.3 join方法 与split是相反的操作
a = "+".join(('1', '2'))
print(a)

#8.4lower方法

#8.5 replace方法
a8_5 = "zhuangzh"
print(a8_5.replace('zh','deng'))
print(a8_5)

#8.6 split

#8.7 strip 将字符串首尾空白去掉

#8.8 translate  只能替换字符，但是可以一次替换多次，并不是说replace只替换第一次遇到的那个参数
#打个比方，要用replace替换a8——5中的z和u要调用两次replace


table = str.maketrans('cs','kz',' ')
#第三个参数表示删除指定字符
a8_8 = 'zhuang zhen long cs '
print(a8_8.translate(table))
