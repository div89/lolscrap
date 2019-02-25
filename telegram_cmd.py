from util import appendToUserList, getLatestGame, getUserData, removeUserFromList

users = []
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Started bot. Add new users!")


def add_user(bot, update, args):
    if len(args) == 0:
        return

    users = getUserData()
    
    usernames = [user.split('\t')[0] for user in users]
    if args[0] not in usernames:
        appendToUserList(args[0])
        bot.send_message(chat_id=update.message.chat_id, text='added user ' + args[0] + ' to user list!')

def list_users(bot, update):
    users = getUserData()
    if not len(users) == 0:
        bot.send_message(chat_id=update.message.chat_id, text=', '.join(users))
    else:
        bot.send_message(chat_id=update.message.chat_id, text='currently no users in list.')

def latest_game(bot, update, args):
    if len(args) == 0:
        return
    return getLatestGame(args[0])

def remove_user(bot, update, args):
    if len(args) == 0:
        return
    res = removeUserFromList(args[0])
    if res != 0:
        bot.send_message(chat_id=update.message.chat_id, text='removed user ' + args[0] + ' from user list!')