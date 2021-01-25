import requests
from bs4 import BeautifulSoup
import pandas
from lxml import etree


def spider():
    topics = []

    for i in range(1, 307, 1):
        a = str(i)
        url = f'https://www.bilibili.com/video/BV1y7411y7am?p=23'

        request = requests.get(url)


        html = request.content.decode('utf-8')
        dom = BeautifulSoup(html,'lxml')

        topics = topics + [i.getText() for i in dom.select(' li:nth-child('+a+') .part')]
        print(dom.select(' li:nth-child('+a+') .part'))

    short = pandas.DataFrame({ '主题': topics})

    short.to_excel('./播放列表.xlsx')



if __name__ == '__main__':
    spider()


