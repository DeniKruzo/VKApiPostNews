from tip import token, keyapi
from newsapi import NewsApiClient
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import requests


# Init!
# для N.A
newsapi = NewsApiClient(api_key=keyapi)
# Для вк
auth = vk_api.VkApi(token = token)
longpoll = VkLongPoll(auth)

def getPresiden():
    url = "https://newsapi.org/v2/everything?q=Путин&from=2022-02-26&to=2022-02-26&sortBy=popularity&apiKey="+keyapi
    news = requests.get(url).json()
    articles = news["articles"]

    my_articles = []
    my_news = " "

    for article in articles:
        my_articles.append(article["title"])

    for i in range(5):
        my_news = my_news + "*) " + my_articles[i] + "\n"

    return my_news

def getNews():
    url = "https://newsapi.org/v2/top-headlines?country=ru&apiKey="+keyapi
    news = requests.get(url).json()
    articles = news["articles"]

    my_articles = []
    my_news = " "

    for article in articles:
        my_articles.append(article["title"])

    for i in range(5):
        my_news = my_news + "*) " + my_articles[i] + "\n"

    return my_news



def write_mess (sender, message):
    auth.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        res_mess = event.text
        sender = event.user_id

        if res_mess == "новости" or res_mess == "Новости":
            write_mess(sender, getNews())
        elif res_mess == "путин" or res_mess == "Путин":
            write_mess(sender, getPresiden())
        else:
            write_mess(sender, "Я глупый!")



