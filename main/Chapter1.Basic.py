import math
import cmath

#一般除法，除法的结果是小数

print("3/2 的结果是", 3/2)

#取整的运算符号是//
print("3//2 的结果是", 3//2)

#求余运算符号是%
print("3%2 的结果是", 3%2)

#乘方运算 **,乘方还有一个函数pow
print("2的3次方 2 **3 的结果是", 2**3)

#变量 python中的变量必须在使用前就给他赋值，变量本身没有默认值
x = 2

#input函数，返回值是输入的值
age = input("请输入你的年龄: ")
print("你的年龄大小是:",age)

#pow函数
pow_x = pow(2,3)
print(pow_x)

#abs函数
abs_x = abs(-10)
print(abs_x)

#round函数
round_x = round(5/2)
print(round_x)

#floor, ceil方法
print(math.floor(2.5), math.ceil(2.5))

#sqrt方法
print(math.sqrt(4), cmath.sqrt(-4))

#str repr 方法
print(repr("hello\nworld"))
print(str("hello\nworld"))
print("hello\nworld")

#字符串拼接 使用+号
x_str = "zhuang" + "zhen" + "long"
print(x_str)

print("zhuang\
zhen")

print(r'C:\Program Files\foo\bar' '\\')