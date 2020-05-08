#词云图
import re
import jieba.posseg as jp
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from wordcloud import WordCloud
import pandas as pd
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from MyFigure import MyFigure
from gensim import corpora,models
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ciyun(QThread):
    sig_one_end = pyqtSignal(str)
    sig_img_end = pyqtSignal(list)

    def __init__(self, name=None):
        super(ciyun, self).__init__()
        self.name = name
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

    def call_id(self,name):#name是小说名
        #在该网站按小说名搜索小说输出网址
        ua=UserAgent()
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':ua.chrome
            }
        urll='https://so.biqusoso.com/s.php?ie=utf-8&siteid=biquge.lu&q='
        url=urll+name
        try:
            response=requests.get(url,headers=headers,timeout=10)
            response.encoding = 'UTF-8'#搜索这里是utf8
            soup=BeautifulSoup(response.text,"lxml")
            id=soup.find_all('li')[1].find_all('span',attrs={'class':"s2"})[0].a.attrs["href"]#提取目标网址id
        except Exception as e:
            id=e
        return id
    def get_soup(self,id):
        url = "https://www.biquge.lu/book/" + str(id.split("/")[6]) + "/"  # 笔趣阁
        ua=UserAgent()
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':ua.chrome
            }
        response = requests.get(url, headers=headers, timeout=20)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, "lxml")
        return soup,url
    def get_data(self,soup):
        novel = soup.title.text.split('无弹窗')[0]  # 小说名
        description = soup.find_all('meta', attrs={"property": "og:description"})[0]['content'].replace("\u3000",
                                                                                                        "").strip()  # 简介
        category = soup.find_all('meta', attrs={"property": "og:novel:category"})[0]['content'].replace("\u3000",
                                                                                                        "")  # 小说类型
        author = soup.find_all('meta', attrs={"property": "og:novel:author"})[0]['content'].replace("\u3000",
                                                                                                    "")  # 作者
        status = soup.find_all('meta', attrs={"property": "og:novel:status"})[0]['content'].replace("\u3000",
                                                                                                    "")  # 状态（连载、完结）
        type = soup.find_all('meta', attrs={"property": "og:type"})[0]['content'].replace("\u3000", "")  # 类型
        update_time = soup.find_all('meta', attrs={"property": "og:novel:update_time"})[0]['content'].replace(
            "\u3000", "")  # 更新时间
        title = self.get_title(soup, description)
        return title, novel, description, category, author, status, type, update_time
    def get_title(self,soup,description):
        title = []  # 标题
        num = []  # 序号
        for i in range(100000):
            try:
                if len(soup.find_all('dd')[i].text.split(" ")) == 2:
                    title.append(soup.find_all('dd')[i].text.split(" ")[1])  # 标题
                elif len(soup.find_all('dd')[i].text.split(" ")) == 1:
                    title.append('')
                else:
                    txtsii = ''
                    for ii in range(1, len(soup.find_all('dd')[i].text.split(" "))):
                        txtsii = txtsii + soup.find_all('dd')[i].text.split(" ")[ii]
                    title.append(txtsii)
                num.append(soup.find_all('dd')[i].a.attrs['href'].split('/')[3].split('.')[0])
                # print(i)
            except:
                break
            df = pd.DataFrame({
                'title': title,
                'num': num})
            df.drop_duplicates(inplace=True)
            text = ''
            for iii in range(len(df)):
                text = text + df['title'][iii]
            text = text + description
        return text
    def stop_words(self,path):
        file1 = open(path, encoding='utf-8')
        stopwords = []  # 创建停用词列表
        for line in file1.readlines():
            stopwords.append(line.strip())
        file1.close()
        return stopwords
    def cut_words(self,text,stopwords):
        words = re.sub(r'[^\u4e00-\u9fa5]+', '', text)  # 把非汉字的字符全部去掉
        flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd')  # 词性
        txt = []
        for i in jp.cut(words):
            if i.word not in stopwords and i.flag in flags and len(i.word) > 1:
                txt.append(i.word)
        return txt

    def lda_result(self,lda, txt):
        dictionary = corpora.Dictionary([txt])  # 构建词典
        doc_bow = dictionary.doc2bow(txt)  # 文档转换成bow
        doc_lda = lda[doc_bow]  # 得到新文档的主题分布
        return doc_lda

    def call_ldamodel(self,path):
        model_name = path  # 模型名称
        lda = models.ldamodel.LdaModel.load(model_name)  # 调用训练好的模型
        return lda

    def analysis(self,name):
        lda = self.call_ldamodel('LdaModel(num_terms=164682, num_topics=8, decay=0.5, chunksize=2000).model')
        subject = [(0, '感情主题'), (1, '政客主题'), (2, '探索真相主题'), (3, '帮派斗争主题'), (4, '战争与贵族主题'),
                   (5, '历史英雄主题'), (6, "智力斗争主题"), (7, '异世界主题')]
        stopwords=self.stop_words('stopwords.txt')
        try:
            id=self.call_id(name)
            soup=self.get_soup(id)[0]
            text=self.get_data(soup)
            txt=self.cut_words(text[0],stopwords)
            doc_lda = self.lda_result(lda, txt)
            url = self.get_soup(id)[1]

            self.sig_one_end.emit("作品名称：%s" % text[1])
            self.sig_one_end.emit("作者：%s" % text[4])
            self.sig_one_end.emit("状态：%s" % text[5])
            self.sig_one_end.emit("简介：%s" % text[2].replace(" ", ""))
            self.sig_one_end.emit("小说类型：%s" % text[3])
            self.sig_one_end.emit("更新时间：%s" % text[7])
            # print("该小说主题分布如下（主题序号，该主题权重）")
            #         lda_sorted=sorted(doc_lda, key=lambda tup: tup[1],reverse=True)
            #         print (sorted(doc_lda, key=lambda tup: tup[1],reverse=True))#排序从大到小
            for topic in sorted(doc_lda, key=lambda tup: tup[1], reverse=True):
                subject_type = subject[topic[0]]
                # print("主题类型：%s"%subject_type[1])
                # print ("该主题最常见的前10个词语分布为：%s\n"%(lda.print_topic(topic[0],10)))
                self.sig_one_end.emit("""主题类型：%s
            该主题最常见的前10个词语分布为：%s\n""" % (subject_type[1], lda.print_topic(topic[0], 10)))

        except Exception as e:
            print(e)
        return txt
    def run(self):
        word_list=self.analysis(self.name)#获取原词文件
        result = " ".join(word_list)
        # print(result)
        # 4.生成词云
        wc = WordCloud(
            font_path=r'C:\Windows\Fonts\simfang.ttf',     #字体路径
            background_color='white',   #背景颜色
            width=1000,
            height=600,
            max_font_size=100,            #字体大小
            min_font_size=30,
            max_words=200
        )
        wc.generate(result)
        wc.to_file('%s词云图.png'%self.name)    #图片保存

        fig_list = []
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.imshow(wc)
        ax.set_xticks([])
        ax.set_yticks([])
        self.canvas.draw()
        fig_list.append(self.canvas)
        self.sig_img_end.emit(fig_list)