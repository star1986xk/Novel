#导入相关包
import requests
from bs4 import BeautifulSoup
import time
import  pandas as pd
from fake_useragent import UserAgent
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

#爬取500篇小说作为训练数据
class spider(QThread):
    sig_one_end = pyqtSignal(str)
    sig_item_end = pyqtSignal(tuple)
    sig_end = pyqtSignal(str)

    def __init__(self, start_id=None, end_id=None, filename=None):
        super(spider, self).__init__()
        self.start_id = start_id
        self.end_id = end_id
        self.filename = filename

    def crawling_data(self,i):
        ua=UserAgent()
        headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':ua.chrome#设置请求头
        }#设置请求头#可以改成自己的useragent
        self.txts=[]
        try:
            url="https://www.biquge.lu/book/"+str(i)+"/"#网站笔趣阁
            self.sig_one_end.emit('正在爬取数据······')
            response=requests.get(url,headers=headers,timeout=20)
            response.encoding = 'gbk'
            soup=BeautifulSoup(response.text,"lxml")
        except Exception as e:
            print(e)
        # print(so.title.text)
        return soup#函数返回网站返回的内容
    def organize_title(self,soup):#整理小说所有章节标题
        title = []  # 标题
        num = []  # 序号
        try:
            last=soup.find_all('dd')[0].a.attrs['href'].split('/')[3].split('.')[0]#最新一章序号
            self.sig_one_end.emit('数据清洗······')
            for i in range(int(last)+200):
                try:
                    if len(soup.find_all('dd')[i].text.split(" "))==2:
                        title.append(self.txts[1].find_all('dd')[i].text.split(" ")[1])#标题
                    elif len(soup.find_all('dd')[i].text.split(" "))==1:
                        title.append('')
                    else:
                        txtsii=''
                        for ii in range(1,len(soup.find_all('dd')[i].text.split(" "))):
                            txtsii=txtsii+soup.find_all('dd')[i].text.split(" ")[ii]
                        title.append(txtsii)
                    num.append(soup.find_all('dd')[i].a.attrs['href'].split('/')[3].split('.')[0])
                    # print(i)
                except:
                    break
        except:
            title.append(" ")
            num.append(" ")
        df = pd.DataFrame({
            'title': title,
            'num': num})#将序号和标题放入DataFrame
        df.drop_duplicates(inplace=True)#去重
        text = ''
        for iii in range(len(df)):
            text = text + df['title'][iii]#所有标题作为一个元素
        return text#返回该小说所有标题

    def organize_data(self,soup):#整理小说名，简介等相关数据
        novel=soup.title.text.split('无弹窗')[0]  # 小说名
        description=soup.find_all('meta', attrs={"property": "og:description"})[0]['content'].replace("\u3000", "").strip()  # 简介
        category=soup.find_all('meta', attrs={"property": "og:novel:category"})[0]['content'].replace("\u3000", "")  # 小说类型
        author=soup.find_all('meta', attrs={"property": "og:novel:author"})[0]['content'].replace("\u3000", "")  # 作者
        status=soup.find_all('meta', attrs={"property": "og:novel:status"})[0]['content'].replace("\u3000", "")  # 状态（连载、完结）
        type=soup.find_all('meta', attrs={"property": "og:type"})[0]['content'].replace("\u3000", "")  # 类型
        update_time=soup.find_all('meta', attrs={"property": "og:novel:update_time"})[0]['content'].replace("\u3000", "")  # 更新时间
        title=self.organize_title(soup)
        return novel,description,category,author,status,type,update_time,title

    def run(self):
        words = []
        start = self.start_id
        end = self.end_id
        for i in range(int(start), int(end)):  # range里的数值是小说在笔趣阁网站中的id
            soup = self.crawling_data(i)  # 获取网站返回的内容
            txts = self.organize_data(soup)
            self.sig_item_end.emit(txts)
            words.append(txts[1] + txts[7])  # 简介和标题
            time.sleep(3)  # 休息3秒，防止反扒
        filename = self.filename
        file = open(filename, 'w', encoding='utf-8')
        for value in words:
            file.write(value)
            file.write('\n')
        file.close()  # 将爬取并整理好的数据保存
        self.sig_end.emit('抓取结束，保存'+self.filename+'成功')


