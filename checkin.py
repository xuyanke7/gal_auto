import requests
import json
import logging
import os

sever = "on"
cookie = os.getenv("COOKIE")
sckey = os.getenv("SCKEY")
sckey = "SCT213504TB5Ot5vjoVcHIJEIA5MlZqWwl"
cookie = "_gid=GA1.2.1391917914.1710593251; koa:sess=eyJ1c2VySWQiOjIwNDczNywiX2V4cGlyZSI6MTczNjUxMzI3MDQ3OSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=vg5xQYTjAKtw9AUCGTGjampNMeg; _gat_gtag_UA_104464600_2=1; _ga_CZFVKMNT9J=GS1.1.1710593250.1.1.1710593317.0.0.0; _ga=GA1.1.1210027151.1710593251"

logging.basicConfig(
    level=logging.INFO,
    filename="logging.log",
    filemode="a",
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def start():

    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.one'
    }
    checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                            'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(url2, headers={
                         'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        if sever == 'on':
            print(mess + ', you have '+time+' days left')
            logging.info(mess)
            requests.get('https://sc.ftqq.com/' + sckey +
                         '.send?text=' + mess + ','+time+'days left')
    else:
        #
        requests.post('https://sc.ftqq.com/' + sckey +
                     '.send?text=Cookie Expired')
        logging.error("Cookie Expired")


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
