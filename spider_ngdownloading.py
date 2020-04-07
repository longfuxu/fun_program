import requests
from bs4 import BeautifulSoup

#找到正确且准确的母网页
url_parent = 'http://www.ngchina.com.cn/travel/photo_galleries/4802.html'

#获取网页的html文件，并且解析达到soup对象
html = requests.get(url_parent).text
soup = BeautifulSoup(html, 'lxml')
#找准正确的tag标签
ul = soup.find_all('ul', attrs={'class': 'cf'})

#标签内部进一步寻找最贴近的子标签
for i in ul:
    ul_img = i.find_all('img')
#子标签内部找到src网址
    for img in ul_img:
        url = img['src']
        r = requests.get(url, stream=True)
#写入名字，名字是url.split方法解析出来
        img_name = url.split('/')[-1]
        with open(r'C:\Users\86183\Desktop\img_2\ %s' % img_name, 'wb')as f:
            for chunk in r.iter_content(chunk_size=128)
            f.write(chunk)
        print('saved %s' % img_name)



