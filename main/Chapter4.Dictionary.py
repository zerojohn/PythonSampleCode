from copy import deepcopy
#del 方法删除字典中对应key的项
y = {"name":"zhuang","age":18}
del y['name']
print(y)

#in 来判断字典中是否包含键
if 'age' in y:
    print('age in y')


#format_map的使用
phonebook = {'name':'zhuangzhenlong','age':18}
s = "my name is {name}".format_map(phonebook)
print(s)


#字典方法
#1 clear 清空字典中所有的项
a_1 = {'name':'zhuangzhenlong'}
a_1.clear()
print(a_1)

#2 copy方法和deepcopy函数
a = {'name':"zhuangzhenlong",'family':['dengyang','zhuangmuyang']}
b = a.copy()
b['name'] = 'dengyang'
b['family'].remove('dengyang')
# b['family'] = ['1','2','3']
print(a)
print(b)
#从上面的输出结果可以看到，copy之后，直接赋值的语句不会改变被copy的对象，但是如果是就地改变，比如
#调用remove方法，那么被拷贝的对象也会跟着发生改变
a = {'name':"zhuangzhenlong",'family':['dengyang','zhuangmuyang']}
c = deepcopy(a)
c['family'].append('wangleping')
print(a)
print(c)
#从上面可以看到，做了deepcopy之后，就地改变的方法，也不会对被copy的对象a产生任何影响。


#3 fromkeys
a_3 = {'name':'zhuangzhenlong'}
#对已经有数据的字典调用这个方法没有任何意义
a_3.fromkeys(['age'])
print(dict.fromkeys(['age']))

#4 get
a_4 = {'name':'zhuangzhenlong'}
print(a_4.get('age'))

#5 items
a_5 = {'name':'zhuangzhenlong','age':'18','sex':'male'}
print(list(a_5.items()))

#6 keys
a_6 = a_5.keys()
print(a_6)

#7 pop
#获取与指定键相关联的值，并从字典中删除该键-值对
a_5.pop('name')
print(a_6)
a_5['height'] = 180
print(a_6)


#8 popitem
print(a_5.popitem())

#9 setdefault
a_9 = {'name':'zhuang'}
print(a_9.setdefault('name','dengyang'))
print(a_9.setdefault('age',1))

#10 update
a_10 = {'name':'zhuang'}
a_10_1 = {'name':"dengyang"}
a_10.update(a_10_1)
print(a_10)
a_10_2 = {'age':"2"}
a_10.update(a_10_2)
print(a_10)

#11 values
a_11 = {'name':'zhuangzhenlong','age':'18','sex':'male', 'height':'18'}
b_11 = a_11.values()
print(b_11)
a_11.pop('age')
print(b_11)
a_11['name'] = 'dengyang'
print(b_11)