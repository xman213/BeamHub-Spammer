import requests, threading, user_agent, random, string, os

def clear():
   os.system('cls')

c = 0
class Generate:
 def online():
    global c
    while True:
            f = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=3))
            email = f'genlol{f}@zt.com'
            user = f'xmantohot{f}'
            password = 'lmafo'
            hed = {
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "en-US,en;q=0.9",
             "Cache-Control": "no-store",
             "Connection": "keep-alive",
             "Content-Length": "69",
             "Content-Type": "application/json; charset=UTF-8",
             "Referer": "https://service30.rumbletalk.net/!HxCxnc6/",
             "User-Agent": user_agent.generate_user_agent()
            }
            data = {"cmd":7,"data":{"username":f"{user}","password":f"{password}","type":2}}
            r = requests.post("https://service30.rumbletalk.net/!HxCxnc6/", headers=hed, json=data)
            if r.status_code == 200 or 201 or 203 or 204:
               c += 1
               print(f'Tech Beams Chat Onliner | Account Online!')
               open("accs.txt", "a").write(user+f':{password}\n')
               os.system(f'title tech beams chat onliner ^| accs: {c}')
            if r.status_code == 400 or 403 or 404:
               print(f'Tech Beams Chat | Account Not Online!')
               os.system(f'title tech beams chat onliner ^| accs: {c}')
 def create():
       global c 
       while True:
           f = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=3))
           email = f'techbeams_chat_gen{f}@zt.com'
           user = f'xmantohot{f}'
           password = 'lmao'
           hed = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-store",
            "Connection": "keep-alive",
            "Content-Length": "228",
            "Content-Type": "application/json; charset=UTF-8",
            "Referer": "https://service30.rumbletalk.net/!HxCxnc6/",
            "User-Agent": user_agent.generate_user_agent()
           }
           data = {"cmd":33,"data":{"firstName":"","lastName":"","username":f"{user}","email":f"{email}","password":f"{password}","image":"https://cdn.discordapp.com/attachments/1003789600893960282/1004112746725507122/zt_bitcoin.png","description":""}}
           r = requests.post("https://service30.rumbletalk.net/!HxCxnc6/", headers=hed, json=data)
           if 'cmd' in r.text:
               c += 1
               print(f'Tech Beams Chat | Account Made!')
               open("accs.txt", "a").write(user+f':{password}\n')
               os.system(f'title tech beams chat account gen ^| accs: {c}')
           if '' in r.text:
               print(f'Tech Beams Chat | Account Not Created!')
               os.system(f'title tech beams chat account gen ^| accs: {c}')
              


 def spam():
    global c
    while True:
            sookie = input('Sookie: ')
            f = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=3))
            hed = {
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "en-US,en;q=0.9",
             "Cache-Control": "no-store",
             "Connection": "keep-alive",
             "Content-Length": "31",
             "Content-Type": "application/json; charset=UTF-8",
             "Referer": "https://service30.rumbletalk.net/!HxCxnc6/",
             "Sookie": sookie ,
             "User-Agent": user_agent.generate_user_agent()
            }
            data = {"cmd":10,"data":{"text":f"ok{f}"}}
            r = requests.post("https://service30.rumbletalk.net/!HxCxnc6/", headers=hed, json=data)
            if 'pending' in r.text:
               c += 1
               print(f'Tech Beams Chat Spammer | Message Sent!')
               os.system(f'title tech beams chat spammer ^| messages: {c}')
            if '' in r.text:
               print(f'Tech Beams Chat Spammer | Message Not Sent!')
               os.system(f'title tech beams chat spammer ^| messages: {c}')




import pystyle
from pystyle import *
os.system('title BeamHub spammer. Made by xman and zt')

menu = """
▄▄▄▄   ▓█████ ▄▄▄       ███▄ ▄███▓ ██░ ██  █    ██  ▄▄▄▄        ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█████▄ ▓█   ▀▒████▄    ▓██▒▀█▀ ██▒▓██░ ██▒ ██  ▓██▒▓█████▄    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██▒ ▄██▒███  ▒██  ▀█▄  ▓██    ▓██░▒██▀▀██░▓██  ▒██░▒██▒ ▄██   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒██░█▀  ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ ░▓█ ░██ ▓▓█  ░██░▒██░█▀       ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
░▓█  ▀█▓░▒████▒▓█   ▓██▒▒██▒   ░██▒░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░▒▓███▀▒░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
▒░▒   ░  ░ ░  ░ ▒   ▒▒ ░░  ░      ░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
░    ░    ░    ░   ▒   ░      ░    ░  ░░ ░ ░░░ ░ ░  ░    ░    ░  ░  ░  ░░         ░   ▒   ░      ░   
░         ░  ░     ░  ░       ░    ░  ░  ░   ░      ░               ░                 ░  ░       ░   
            ░                                                   ░                                           
                                                                     ╔══════════════════════════════╗
                                                                     ║ Made with <3 by the LEAD team║
                                                                     ║ discord.gg/lead              ║
                                                                     ╚══════════════════════════════╝
[1] Account Creator And Viewer botter  [2] Spammer (Very Buggy) [3] Account Onliner
"""
threads = input(Colorate.Horizontal(Colors.blue_to_cyan,'Threads: '))
clear()
print(Colorate.Horizontal(Colors.blue_to_cyan, menu))
print(' ')
print(' ')

choice = int(input(Colorate.Horizontal(Colors.blue_to_cyan, 'Enter Choice: ')))

if choice == 1:

 if threading.active_count() < int(threads):
         threading.Thread(target=Generate.create).start() 
elif choice == 2:
 if threading.active_count() < int(threads):
        threading.Thread(target=Generate.spam).start() 
elif choice == 3:
   if threading.active_count() < int(threads):
        threading.Thread(target=Generate.online).start() 
else:
    print(Colorate.Horizontal(Colors.blue_to_cyan, 'Please pick a number 1-3'))
    import time
    time.sleep(40)




