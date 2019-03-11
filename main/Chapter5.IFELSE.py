#1 自定义分隔符 seq
print("my","name","is","zhuangzhenlong",sep=' ')

#2 自定义结束符 end
print("hello world!",end='\n')

#导入时模块重命名 as
import math as example
from math import sqrt as foobar

#3-1新概念 序列解包,序列包含的元素个数必须与左边列出的目标个数相同，否则python会引发异常。
x,y = (1,2)
x, y = y, x
print(x,y)

# 使用*可以无需保证值和变量的个数相同,*号用来收集多余的值
a,b,*test = [1,2,3,4]
print(a, b, test)

#3-2 链式赋值
x = y = 3

#3-3 增强赋值
x *= 3
x += 3

y = 'zhuang'
# and not or
print(not True or not False)

#assert 断言
age = -1
# assert 0 < age  <100 ,'age must dayu 0'
print(ord('a'))
print(chr(97))

#zip函数
a = (1,2,3)
b = (4,5,6)
for x in zip(a,b):
    print(x)
print(list(zip(a,b)))

#enumerate
u = [1,2,3]
for index,value in enumerate(u):
    print(index,value)

#reversed
p = reversed(u)
print(p)
print(list(p))


#简单推导
print([x*x for x in range(10)])

#稍微复杂一点的
print([x*x for x in range(0,10) if x % 3 == 0])

#再复杂一点的
print([(x,y) for x in range(3) for y in range(3)])
#此处会产生九个结果，取了一个全交集

#还可以更复杂
A = ['Alex','Bob',"cherry"]
B = ['Adam','bMW','Charlie']
print([x+','+y for x in A for y in B if x.lower()[0] == y.lower()[0]])


#再谈del方法
r = [1,2,3]
w = r
del r[0]
print(w)

del r
print(w)