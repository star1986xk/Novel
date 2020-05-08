# LDA建模分析导入包
import time

import jieba.posseg as jp, re, jieba
from gensim import corpora, models
from gensim.models.coherencemodel import CoherenceModel  # 计算相似度
from threading import Thread
import pyLDAvis.gensim
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class ldamodel(QThread):
    sig_one_end = pyqtSignal(str)
    sig_img_end = pyqtSignal(list,list)
    sig_img2_end = pyqtSignal(list,list)
    sig_end = pyqtSignal()

    def __init__(self, filename=None):
        super(ldamodel, self).__init__()
        self.filename = filename

    def stopwords_fun(self, path):  # path为停用词文件
        stop = path  # 路径改为path
        file = open(stop, encoding='utf-8')
        stopwords = []  # 创建停用词列表
        for line in file.readlines():
            #     print(line)
            stopwords.append(line.strip())  # 去除收尾换行符读取停用词
        return stopwords

    def pretreatment(self, file):  # 数据处理
        txts = []
        with open(file, 'r', encoding='utf-8') as sf:  # 文件路径要改
            for i in sf.readlines():
                txts.append(i.strip())  # 去掉首位空格
        words = []
        for txt in txts:
            line = re.sub(r'[^\u4e00-\u9fa5]+', '', txt)  # 把非汉字的字符全部去掉
            words.append(line)
        jieba.add_word('剑神', 9, 'n')  # 添加词，不会被分，模型优化过程中可继续添加
        flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd')  # 词性
        # 分词
        train = []
        for word in words:
            txt = []
            for i in jp.cut(word):  # jp切词返回词性和词语
                if i.word not in self.stopwords and i.flag in flags and len(i.word) > 1:
                    txt.append(i.word)
            train.append(txt)
        return train  # 返回整理好的训练数据集

    def training_model(self, train, n):
        # 构建词典
        dictionary = corpora.Dictionary(train)
        # 基于词典，使【词】→【稀疏向量】，并将向量放入列表，形成【稀疏向量集】
        corpus = []
        for ii in train:
            corpus.append(dictionary.doc2bow(ii))
        lda = models.ldamodel.LdaModel(corpus=corpus, num_topics=n, id2word=dictionary, passes=20)  # 训练模型
        return lda, dictionary, corpus

    def run(self):
        self.stopwords = self.stopwords_fun('stopwords.txt')
        train = self.pretreatment(self.filename)
        self.sig_one_end.emit('文件读取成功,分词完成')
        # 下面的代码全部为选择最合适的主题数写的，所以要分段执行
        x_list = []  # 不同主题数的相困惑度
        y_list = []
        for i in range(1, 20):
            lda = self.training_model(train, i)
            x_list.append(i)
            y_list.append(lda[0].log_perplexity(lda[2]))
            self.sig_one_end.emit("主题个数为：%d" % i)

        # 困惑度是越低越好的当主题太多时，我们的模型已经过拟合了
        self.sig_img_end.emit(x_list,y_list)



        # 相似度越高，模型效果越好
        x_l = []  # 不同主题数的相似度
        y_l = []
        for e in range(1, 20):
            lda = self.training_model(train, i)  # n是ldamodel.py中做模型困惑度图中的最高转折点x值
            x_l.append(e)
            cv_tmp = CoherenceModel(model=lda[0], texts=train, dictionary=lda[1], coherence='c_v')
            y_l.append(cv_tmp.get_coherence())
        self.sig_img2_end.emit(x_l, y_l)

        # 可视化模型
        try:
            lda = self.training_model(train, 8)
            vis_data = pyLDAvis.gensim.prepare(topic_model=lda[0], corpus=lda[2], dictionary=lda[1])
            file_path = './{}.model'.format(lda[0])
            lda[0].save(file_path)  # 保存模型
            task = Thread(target=self.open_serving,args=(vis_data,))
            task.start()
            time.sleep(2)
            self.sig_one_end.emit('运行结束')
            self.sig_end.emit()
        except Exception as e:
            print(e)

    def open_serving(self,data):
        pyLDAvis.show(data, open_browser=False)