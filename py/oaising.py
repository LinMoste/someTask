# const $ = new Env('OAI签到')
import requests
import os


url = "https://oai.itsfurry.com/api/user/signing"
EnableNotify = False
try:
    from notify import send
    EnableNotify = True
    print("当前脚本在青龙面板中运行")
except ImportError:
    print("当前脚本不在青龙面板中运行")


def reqSign():
    cookie = os.environ.get('ITS_COOKIE')
    if cookie is None:
        print("Cookie not set  use getenv method")
        cookie = os.getenv('ITS_COOKIE')

    if cookie is None:
        print("cookie not set ")
        return

    headers = {
        "authority": "oai.itsfurry.com",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "cookie": cookie,
        "new-api-user": "1308",
        "origin": "https://oai.itsfurry.com",
        "referer": "https://oai.itsfurry.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    data = {
        "id": 1308
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        print("状态码:", response.status_code)
        if EnableNotify:
            if response.status_code == 200 :
                send("签到成功","")
            else:
                send("签到失败",response.text)
        print("响应内容:", response.text)

    except requests.exceptions.RequestException as e:
        print("请求失败:", e)
        if EnableNotify:
            send("鸿星尔克签到失败",str(e))

if __name__ == '__main__':
    reqSign()
else:
    print("模块注入。")
