from util import appendToUserList, getLatestGame, getUserData, removeUserFromList

users = []


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Started bot. Add new users!")


def add_user(bot, update, args):
    if len(args) == 0:
        return
    new_user = args[0]
    users = getUserData()

    usernames = [user.split("\t")[0] for user in users]
    if new_user not in usernames:
        appendToUserList(new_user)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=f"added user {new_user} to user list!",
        )


def list_users(bot, update):
    users = getUserData()
    if len(users) == 0:
        bot.send_message(
            chat_id=update.message.chat_id, text="currently no users in list."
        )
    else:
        bot.send_message(chat_id=update.message.chat_id, text=", ".join(users))


def latest_game(bot, update, args):
    if len(args) == 0:
        return
    return getLatestGame()


def remove_user(bot, update, args):
    if len(args) == 0:
        return
    res = removeUserFromList(args[0])
    if res != 0:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=f"removed user {args[0]} from user list!",
        )
