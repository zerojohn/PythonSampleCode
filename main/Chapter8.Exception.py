#异常

# raise语句

# raise Exception()
#
# raise Exception('出错了')

#自定义异常

class SomeCustomException(Exception):pass

# 捕获异常

# 开启异常抑制功能
try:
    1 / 0
except ZeroDivisionError:
    print('异常到这里就为止了')

# 也可以继续抛出
# try:
#     1 / 0
# except ZeroDivisionError:
#     raise


#在放生异常的时候引发别的异常，下面的示例中引发ZeroDivisionError异常的时候又抛出了ValueError异常
# try:
#     1 / 0
# except ZeroDivisionError:
#     raise ValueError

#也可以禁用之前传过来的异常 ，下面例子中ZeroDivisionError被抛弃了。
# try:
#      1 / 0
# except ZeroDivisionError:
#     raise ValueError from None

#多个异常
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
# except ZeroDivisionError:
#     print('除数不能为0')
# except TypeError:
#     print('只能用数相除')

#另外一种写法
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
# except (ZeroDivisionError,TypeError):
#     print('除数不能为0，也不能是字母或者其他类型，只能是整数')

# 捕获异常
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
# except (ZeroDivisionError,TypeError) as e:
#     print('除数不能为0，也不能是字母或者其他类型，只能是整数')
#     print(e)

#else子句 当异常没有发生时候执行
# while True:
#     try:
#         x = int(input())
#         y = int(input())
#         print(x / y)
#     except Exception as e:
#         print('Invalid input',e)
#         print('Please input again')
#     else:
#         break

#finally
x= None
try:
    x = 1/0
except  ZeroDivisionError:
    print("division zero")
finally:
    del x