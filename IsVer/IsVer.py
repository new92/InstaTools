# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Script in which the user enters a username and the script returns if the user with the specific username follows verified users.
If true then:
    The script finds and displays the usernames of the verified users followed by the user with the specific username
Else:
    The script exits

"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! IsVer requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IsVer ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from tqdm import tqdm
    total_mods = 8
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import os
    import json
    from os import system
    import instaloader
    import requests
    from prettytable import PrettyTable
    from colorama import init, Fore
except ImportError:
    print("[!] WARNING: Not all packages used in IsVer have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall IsVer")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall IsVer")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW

print(f"{GREEN}[✓] Successfully loaded modules !")
sleep(1)

ANS = ['yes', 'no']

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    fp = os.path.exists(fpath(f)) if not fpath(f) == None else None
    fsize = 0 if fp == None else os.stat(fpath(f)).st_size
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] Contributors : {conf['contributors']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}[+] Latest update: {conf['update']}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")
    
def banner() -> str:
    return f"""{YELLOW}
██╗░██████╗██╗░░░██╗███████╗██████╗░
██║██╔════╝██║░░░██║██╔════╝██╔══██╗
██║╚█████╗░╚██╗░██╔╝█████╗░░██████╔╝
██║░╚═══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██║██████╔╝░░╚██╔╝░░███████╗██║░░██║
╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝"""

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def checkUser(username:str) -> bool:
    return username in ['', ' ', 'None'] or len(username) > 30

def ValUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

def main():
    print(banner())
    print("\n")
    print(f"{YELLOW} [-] -- Socials --")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print(f"{YELLOW}[+] Leetcode: @new92")
    print("\n")
    print(f"{YELLOW}[+] With IsVer you can see if a user follows verified accounts and if yes which and how many (on Instagram)")
    print("\n")
    print(f"{YELLOW}[1] Initiate IsVer")
    print(f"{YELLOW}[2] Show IsVer's info")
    print(f"{YELLOW}[3] Uninstall IsVer")
    print(f"{YELLOW}[4] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-4]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print(f'{YELLOW}|--------------------LOGIN--------------------|')
        user=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(user):
            if user in ['None', '', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
            sleep(1)
            user=str(input(f"{YELLOW}[::] Please enter again your username: "))
        user = user.lower().strip()
        while ValUser(user):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            print(f"{YELLOW}[4] Uninstall IsVer and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(user):
                    if user in ['None', '', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length ! Acceptable length: <= 30 characters")
                    sleep(1)
                    user=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{GREEN}[+] Thank you for using IsVer 😁")
                sleep(2)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(2)
                quit(0)
        psw=str(input("[::] Please enter your password: "))
        while psw in ['None', '', ' ']:
            print("[!] This input can't be blank !")
            sleep(1)
            psw=str(input("[::] Please enter again your password: "))
        print(f'{YELLOW}|---------------------------------------------|')
        try:
            loader.login(user,psw)
        except Exception as ex:
            print(f"{RED}[!] Login error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            sleep(1)
            quit(0)
        username=str(input(f"{YELLOW}[::] Please enter the username of the target user: "))
        while checkUser(username):
            if username in ['None', '', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid username !")
            username=str(input(f"{YELLOW}[::] Please enter again the username of the target user: "))
        username = username.lower().strip()
        while ValUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            print(f"{YELLOW}[4] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                sleep(1)
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(username):
                    if username in ['None', '', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{GREEN}[+] Thank you for using IsVer 😁")
                sleep(2)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(2)
                quit(0)
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        keep=str(input(f"{YELLOW}[?] Keep log ? "))
        while keep.lower() not in ANS or keep in ['', ' ']:
            if keep in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(2)
            keep=str(input(f"{YELLOW}[?] Keep log ? "))
        keep = True if keep.lower() == ANS[0] else False
        name = 'IsVer_log.txt'
        profile=instaloader.Profile.from_username(loader.context, username)
        FOLLOWINGS = [following.username for following in profile.get_followees()]
        VERS = []
        for i in range(len(FOLLOWINGS)):
            ver_profile = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
            if ver_profile.is_verified:
                VERS.append(FOLLOWINGS[i])
        followees = profile.followees
        print(f"{YELLOW}[+] Is {username} following verified accounts ? {len(VERS) == 0}")
        if len(VERS) == 0:
            sleep(2)
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while num < 1 or num > 2:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(2)
                num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Thank you for using IsVer 😁")
                quit(0)
        else:
            print(f"{YELLOW}[+] {username} follows {len(VERS)} verified accounts")
            sleep(2)
            table = PrettyTable()
            table.field_names = ['usernames', 'followers', 'followings']
            for i in range(len(VERS)):
                table.add_row([VERS[i], VERS[i].followers, VERS[i].followings])
            print(table)
            sleep(5)
            print(f"{GREEN}[+] Percentage of verified accounts followed by {username} ==> {float(len(VERS)) / len(FOLLOWINGS)*100}%")
            sleep(2)
            print(f"{GREEN}[+] Verified followings: {len(VERS)}/{followees}")
            if keep:
                with open(name, 'w', encoding='utf8') as fp:
                    fp.write(str(table))
                print(f"{GREEN}[✓] Successfully saved log !")
                sleep(2)
                print(f"{GREEN}[↪] File name: {name}")
                print(f"{GREEN}[↪] Path: {fpath(name)}")
                print(f"{GREEN}[↪] File size: {os.stat(fpath(name)).st_size} bytes")
                sleep(3)
    elif num == 2:
        clear()
        ScriptInfo()
        print("\n\n")
        print(f"{YELLOW}[1] Return to menu")
        print(f"{YELLOW}[2] Exit")
        number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while number < 1 or number > 2:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable numbers: [1/2]")
            sleep(2)
            number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
        if number == 1:
            clear()
            main()
        else:
            clear()
            print(f"{YELLOW}[+] Exiting...")
            sleep(1)
            print(f"{GREEN}[+] See you next time 👋")
            sleep(2)
            quit(0)
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(2)
        quit(0)
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while number < 1 or number > 2:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(2)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if number == 1:
        clear()
        main()
    else:
        print(f"{YELLOW}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(2)
        quit(0)

if __name__ == '__main__':
    main()
