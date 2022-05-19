import requests

def getLink(mail, link):
    f = open(r"C:\Users\minh303\Documents\School Folder\Python\api\Chegg-Discord-BOT-main\Chegg-Discord-BOT-INIT-2\lib\bot\key.0", "r")
    secretkey = f.readline()
    f.close()

    a = requests.post("https://cheggbot.woosal.com", data={"mail":"{0}".format(mail),"soru":"{0}".format(link),"key":f"{secretkey}"})
    return a.text
