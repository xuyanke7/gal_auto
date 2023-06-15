import requests
import json
import logging
import os

sever = "on"
cookie = "koa:sess=eyJ1c2VySWQiOjIwNDczNywiX2V4cGlyZSI6MTcwNDA4NTY2NzQ2MSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=hTBINafo3XYOBQwp2TNfQ0OPd2A; _gid=GA1.2.169040157.1686730282; _gat_gtag_UA_104464600_2=1; _ga=GA1.1.1206574097.1678165680; _ga_CZFVKMNT9J=GS1.1.1686730281.3.1.1686730497.0.0.0"


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
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
        'token': 'glados.network'
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
            print(mess)
            logging.info(mess)
    else:
        # 
        logging.error("Cookie Expired")


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
