from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import wx

url ='http://www.weather.com.cn/weather/101190101.shtml'
html = requests.get(url)
bs = BeautifulSoup(html.content, "lxml")                                            # 创建BeautifulSoup对象
data = bs.find('div', {'id': '7d'})                                                 # 找到id为7d的div
ul = data.find('ul')                                                                # 获取ul部分
li = ul.find_all('li')                                                              # 获取所有的li
tempH = []
tempL = []
Inf = []
Date = []
msg = []

for day in li:                                                                      # 对每个li标签中的内容进行遍历

    date = day.find('h1').string                                                    # 找到日期
    Date.append(date)
        
    inf = day.find_all('p')                                                         # 找到li中的所有p标签
    Inf.append(inf[0].string,)                                                      # 第一个p标签中的内容（天气状况）加到Inf中
        
    if inf[1].find('span') is None:
        temperature_highest = '暂无'                                                # 天气预报可能没有当天的最高气温，需要加个判断语句,来输出最低气温
    else:
        temperature_highest = inf[1].find('span').string                            # 找到最高温
    tempH.append(temperature_highest)                                               # 将最高温添加到tempH中
        
    temperature_lowest = inf[1].find('i').string                                    # 找到最低温
    tempL.append(temperature_lowest)                                                #将最低温添加到tempL中

for x in range(0,7):
    msg.append('%s的最高气温为: %s，最低气温为: %s，天气为: %s'%(Date[x],tempH[x],tempL[x],Inf[x]))





class Myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"南京天气预报",size=(420,165))
        panel = wx.Panel(self)
        
        label1 = wx.StaticText(panel,-1,msg[0])	
        label2 = wx.StaticText(panel,-1,msg[1])
        label3 = wx.StaticText(panel,-1,msg[2])
        label4 = wx.StaticText(panel,-1,msg[3])
        label5 = wx.StaticText(panel,-1,msg[4])
        label6 = wx.StaticText(panel,-1,msg[5])
        label7 = wx.StaticText(panel,-1,msg[6])


        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(label1,proportion=0)
        mainSizer.Add(label2,proportion=0)
        mainSizer.Add(label3,proportion=0)
        mainSizer.Add(label4,proportion=0)
        mainSizer.Add(label5,proportion=0)
        mainSizer.Add(label6,proportion=0)
        mainSizer.Add(label7,proportion=0)
        panel.SetSizer(mainSizer)




app = wx.App()
frame = Myframe()
frame.Show()
app.MainLoop()










