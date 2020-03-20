#替换空格
import re

def replace(data,target):
    new_date = ""
    for item in data:
        if item == " ":
            new_date += target
        else:
            new_date += item
    return new_date

print(replace("We Are Happy","%20"))



str = "We Are Happy"
str1 = str.replace(" ","%20")
print(str1)


str2 = "We Are Happy"
              #空格  替换内容 替换谁？
str3 = re.sub("\s+","%20",str2)
print(str3)