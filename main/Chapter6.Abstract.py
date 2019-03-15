def square(x):
    'Caculates the square of the number x.'
    return x * x

print(square.__doc__)


#关键字参数
def hello_1(name,greeting):
    print('{} {}'.format(name,greeting))

hello_1('hello','world')

hello_1(greeting='world',name='zhuang')

#关键字最大的有点在于可以指定默认值

def hello_2(greeting='hello',name='zhuang'):
    print('{} {}'.format(name,greeting))

#关键字参数和位置参数混合,位置参数必须在前面，否则编译器可能出现无法判断对号入座的情况
#如果关键字参数在前，那么会导致在函数调用的时候，如果出现调用的参数比定义的参数少，不知道替换哪一个

def hello_3(greeting,name='zhuang'):
    print('{} {}'.format(greeting,name))

#收集参数，这点在第五章赋值的时候也有讲到
def print_params(*params):
    print(params)

print_params(1,2,3)


#收集参数可以不放在最后
def print_params1(x,*params,z = 5):
    print(x,params,z)
print_params1(1,2,3,4,5)
print_params1(1,2,3,4,z=5)

#收集关键字参数，得到的结果是一个字典。
def print_keyparams(**params):
    print(params)

print_keyparams(x=1,y=2,z=3)

#综上所述，参数列表中的顺序应该是位置参数 > 收集参数 > 关键字参数

#分配关键字
# 列表分配
array = [1,2]
def add(x,y):
    return x + y

add(*array)

testdic = {'name':'zhuang','greeting':'hello'};
hello_3(**testdic)

def foo(x,y,z,m=0,n=0):
    print(x,y,z,m,n)
array_1 = [1,2,3,4,5]
dic_1 = {'m':1,'n':2}
foo(*array_1)