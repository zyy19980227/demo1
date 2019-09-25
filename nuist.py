import base64
import requests
'''
在同目录下创建一个login.log，
第一行输入登录号码，第二行输入运营商，第三行输入密码
电信ChinaNet
移动CMCC
联通Unicom
学号NUIST
'''
Line = []
for line in open('login.log'):
    line1=line.strip('\n')
    Line.append(line1)

USER_ACCOUNT = Line[0]
DOMAIN_SELECTION = Line[1]
USER_PASSWATD = Line[2]

#登录地址
post_addr="http://a.nuist.edu.cn/index.php/index/login"

#构造头部信息
post_header={
    'Host': 'a.nuist.edu.cn',
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    
    'Accept-Language':'zh-CN,zh;q=0.9',
    
    'Accept-Encoding': 'gzip, deflate',
    
    'Content-Type': 'application/x-www-form-urlencoded',
    
    'X-Requested-With':'XMLHttpRequest',
    
    'Referer':'http://a.nuist.edu.cn/index.php?url=aHR0cDovL2Nvbm4xLm9wcG9tb2JpbGUuY29tL2dlbmVyYXRlXzIwNA==',
    
    'Content-Length': '70',

    'Cookie':'sunriseUsername='+USER_ACCOUNT+';sunriseDomain='+DOMAIN_SELECTION+';sunriseRememberPassword=true;\
    sunrisePassword='+USER_PASSWATD+';PHPSESSID=qtfrmslgdjlfk3jakj18fvjlq4;think_language=zh-CN',

    'Connection':'keep-alive',
}

'''
password在post的参数中为base64编码
'''
post_data={'domain':DOMAIN_SELECTION,
           'enablemacauth':'0',
           'password':base64.b64encode(USER_PASSWATD.encode()),
           'username':USER_ACCOUNT
          }
#发送post请求登录网页
z=requests.post(post_addr,data=post_data,headers=post_header)
#z.text为str类型的json数据因此先编码成byte类型在解码成unicode型这样就可以正常输出中文
s=z.text.encode('utf-8').decode('unicode-escape')
print(s)
