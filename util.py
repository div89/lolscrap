from datetime import datetime
import pytz
import os

users_filename = os.getenv('USER_FILE')
#  'users.txt'

def getDate(dateAsString):
    utc_date = datetime.utcfromtimestamp(int(dateAsString))
    old_timezone = pytz.timezone("UTC")
    new_timezone = pytz.timezone("Europe/Berlin")   
    tz_date = old_timezone.localize(utc_date).astimezone(new_timezone)
    return tz_date


def getUserData():
    userlist = []
    with open(users_filename) as f:
        users = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    for user in users:
        userlist.append(user.split('\t')[0].rstrip())
    return userlist

def getLatestGame(username):
    users = getUserData()


def appendToUserList(username):
    with open(users_filename, 'a') as userfile:
        userfile.write(username)
        userfile.write('\t')
        userfile.write(unicode(datetime.now()))
        userfile.write('\n')

def removeUserFromList(username):
    lines = []
    count = 0
    with open(users_filename, 'r') as userfile:
        lines = userfile.readlines()

    with open(users_filename, 'w') as userfile:
        for line in lines:
            data = line.split('\t')
            if data[0]!=username:
                userfile.write(line)
            else:
                count+=1
    return count

def updateUserList(username, new_date):
    lines = []
    count = 0

    with open(users_filename, 'r') as userfile:
        lines = userfile.readlines()

    with open(users_filename, 'w') as userfile:
        for line in lines:
            data = line.split('\t')
            if data[0]!=username:
                userfile.write(line)
            else:
                userfile.write(data[0] + '\t' + new_date + '\n')
                count+=1
    return count