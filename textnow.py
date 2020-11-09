# coding: utf-8

from textnow_sms import Textnow

if __name__ == '__main__':
    usernames = []
    passwords = []
    passwdStr = ""
    sentNum = ""
    sentMsg = ""
    try:
        f = open("passwd.txt", "r")
        passwdStr = f.read()
        passwds = passwdStr.split('\n')
        for index in range(0, len(passwds)):
            passwdInfo = passwds[index].split(',')
            usernames.append(passwdInfo[0])
            passwords.append(passwdInfo[1])
    except:
        print(u"passwd.txt文件不存在")
        quit()

    print(u"共有 %s 个账号，即将开始保号处理" % len(usernames))

    try:
        f = open("conf.txt", "r")
        sentInfo = f.read()
        sentNum = sentInfo.split('\n')[0]
        sentMsg = sentInfo.split('\n')[1]
    except:
        print(u"conf.txt文件不存在")
        quit()

    for idx in range(0, len(usernames)):
        username = usernames[idx]
        password = passwords[idx]
        text = Textnow(username, password, sentNum, sentMsg)
        text.send_text()
        print("---第%s个账号处理完毕---" % (idx + 1))

    print("---Good Job! 所有账号处理完毕---")
