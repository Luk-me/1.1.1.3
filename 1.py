import requests
import time
import rc4

def con():
    try:
        url="https://www.baidu.com"
        r=requests.get(url)
        time.sleep(10)
    except:
        login()

def login():
    user="91079"
    pswd="Az123456!"
    url = "http://1.1.1.3/ac_portal/login.php"
    data={
    "opr": "pwdLogin",
    "userName": "",
    "pwd": "",
    "auth_tag": "",
    "rememberPwd": "1"
    }
    now_date = str(int(round(time.time()*1000)))
    password=rc4.encrypt(now_date,pswd)
    data['userName']=user
    data['pwd']=password
    data['auth_tag']=now_date
    requests.post(url, data)

if __name__ == '__main__':
    while 1:
        try:
            con()
        except:
            print("登陆失败")
