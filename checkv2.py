import requests
import re
import time
import os

your_name = os.environ["YOUR_NAME"]
your_pwd = os.environ["YOUR_PWD"]
wechat_key = os.environ["WECHAT_KEY"]
token = os.environ["TOKEN"]
chat_id = os.environ["CHAT_ID"]
bark_url = os.environ["BARK"]
form_data = os.environ["FORM"]

def bot_post(text):
    if wechat_key != "":
        url1 = 'https://sctapi.ftqq.com/' + wechat_key + '.send?title=check_ok' + '&desp='+text+time.strftime("%m-%d", time.localtime())
        re_result = requests.get(url1)
        print(re_result.text)
    if token != "":
        url2 = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+text+time.strftime("%m-%d", time.localtime())
        re_result = requests.get(url2)
        print(re_result.text)
    if bark_url != "":
        url3 = bark_url + text + '?icon=https://imgapp.buaa.edu.cn/image/25/c2adaf73e7b4ea6058125d26d2392e21.jpg'
        re_result = requests.get(url3)
        print(re_result.text)
        

def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    print(responseRes.text)
    return responseRes


def fillForm(res):
    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/ncov/wap/default/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': res.headers['set-cookie']
    }
    r = s.post('https://app.buaa.edu.cn/ncov/wap/default/save', data=form_data, headers=headers)
    return r


def main():
    result = fillForm(buaaLogin(your_name, your_pwd))
    print(result.text)
    bot_post(result.json()["m"])
    return("DONE")
main()
