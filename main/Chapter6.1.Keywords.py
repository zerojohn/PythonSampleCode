#函数关键字非常重要，这章专门来讨论这个问题

#1 位置参数
#最普通的函数参数形式

def power(x):
    return x * x

print("位置参数运算结果是:{}".format(power(3)))


#2 默认参数
# 2.1默认参数要放在必选参数的后面
def power_2(x, n = 2):
    s = 1
    for j in range(n):
        s *= x
    return s

print("默认参数运算结果是:{}".format(power_2(3)))

# 2.2 当有多个默认参数时候，调用的时候可以像下面这样，用命名的形式指定其中某几个参数的值

def power_mitiple_default(x, y = 3, z = 4):
    return x * y * z

print("多个默认参数的运算结果是:{}".format(power_mitiple_default(1,z=5)))


# 必须牢记的一点是，默认参数必须指向不变的对象

def add_end(L=[]):
    # return L.append('END')
    L.append('END')
    return L

#在函数定义的时候，L的值就已经被计算出来了，那么后面用到的都是这个地址的值

print(add_end())
print(add_end())


#3 可变参数
def cal(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
#两种调用方法
cal(1,2,3)
cal(*(1,2,3))

#4 关键字参数
def person(name,age,**kv):
    print('name:{},age:{},other:{}'.format(name,age,kv))


#同样支持两种调用形式
person('longshao','18', sex = 'male',height = '180')
person('longshao',18,**{'sex':'male','height':'180'})


#5 命名关键字参数 因为普通的关键字参数，对传入的关键字没有做任何限制
def persong_(name,age,*,city,addr):
    print('{name},{age},{city},{addr}'.format(name=name,age=age,city=city,addr=addr))

person('zhuangzhenlong',18,city = 'wuhan',addr ='guanggu')

#!!!!如果函数中已经定义了可变参数，那么后面的命名关键字参数就不用再带上星号了
def person2(name, age,*kk,city,addr):
    print('{},{},{},{},{}'.format(name,age,kk,city,addr))
person2('zhuang',18,'xia','xie',city='wuhan',addr='guanggu')


#!!!关键字参数也可以有缺省值
def person3(name,age,*,city='wuhan',addr):
    print(name,age,city,addr)
person3('zhuang',18,addr='guanggu')

#参数组合
#参数组合的顺序必须是 必选参数(位置参数),可变参数，命名关键字参数，关键字参数

def product(*x):
    s = 1
    if len(x) <= 0:
        raise TypeError
    for i in x:
        if i == 0:
            break
        else:
            s *= i
    return s

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
