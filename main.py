from bs4 import BeautifulSoup
import urllib2
from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram.ext import Updater
import os
import sys
from GameItem import GameItem
from util import getDate, getUserData
from telegram_cmd import add_user, latest_game, list_users, remove_user, start
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
userlist = getUserData()

def getCurrentGameStats(username):
    response = urllib2.urlopen('https://euw.op.gg/summoner/userName=' + username)
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    tmp = soup.findAll('div', {"class": "GameItemWrap"})

    gameStats = []
    for item in tmp:
        currentStats = item.find('div', {'class': 'GameStats'})
        gameType = ' '.join(currentStats.find('div', {'class': 'GameType'}).getText().split())
        timeStamp = getDate(item.find("div", {"class": "TimeStamp"}).find("span")['data-datetime'])
        gameStats.append(GameItem(gameType, timeStamp))

    return gameStats

if len(userlist) != 0:
    data = getCurrentGameStats(userlist[0].split('\t')[0])
    data.sort()
    if len(data) != 0:
        print data[0].printFormatedDate()


def sayhi(bot, job):
    job.context.message.reply_text("hi")

def time(bot, update,job_queue):
    job = job_queue.run_repeating(sayhi, 30, context=update)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        logging.critical('No token found.')
        sys.exit()
    
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text , time,pass_job_queue=True))

    dispatcher.add_handler(CommandHandler('add', add_user, pass_args=True))
    dispatcher.add_handler(CommandHandler('remove', remove_user, pass_args=True))
    dispatcher.add_handler(CommandHandler('list', list_users))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('latest', latest_game, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()