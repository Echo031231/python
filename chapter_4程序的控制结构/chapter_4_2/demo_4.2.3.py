#多分支结构if-elif-else

#将百分制成绩转换为五分制
score = eval(input("请输入分数："))

if(score >= 90):
    grade = 'A'
elif(score >= 80):
    grade = 'B'
elif(score >= 70):
    grade = 'C'
elif(score >= 60):
    grade = 'D'
else:
    grade = 'E'
print("转换后的等级为:{}".format(grade))











