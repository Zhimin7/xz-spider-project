import requests
from bs4 import BeautifulSoup


zero = ''.encode('utf-8')
print(type(zero))
one = ''.encode('utf-8')
two = ''.encode('utf-8')
three = ''.encode('utf-8')
eight = ''.encode('utf-8')
five = ''.encode('utf-8')
# two_handred = ''.encode('utf-8')
# three_handred = ''.encode('utf-8')
# fifty = ''.encode('utf-8')

'''

zero = ''.encode('utf-8')
one = ''.encode('utf-8')
two = ''.encode('utf-8')
three = ''.encode('utf-8')
eight = ''.encode('utf-8')
five = ''.encode('utf-8')
'''
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
response = requests.get('https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
salary = soup.select('span.day.font')
for s in salary:
    number = s.text.encode('utf-8').replace(zero, b'0').\
        replace(one, b'1').replace(two, b'2').\
        replace(eight, b'8').replace(three, b'3').replace(five, b'5')
    print(number.decode('utf-8'))