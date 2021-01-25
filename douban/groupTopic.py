import requests
from bs4 import BeautifulSoup
import pandas as pd

def spider():
    url1 = "https://www.douban.com/group/205468/discussion?start=0"

    headers = {
        'Referer': 'https://www.douban.com/group/205468/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    topics = []
    dates = []
    authers = []
    pictures = []

    for i in range(0, 300, 30):
        url = f'https://www.douban.com/group/205468/discussion?start={i}'

        request = requests.get(url, headers=headers)
        print(request.status_code)
        html = request.content.decode('utf-8')
        dom = BeautifulSoup(html, 'lxml')
       
        topics = topics + [i.get('href') for i in dom.select('td.title > a:link')]
        dates = dates + [i.getText() for i in dom.select('td.time')]
        authers = authers + [i.getText() for i in dom.select(' td:nth-child(2) > a')]

        print(authers)
        # print(dates)
    
    # for i in topics:
    #     request = requests.get(i,headers=headers)
    #     html = request.content.decode('utf-8')
    #     dom = BeautifulSoup(html, 'lxml')
    #     pictures = pictures + [i.get('src') for i in dom.select('#link-report > div > div > div > div > img')]
    #
    #     print(pictures)



    short = pd.DataFrame({
        '时间': dates, '作者':authers,'主题': topics})

    short.to_excel('./主题205468.xlsx')

def abc():
    print(123)
if __name__ == '__main__':
    spider()
    # abc()
