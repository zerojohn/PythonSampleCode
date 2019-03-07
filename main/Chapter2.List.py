#字符串就是由字符组成的序列
#python没有定义字符变量，一个字符就是长度为1的字符串
test_string = "zhuang"
print(test_string[0])

##############################切片#######################################
#切片操作
numbers = [1,2,3,4,5,6,7,8,9,10]

#1 正常切片
print("第一个到第三个的切片是:", numbers[0:3])

#2 用负数作为索引，表示从后往前
print("倒数第三个到倒数第二个", numbers[-3:-1])

#3 注意，负数作为索引时候，只有一种方式可以包含最后一个元素进来
print("倒数第三个到倒数第一个", numbers[-3:])

#[-3:0]这样的写法是会报错的，因为切片的第一个元素必须位于第二个元素前面，否则就是空序列
print("[-3:0] 这种写法得到的结果是",numbers[-3:0])

#可以省略切片的开头或者结尾
print("完整的序列是",numbers[:])

#可以采用正负数都包含的写法
print("整数第一个到倒数第三个",numbers[0:-2])

#上面都是针对的单步步长，还可以手动设置更大的步长
print("按照步长3提取争取序列中的相应元素:",numbers[::3])

#步长不能为0，但是可以为负数，此时切片从右向左提取元素
print("提取第八个到第三个之间的元素",numbers[7:1:-1])

#python会自动根据步长是正数还是负数来决定索引的方向
print("正向切片",numbers[::2])
print("反向切片", numbers[::-2])

##############################序列的方法#######################################
#1 加法
# 序列加法,但是不同类型的序列不能相加
print("[1,2,3] + [4,5,6] 的结果",[1,2,3] + [4,5,6])

#2 乘法
print("[1] 10次",[1] * 10)
# 初始化有长度但是无内容的序列
m = [None] * 10
print(m)

#3 成员资格，判断特定值是否在序列中 使用运算符in
print("&&&" in "&&&^^^")

#4 长度，最小值，最大值

#################################列表操作####################################
#列表
#list函数,字符串转字符列表
print(list("zhuang"))
#也可以将字符数组转成字符串
name = ['z', 'h', 'u', 'a', 'n', 'g','zhen']
print("".join(name))

#基本列表操作
#1 修改列表
j = ['1', '2']
j[0] = '3'
print(j)

#删除元素
del j[0]
print(j)

#切片复制，可以将切片替代为长度不同的序列
qiepianstr = list("12345")
qiepianstr[1:] = list("zhenlong")
print(qiepianstr)
#也可以通过切片进行插入操作
qiepianstr[0:0] = list('sds')
print(qiepianstr)
#也可以通过切片进行删除操作
qiepianstr[-1:-3] = list('abc')
print(qiepianstr)


#列表的方法
#1 append ,无返回值，就地
lst = [1,2,3,4,5,6,7,8,9]
lst.append('a')
print(lst)

#2 clear 清空列表
# lst.clear()
# print(lst)

#3 copy 深度拷贝
# print(lst.clear())

#4 count 指定元素在列表中出现的次数

#5 extend使用一个序列来扩充另外一个序列
a5 = [1,2,3]
b5 = [4,5,6]
print(a5.extend(b5))
# a5[2:2]=b5
# print(a5)

#6 index 在列表中查找第一次出现指定值的索引

#7 insert 指定位置插入元素
a7 = [1,2,3]
a7.insert(2,4)
print(a7)

#8 pop 弹出元素
a8 = [1,2,3]
a8.pop(1)
print(a8)

#9 remove 删除指定元素，找不到会报错
a9 = [1,2,3]
a9.remove(1)

#10 reverse

#11 sort

#12 sorted

#高级的排序 sort可以接收两个参数 key和reverse
a12 = ['abc','de','fghi','jklmno','q']
a12.sort(key=len,reverse=False)
print(a12)