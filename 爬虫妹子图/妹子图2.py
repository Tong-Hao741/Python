import requests
import re
url = 'https://www.vmgirls.com/9456.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
}

r = requests.request('GET',url,headers = headers)
json = re.compile('<img alt="可爱的你-唯美女生".*?data-src="(.*?)" data-nclazyload')
data = re.findall(json,r.text)

for i in range(len(data)):
    print("正在下载第{}张照片".format(i+1))
    with open(("妹子图片/") + "可爱清纯妹子图_" + str(i) + ".jpg",'wb') as f:
        url_2 = data[i]
        r_2 = requests.request('GET',url_2,headers = headers)

        f.write(r_2.content)
    print("下载完成")



