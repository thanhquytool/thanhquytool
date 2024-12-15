import json
import requests,os,time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys
banner = f"""
\033[1;32m████████╗ ██████╚╗         ████████╗ █████╗  █████╗ ██╗
\033[1;36m╚══██╔══╝██║   ██║         ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;32m   ██║   ██║   ██║   █████╗   ██║   ██║  ██║██║  ██║██║
\033[1;36m   ██║   ██║ ████╚╗  ╚════╝   ██║   ██║  ██║██║  ██║██║
\033[1;36m   ██║   ╚████████║           ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m   ╚═╝    ╚════╗\033[1;36m██\033[1;31m║           ╚═╝    ╚════╝  ╚════╝ ╚═════╝
\033[1;31m               ╚══╝
\033[1;37mTool By: \033[1;32mThành Quý Tool
\033[1;37m══════════════════════════════════════════════════════════════
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;31m☞ Golike TikTok🧸 ☜
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;36mhttps://www.youtube.com/@thanhquytool
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;32m0355879036
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;33mhttps://t.me/quyleotop
\033[1;37m══════════════════════════════════════════════════════════════
"""
os.system('cls' if os.name== 'nt' else 'clear')
for x in banner:
  print(x,end = "")
  sleep(0.001)


    # Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;32m>\033[1;33m>\033[1;31m> \033[1;36mAuthorization Golike: \033[1;31m")
  token = input("\033[1;32mLưu Ý: T Nằm Dưới Authorization\n\033[1;32m>\033[1;33m>\033[1;31m> \033[1;36mNhập T: \033[1;31m")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;32mNhập \033[1;37m[\033[1;33m1\033[1;37m] \033[1;32mĐể Vào Tool Golike TikTok\n\033[1;36mNhập Authorization Acc Golike Khác Tại Đây Để Đổi Acc Golike\n\033[1;37m══════════════════════════════════════════════════════════════\n\033[1;36m┌─\033[1;37m[\033[1;32mTool By Thành Quý Tool\033[1;37m]\n\033[1;36m└──╼➤: \033[1;31m")

  if select != "1":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}
os.system("cls" if os.name == "nt" else "clear")
for x in banner:
  print(x,end = "")
  sleep(0.001)

def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;31mAuthorization Hoặc T Sai Hãy Nhập Lại!")
    quit()

  for i in range(len(chontktiktok["data"])):
    # print(f'\033[1;97m•[✩]➭\033[1;36m [{i+1}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m㊪ :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
    print(f'\033[1;36m[{i+1}] \033[1;97mTài Khoản :\033[1;93m {chontktiktok["data"][i]["nickname"]} :\033[1;32m Đang Hoạt Động')
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mNhập Số Thứ Tự Acc: \033[1;31m"))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mAcc Này Không Có Trong Danh Sách - Vui Lòng Nhập Lại: \033[1;31m"))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;31mVui Lòng Nhập Số Thứ Tự Acc Hoặc Nhập ( CTRL z ) Để Dừng Tool") 
while True:
  try:
    delay = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mNhập Delay: \033[1;31m"))
    break
  except:
    print("\033[1;31mVui Lòng Nhập Số Bất Kì Hoặc Nhập ( CTRL z ) Để Dừng Tool")
while True:
  try: 
    doiacc = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mNhận Tiền Lỗi Bao Nhiu Lần Thì Đổi Acc: \033[1;31m"))
    break
  except:
    print("\033[1;31mVui Lòng Nhập Số Bất Kì Hoặc Nhập ( CTRL z ) Để Dừng Tool")    
os.system('cls' if os.name== 'nt' else 'clear')    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

for x in banner:
  print(x,end = "")
  sleep(0.001)
  

while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[31mThông Báo! Acc Tiktok {dsaccloi} Đang Bị Nhả Follow Vui Lòng Đổi Acc Khác")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mNhập Số Thứ Tự Acc: \033[1;31m"))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;31;40m[\033[1;33;40m«\033[1;37;40m/\033[1;33;40m»\033[1;31;40m] \033[1;37;40m> \033[1;36mAcc Này Không Có Trong Danh Sách - Vui Lòng Nhập Lại: \033[1;31m"))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;31mVui Lòng Nhập Số Thứ Tự Acc Hoặc Nhập ( CTRL z ) Để Dừng Tool") 

     
  print(f'\033[1;97mĐang \033[1;96mLấy \033[1;95mNhiệm \033[1;91mVụ\033[1;93m Follow',end="\r")    
  # while True:
  #     try:  
  #         nhanjob = nhannv(account_id)
  #         break
  #     except:
  #         time.sleep(1)  # Thêm thời gian chờ 1 giây trước khi thử lại
  #         pass
  while True:
    try:
        nhanjob = nhannv(account_id)
        if nhanjob:  # Kiểm tra nếu nhanjob tồn tại và không rỗng
            break  # Thoát khỏi vòng lặp nếu nhận được nhiệm vụ thành công
        else:
            print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
    except:
        print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
        pass
    time.sleep(1)
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mT\033[1;36mh\033[1;35mà\033[1;32mn\033[1;31mh \033[1;34mQ\033[1;33mu\033[1;36mý\033[1;36m🧸 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;34mT\033[1;31mh\033[1;37mà\033[1;36mn\033[1;32mh \033[1;35mQ\033[1;37mu\033[1;33mý\033[1;32m🧸 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
                "\033[1;31mT\033[1;37mh\033[1;36mà\033[1;33mn\033[1;35mh \033[1;32mQ\033[1;34mu\033[1;35mý\033[1;37m🧸 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
                "\033[1;32mT\033[1;33mh\033[1;34mà\033[1;35mn\033[1;36mh \033[1;37mQ\033[1;36mu\033[1;31mý\033[1;34m🧸 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
                "\033[1;37mT\033[1;34mh\033[1;35mà\033[1;36mn\033[1;32mh \033[1;33mQ\033[1;31mu\033[1;37mý\033[1;34m🧸 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
                "\033[1;34mT\033[1;33mh\033[1;37mà\033[1;35mn\033[1;31mh \033[1;36mQ\033[1;36mu\033[1;32mý\033[1;37m🧸 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;36mT\033[1;35mh\033[1;31mà\033[1;34mn\033[1;37mh \033[1;35mQ\033[1;32mu\033[1;36mý\033[1;33m🧸 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;32mĐang Nhận Tiền         ",end = "\r")
# Vòng lặp cố gắng nhận tiền với tối đa 2 lần thử
    max_attempts = 2
    attempts = 0
    nhantien = None

    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:  # Nhận tiền thành công
                break
        except:
            pass  # Bỏ qua ngoại lệ và thử lại nếu có

        attempts += 1  # Tăng số lần thử

    # Kiểm tra kết quả của việc nhận tiền
    if nhantien and nhantien["status"] == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)

        chuoi = (f"\033[1;36m{dem}\033[1;31m\033[1;97m ● "
                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m ● "
                f"\033[1;32msuccess\033[1;31m\033[1;97m ● "
                f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m ●"
                f"\033[1;32m Ẩn ID\033[1;97m ●\033[1;97m \033[1;32m+{tien} \033[1;97m● "
                f"\033[1;33m{tong} VNĐ")

        print("                                                    ", end="\r")
        print(chuoi)
        checkdoiacc = 0
    else:
        # Nếu cả 2 lần thử đều thất bại, bỏ qua nhiệm vụ
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print("                                              ", end="\r")
                print("\033[1;31mBỏ Qua Nhiệm Vụ! ", end="\r")
                sleep(1)
                checkdoiacc += 1
                break
            except:
                qua = 0
                pass

