import time
#import eventlet
import requests
import logging
import telebot
from time import sleep
from bs4 import BeautifulSoup

URL_SPY = 'http://quote-spy.com/'
FILENAME_VK = 'last_known_id.txt'
#BASE_POST_URL = 'https://vk.com/wall-39270586_'

BOT_TOKEN = '549277681:AAGz364DCYncVsIPKIjW0_jG8qpElQK9Rp8'
CHANNEL_NAME = '@f_news_c'

bot = telebot.TeleBot(BOT_TOKEN)

def get_data():
    response = requests.get(URL_SPY)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find(id="NewsPanel1").find_all("tr")
    L_MES = content_div[0]#[len(content_div) - 1]
    return L_MES


def send_new_posts(item):
    news = item.find_all("td")[1].find("a")
    #bot.send_message(CHANNEL_NAME, "[" + news.text + "](" + news.get("href") + ")" )
    bot.send_message(CHANNEL_NAME, news.get("href"))
    return


if __name__ == '__main__':
    LAST_M = get_data()
    LAST_MES = LAST_M.find_all("td")[1].find("a")
    send_new_posts(LAST_M)
    while True:
        mes = get_data()
        news = mes.find_all("td")[1].find("a")
        if news.text != LAST_MES.text:
            send_new_posts(mes)
            LAST_M = mes
            LAST_MES = LAST_M.find_all("td")[1].find("a")
        #time.sleep(2)




