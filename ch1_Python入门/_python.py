#单行注释

'''
多行
注释
'''

#数字变量
a = 1
b = 2
c = 2.3
d = 2+3j

print(a+b)
print(a+c)
print(d)

print(type(d))

#函数内部控制全局变量 —— global
def fun():
    global x
    x = "Yes"

fun()
print(x)

#字符串
a = "hello "
b = "world!"
c = 100

print(a+b)
d = "My point is {}"
print(d.format(c))#字符串与数字级联

print(a[1])
print(a[1:3]) #左闭右开
print(a[-3:-1]) #左开右闭
print(a.replace("ll", "LL")) #替换
print(a.split("ll")) #拆分
print(a.lower()) #小写
print(a.upper()) #大写

x = "ll" in a #在其中
print(x)

#运算符
print(3/2)
print(3//2) #整除
print(2**3) #幂


#列表
myList = [123, ['abc', 234, 345]]
myList.append('xyz') #末尾追加
myList.insert(1, 0) # [1]位置添加
print(myList)

YourList = myList.copy() #复制
YourList.pop()
YourList[-1].append('ooo')
print(myList)

YourList = myList #引用

YourList.extend(myList) #添加到末尾

#元组
myTuple = (1, 'a') #不可更改
YourTuple = (1,) #只有一个元素的元组要加逗号

del myTuple #元组只能整体删除

#集合
myset = {1, 'a', 2, 3}
myset.add('b') #添加一个
myset.update(['x', 'y', 0]) #添加多个
print(myset)

#字典
mydict = {
    'a': 123,
    'b': 456,
    789: 'c'
}
print(mydict['a'])
mydict.pop(789)
del mydict['b']
print(mydict)

# if-else
if 10>3 or 10>11:
    print("hello world")
elif 10 > 12:
    print("no")

# for
for i in range(5):
    print(i)
else:
    print(100)
