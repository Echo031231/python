# 二分支结构if-else

'''
#判断用户输入数字的某个属性
s = eval(input("请输入一个整数:"))

if s % 3 == 0 and s % 5 == 0:
    print("这个数字既能被3整除,又能被5整除")
else:
    print("这个数字不能被3和5同时整除")
'''


'''
#判断用户输入数字的某个属性
#-----<表达式1> if <条件> else <表达式2>
s = eval(input("请输入一个整数:"))

token = "" if s % 3 == 0 and s % 5 == 0 else "不"
print("这个数字{}能够同时被3和5整除".format(token))
'''
    
