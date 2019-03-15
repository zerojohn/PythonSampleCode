# 1 多态
# 2 封装
# 3 继承

# 类
# 创建自定义的类

class Person:

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def greeting(self):
        print("Hello world! I'm {}".format(self.name))

# 内部方法 加上两个下划线
    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print('the secret message is:')
        self.__inaccessible()


# 属性作用域的问题

class MemberCenter:
    member = 0
    def init(self):
        MemberCenter.member += 1

m1 = MemberCenter()
m1.init()
print(MemberCenter.member)
m2 = MemberCenter()
m2.init()
print(MemberCenter.member)


#此处改变的不是类变量的值，而是m2的属性member值

m2.member = 1
print(m1.member)
print(m2.member)

# 指定超类
class Father:
    def init(self):
        self.blocked = []

    def filter(self,x):
        return [y for y in x if y not in self.blocked]

class Child(Father):
    def init(self):
        self.blocked = ['Adam',]

f = Father()
f.init()
print(f.filter(['Adam','Lilei']))

c = Child()
c.init()
print(c.filter(['Adam','Lilei']))

# issubclass 判断父子类关系

print(issubclass(Child,Father))

# __bases__
print(Child.__bases__)

# isinstance
print(isinstance(c,Child))

#多重继承 不到万不得已，不要使用 因为方法会被覆盖

#hasattr
print(hasattr(c,'filter'))

#getattr 第三个参数的意思是当对应的属性方法不存在的时候，返回的值
print(getattr(c,'filter',None))

#setattr 和上面的getattr作用相反
p = Person()
p.set_name('zjhuag')
setattr(p,'name','zhuang')
print(p.get_name())

#callable
print(callable(getattr(c,'filter',None)))

#__dict__属性，查看对象储存的所有值
print(p.__dict__)


#抽象基类 不能被实例化的基类
from abc import  ABC,abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

# 一个很危险的方法 register，表明了成为子类的意图，但是却不一定实现了这个方法
class Clam:
    pass

Talker.register(Clam)

print(issubclass(Clam,Talker))

c = Clam()

print(isinstance(c,Talker))

c.talk()