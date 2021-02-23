#定义一个数字可以自己控制大小
list_error = []
cookie_list = []
cookie = 'BBBBBBBB'
i = 0
scanf = input('[+]please input your name:')
#check_scanf函数用于检测输入长度可以用该函数限制列表长度类似于自定义一个20大小的的数组
def check_scanf(scanf):
    if len(scanf)>20:
        return 'F'
    elif len(scanf)<= 20:
        return 'T'
#添加cookie也就是canary的值
if check_scanf(scanf) == 'T':
    for i in range(len(list(scanf))):
        list_error.append(scanf[i])
    list_error.append(cookie)
elif check_scanf(scanf) =='F':
    for i in range(len(list(scanf))):
        list_error.append(scanf[i])
        i+=1
        if i == 21:#这个i是数组的大小可以自定义修改主要思想就是在数组最后添加cookie值
            list_error.append(cookie)       
#判断是否发生栈溢出
#检测最后8位canary的值是否合法
#按照定义的数组大小，cookie的值默认插在最后如果发生溢出
# 那么cookie的值只会插在原定义数组大小的末尾溢出的部分则会填充到cookie后面
def check(canary):
    if canary != 'B':
        return 'F'
    elif canary =='B':
        return 'T'
canary = list(list_error[-1])
for j in range(len(canary)):
    if check(canary=canary[j]) == 'T':
        cookie_list.append('T')
if len(cookie_list)==8:
    print('[+]Pass!!')
else:
    print('[+]*******  Warning Stack overflow！！！*******')
#print(list_error)
#print(len(list_error))
#print('[+]cookie_list:',cookie_list)
