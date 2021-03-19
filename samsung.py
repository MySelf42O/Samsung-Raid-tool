import requests, os, colorama, random, json
from os import system
from random import randint
from colorama import Fore, Style
from time import sleep
import threading
colorama.init()


#dont skid this shit

system("title " + "Samsung Raid By FGLX.sql#9999")
system('mode con: cols=85 lines=20')


def logo():
    msg = Fore.BLUE+"""
  _________                                            __________        .__    .___
 /   _____/____    _____   ________ __  ____    ____   \______   \_____  |__| __| _/
 \_____  \\__  \  /     \ /  ___/  |   \/    \  / ___\   |       _/\__  \ |  |/ __ | 
 /        \/ __ \|  Y Y  \\___ \|  |   /   |  \/ /_/  >  |    |   \ / __ \|  / /_/ | 
/_______  (____  /__|_|  /____  >____/|___|  /\___  /   |____|_  /(____  /__\____ | 
        \/     \/      \/     \/           \//_____/           \/      \/        \/
        """
    print(msg)


def logomenu():
    msg = Fore.BLUE+"""
  _________                                            __________        .__    .___
 /   _____/____    _____   ________ __  ____    ____   \______   \_____  |__| __| _/
 \_____  \\__  \  /     \ /  ___/  |   \/    \  / ___\   |       _/\__  \ |  |/ __ | 
 /        \/ __ \|  Y Y  \\___ \|  |   /   |  \/ /_/  >  |    |   \ / __ \|  / /_/ | 
/_______  (____  /__|_|  /____  >____/|___|  /\___  /   |____|_  /(____  /__\____ | 
        \/     \/      \/     \/           \//_____/           \/      \/        \/
        """
    print(msg)
    print(Fore.LIGHTMAGENTA_EX+"═════════════════════════════════════════════════════════════════════════════════════")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"1"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Join Server")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"2"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Leave Server")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"3"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Send Messages")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"4"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Recation Bypass")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"5"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Token Checker")
    print(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"6"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+" Change BIO")
    print(Fore.LIGHTMAGENTA_EX+"═════════════════════════════════════════════════════════════════════════════════════")


joined = 0
faild = 0

def join():
    global joined
    global  faild
    os.system("cls")
    logo()
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    ID=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Invite ID ")
    with open(txt) as f:
        for line in f:
            token = line.strip("\n")
            res = requests.post(f"https://discordapp.com/api/v6/invites/{ID}",headers={'authorization':f'{token}'})
            if res.status_code == 200:
                joined += 1
                os.system("cls")
                logo()
                print(Fore.LIGHTGREEN_EX+f"Joined:{joined}")
                print(Fore.RED+f"Faild:{faild}")
                with open("Joined.txt", "a+") as (k):
                    k.writelines(f"{token}\n")
            else:
                faild += 1
                os.system("cls")
                logo()
                print(Fore.LIGHTGREEN_EX+f"Joined:{joined}")
                print(Fore.RED+f"Faild:{faild}")
    menu()
            

text = ""
ID = ""
txt = ""



def message():
    os.system("cls")
    logo()
    global text
    global ID
    global txt
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    text=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Message ")
    ID=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Channel ID ")
    for x in range(2):
        x = threading.Thread(target=send)
        x.start()
    menu()

def bypass():
    os.system("cls")
    logo()
    global txt
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    channel=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Channel ID ")
    message=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Message ID ")
    with open(txt) as f:
        for line in f:
            token = line.strip("\n")
            r = requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{message}/reactions/%E2%9C%85/%40me", headers={'authorization':f'{token}'})
    menu()

def checker():
    os.system("cls")
    logo()
    checked = 0
    hit = 0
    bad = 0
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    with open(txt) as f:
        for line in f:
            token = line.strip("\n")
            r = requests.get(f"https://discordapp.com/api/v6/auth/login",headers={'authorization':f'{token}'})
            if r.status_code == 200:
                hit += 1
                checked += 1
                os.system("cls")
                logo()
                print(Fore.YELLOW+f"[{token}]")
                print(Fore.LIGHTGREEN_EX+f"Good:{hit}")
                print(Fore.RED+f"Bad:{bad}")
                print(Fore.BLUE+f"Checked:{checked}")
                with open("Good.txt", "a+") as (k):
                    k.writelines(f"{token}\n")
            else:
                bad += 1
                checked += 1
                os.system("cls")
                logo()
                print(Fore.YELLOW+f"[{token}]")
                print(Fore.LIGHTGREEN_EX+f"Good:{hit}")
                print(Fore.RED+f"Bad:{bad}")
                print(Fore.BLUE+f"Checked:{checked}")
                with open("Bad.txt", "a+") as (k):
                    k.writelines(f"{token}\n")

    menu()



def leave():
    os.system("cls")
    logo()
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    ID=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Server ID ")
    os.system("cls")
    logo()
    print("Leaveing...")
    with open(txt) as f:
        for line in f:
            token = line.strip("\n")
            requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{ID}",headers={'authorization':f'{token}'})
    menu()

def bio():
    os.system("cls")
    logo()
    txt=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Import Tokens ")
    bioT=input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +">"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX+"Bio Text: ")
    os.system("cls")
    logo()
    payload ={
        "custom_status": {"text": "bioT"}
        }
    with open(txt) as f:
        for line in f:
            token = line.strip("\n")
            r = requests.patch(f"https://discord.com/api/v8/users/@me/settings",json=payload,headers={'authorization':f'{token}','content-type': 'application/json'})
            print(r.text)
    menu()
            
            


def menu():
    os.system("cls")
    logomenu()
    print("")
    option = int(input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +"?"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX))
    while option != 0:
        if option == 1:
            join()
            pass
        elif option == 2:
            leave()
            pass
        elif option == 3:
            message()
            pass
        elif option == 4:
            bypass()
            pass
        elif option == 5:
            checker()
            pass
        elif option == 6:
            bio()
            pass
        else:
            print("Invalid Option")
            os.system("cls")
            main()


menu()

