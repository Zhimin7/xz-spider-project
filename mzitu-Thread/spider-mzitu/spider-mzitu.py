import requests
from lxml import etree
import threading


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
name = 0    # 图片名


def request_data(url):
    response = requests.get(url, headers=headers)
    return response


def save_data(result, path):
    f = open(path, 'wb')
    f.write(result)


def get_data(url):
    global name
    img_lists = []  # 存储图片链接
    response = request_data(url)
    html_data = etree.HTML(response.content.decode('utf-8'))
    li_lists = html_data.xpath('//div[@id="comments"]/ul/li')
    for li_list in li_lists:
        img_list = li_list.xpath('.//p/img/@data-original')[0]
        img_lists.append(img_list)
    for img in img_lists:
        result = request_data(img).content
        save_data(result, f'./image/{name}.jpg')
        print(f'正在下载{img}')
        name += 1


if __name__ == '__main__':
    for i in range(1, 3):
        url = f'https://www.mzitu.com/jiepai/comment-page-{i}/'
        t1 = threading.Thread(target=get_data, args=(url, ))
        t1.start()