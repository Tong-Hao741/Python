import requests
from tkinter import *
import execjs
import json
# ====================================代码部分
class BaiDuTranslateWeb:

    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
        self.headers = {
            'authority': 'fanyi.baidu.com',
            'accept': '*/*',
            'sec-fetch-dest': 'empty',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://fanyi.baidu.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'BIDUPSID=6FB7680FDD580FF316328871A77AC0D1; PSTM=1571148042; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __cfduid=df6fc24d3e7818b34540d0e594efa7cc51574232064; BDUSS=W1QYkkybTJYOGczTnJKN0wyWGdzQkM3UUh1cjBnZmhMZTFUazRaN2JaalZUd0JlRVFBQUFBJCQAAAAAAAAAAAEAAADASd6E3O3d78jVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANXC2F3VwthdR; APPGUIDE_8_2_2=1; BAIDUID=4956C2E7B5CE1CADF0BB5A0C2C8E040F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; PSINO=2; ZD_ENTRY=baidu; yjs_js_security_passport=8733190434e63c9d2e60fab95381ebf84bc59568_1582200098_js; BDRCVFR[5IRyTarJWqT]=mbxnW11j9Dfmh7GuZR8mvqV; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1581647013,1582191586,1582200093,1582201256; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1582201344; __yjsv5_shitong=1.0_7_c36af1b2f3e92b3e2f61972222fce2952ff9_300_1582201344284_42.235.130.154_4d1a9929',
        }
        self.params = (
            ('from', 'en'),
            ('to', 'zh'),
        )
        #query和sign是固定的，错一不可
        self.data = {
            'from': 'en',
            'to': 'zh',
            'query': None,
            'simple_means_flag': '3',
            'sign': None,
            'token': '6e09565a1e83dcadfb491ba8ee46e0c2',
            'domain': 'common'
        }

    def get_sign(self):
         input = entery.get()
         with open("baidu.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", input)

            return sign

    def print_rsult(self):
        text.delete('1.0', END)
        word = entery.get()
        self.data["query"] = str(word)
        self.data["sign"] = self.get_sign()

        response = requests.post(self.url, headers=self.headers, params=self.params,
                                 data=self.data)
        data = response.text
        json_data = json.loads(data)
        result = json_data['trans_result']["data"][0]["dst"]
        #显示在窗口上
        text.insert(END, result + "\n")
        text.see(END)
        text.update()





# =====================================界面部分
root = Tk()
# 标题
root.title("网易云音乐爬取器")
# 设置窗口大小和位置
root.geometry('350x220+550+250')
# 设置标签
label = Label(root, text='在线翻译：', font=('【嵐】芊柔体', 18))
label.grid(row=0, column=0)
# 设置输入框
entery = Entry(root, font=('微软雅黑', 10), width=25)
entery.grid(row=0, column=1)
# 设置列表框
text = Text(root, width=28, font=('微软雅黑', 14), height=5)
text.grid(row=1, column=0, columnspan=2, pady=10, padx=15)
# 设置两个按钮
button_1 = Button(root, text='翻译',command = BaiDuTranslateWeb().print_rsult)
button_1.grid(row=2, column=0, sticky=W)
button_2 = Button(root, text='退出', command=root.quit)
button_2.grid(row=2, column=1, sticky=E)
# 显示窗口
root.mainloop()


