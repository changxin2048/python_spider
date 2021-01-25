import requests
from bs4 import BeautifulSoup
import pandas as pd

def spider():
    url1 = "https://movie.douban.com/subject/33420285/comments?status=P"

    headers = {
        'Referer': 'https://movie.douban.com/subject/33420285/comments?status=P',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    reviewers = []
    dates = []
    shot_comments = []
    votes = []

    for i in range(0, 100, 20):
        url = f'https://movie.douban.com/subject/33420285/comments?start={i}&limit=20&sort=new_score&status=P'
        request = requests.get(url, headers=headers)
        html = request.content.decode('utf-8')
        dom = BeautifulSoup(html, 'lxml')
        reviewers = reviewers + [i.getText() for i in
                                 dom.select('#comments > div > div.comment > h3 > span.comment-info > a')]
        dates = dates + [i.getText() for i in
                         dom.select('#comments > div > div.comment > h3 > span.comment-info > span.comment-time')]
        shot_comments = shot_comments + [i.getText() for i in dom.select('#comments > div > div.comment > p > span')]
        votes = votes + [i.getText() for i in
                         dom.select('#comments > div > div.comment > h3 > span.comment-vote > span')]

    short = pd.DataFrame({
        '时间': dates, '评论者': reviewers, '留言': shot_comments, '票数': votes
    })

    short.to_excel('./short.xlsx')


if __name__ == '__main__':
    spider()
