#构造函数
#__init__
class Foobar:
    def __init__(self):
        self.somevar = 42

f = Foobar()
print(f.somevar)

# 带参数的构造函数
class Foobar1:
    def __init__(self,value = 42):
        self.somevar = value

f1 = Foobar1("This is a test")
print(f1.somevar)


#调用未关联的超类函数
class Father:
    def __init__(self):
        self.hungry = False
    def eat(self):
        if self.hungry == False:
            print('I\'m full')
        else:
            print('I\'m hungry')

class Child(Father):
    def __init__(self):
        Father.__init__(self)
        self.sound = 'aaaaa'


c = Child()
c.eat()

#使用函数super

class Daughter(Father):
    def __init__(self):
        super().__init__(self)
        self.sound = 'yinyin'

    def sing(self):
        print(self.sound)

#基本的序列和映射协议 __getItem__

def check_index(key):
    if not isinstance(key,int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    def __init__(self,start = 0,step = 1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, item):
        check_index(item)
        try:
            return self.changed[item]
        except KeyError:
            return self.start + item * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])

#从list str dict派生
class CounterList(list):

    def __init__(self, *kwargs):
        super(CounterList, self).__init__(*kwargs)
        self.counter = 0

    def getCounter(self):
        return self.counter

    def __getitem__(self, item):
        self.counter += 1
        super().__getitem__(item)

c = CounterList(range(10))



print(range(10))


#关于self的用法，不一定非要使用self，不使用self也可以，可以用别的值来进行代替
#在方法定义的时候必须传入，在方法调用的时候会自动传入实例本身。
class Test:
    def __init__(x):
        x.attr = 3

    def Hello(x,y):
        x.attr = y

    def get_attr(x):
        print(x.attr)

t = Test()
t.get_attr();
t.Hello(100)
t.get_attr()
#实际相当于这样在调用
Test.get_attr(t)

#函数property

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self,size):
        self.width ,self.height = size

    def get_size(self):
        return self.width,self.height

    size = property(get_size,set_size)

r = Rectangle()

print(r.size)
print(r.width)

class Property_Test:

    def get_fee(self):
        return self._fee

    def set_fee(self,value):
        self._fee = value


    x = property(get_fee,set_fee)

s = Property_Test()
s._fee = 3
s.x = 4
print(s._fee)

class Property_Test1:



    @property
    def fee(self):
        return self._fee
#注意此处方法必须和上面的get方法的方法名完全相同
    @fee.setter
    def fee(self, value):
        self._fee = value

P = Property_Test1()
P.fee = 4

class Bird:
    def __init__(self,s = 'jojo'):
        self.sound = s

    def sounds(self):
        print(self.sound)

class kkk(Bird):
    def __init__(self):
        super(kkk, self).__init__('haha')
        self.name = 's'

k = kkk()
k.sounds()


#__getattr__

class Rec:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __getattr__(self, item):
        if item == 'size':
            return self.width,self.height
        else:
            raise TypeError

    # def __getattribute__(self, item):
    #     print('Hello')
    #     return 3

r = Rec(100,100)
# __getattr__只有在属性不存在的情况下才会被调用，如上面的Rec类如果调用
# r.size 那么就会调起这个方法

# __getattribute__无论属性是否存在，都会被调用

#数据描述符