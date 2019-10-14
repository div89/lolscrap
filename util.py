from datetime import datetime
import pytz
import os

users_filename = os.getenv("USER_FILE")

UTZ_TZ = pytz.timezone("UTC")
GMT2_TZ = pytz.timezone("Europe/Berlin")

def getDate(dateAsString):
    utc_date = datetime.utcfromtimestamp(int(dateAsString))
    tz_date = UTZ_TZ.localize(utc_date).astimezone(GMT2_TZ)
    return tz_date


def getUserData():
    userlist = []
    with open(users_filename) as f:
        users = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    for user in users:
        userlist.append(user.split("\t")[0].rstrip())
    return userlist


def getLatestGame():
    users = getUserData()

def appendToUserList(username):
    with open(users_filename, "a") as userfile:
        userfile.write(f"{username}\t{str(datetime.now())}\n")

def removeUserFromList(username):
    lines = []
    count = 0
    with open(users_filename, "r") as userfile:
        lines = userfile.readlines()

    with open(users_filename, "w") as userfile:
        for line in lines:
            name, _ = line.split("\t")
            if name != username:
                userfile.write(line)
            else:
                count += 1
    return count


def updateUserList(username, new_date):
    lines = []
    count = 0

    with open(users_filename, "r") as userfile:
        lines = userfile.readlines()

    with open(users_filename, "w") as userfile:
        for line in lines:
            name, _ = line.split("\t")
            if name != username:
                userfile.write(line)
            else:
                userfile.write(f"{name}\t{new_date}\n")
                count += 1
    return count
