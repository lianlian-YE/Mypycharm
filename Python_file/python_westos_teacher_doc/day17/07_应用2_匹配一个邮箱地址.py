#!/usr/bin/env python
#coding:utf-8


""""
Name: 07_应用2_匹配一个邮箱地址.py
Date: 2018/06/17
Connect: xc_guofan@163.com
Author: lvah
Desc:


匹配163邮箱;  q@163.com

规则:
    6~18个字符，可使用字母、数字、下划线，需以字母开头;

"""
import re
from itertools import chain

s = """
你好，各种格式的邮箱入下所示：

    kevintian126@126.com 

2. 1136667341@qq.com 

3. meiya@cn-meiya.com 

4. wq901200@hotmail.com 

5. meiyahr@163.com

6. meiyuan@0757info.com 

7. chingpeplo@sina.com 

8. tony@erene.com.com

9. melodylu@buynow.com

具体释义入下：

1.163邮箱 




提供以@163.com为后缀的免费邮箱，3G空间，支持超大20兆附件，280兆网盘。精准过滤超过98％的垃圾邮件。 


2.新浪邮箱 




提供以@sina.com为后缀的免费邮箱，容量2G，最大附件15M，支持POP3。 



3.雅虎邮箱 




提供形如@yahoo.com.cn的免费电子邮箱，容量3.5G，最大附件20m，支持21种文字。 


4.搜狐邮箱 



提供以@sohu.com结尾的免费邮箱服务，提供4G超大空间，支持单个超大10M附件。强大的反垃圾邮件系统为您过滤近98%的垃圾邮件。 


5.QQ邮箱 




提供以@qq.com为后缀的免费邮箱，容量无限大，最大附件50M，支持POP3，提供安全模式，内置WebQQ、阅读空间等。 


"""



# 1. 找出可能是邮箱地址的， 返回一个列表;
pattern = r'\w{6,18}@\w+\.com'
email_li = re.findall(pattern, s)


# 2. 筛选出以字母开头的;
li = []
for email in email_li:
    li.append(re.findall(r'^[a-zA-Z].*', email))

# 将嵌套列表转换为非嵌套列表;
print(list(chain(*li)))


    # match方法的规则:
    #       如果找到符和规则的内容， 返回一个对象SRE_Match， 这个对象有group方法, 显示匹配到的内容;
    #       如果没有找到符和规则的内容， 返回一个None;

    # matchObj = re.match(r'^[a-zA-Z].*', email)
    # if matchObj:
    #     print(matchObj.group())