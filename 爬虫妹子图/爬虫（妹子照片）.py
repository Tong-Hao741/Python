import requests
import re

url = "http://www.mzitu.com"
user = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Referer":"https://www.mzitu.com/"

}
#获取网站源代码，并修改user-agent，通过第一层反爬
r = requests.request('GET',url,headers = user)
#运用正则表达式筛选数据,image_url获取后是列表类型
print(r.text)
image_url = re.findall("data-original='(.*)' "
                       "alt='(.*?)'",r.text)
print(image_url)
for image_orgin_url,image_name in image_url:
    #  wb 是二进制写入，例如图片在源地址中也是二进制存储
    with open("妹子图片/" + image_name + ".jpg",'wb') as f:
        image_content = requests.get(image_orgin_url,headers = user)
        f.write(image_content.content)



