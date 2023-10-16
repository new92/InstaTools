# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Mutuals is a powerful Python script designed to discover and display mutual followers and followings between two Instagram accounts. Whether you're looking to strengthen connections or gain insights into shared networks, Mutuals simplifies the process, allowing users to identify and connect with those who share mutual interests and connections on Instagram.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print(f"[!] Error ! Mutuals requires Python version 3.X ! ")
        sleep(2)
        print(f"""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print(f"[*] Please install Python 3 and then use Mutuals ✅")
        sleep(2)
        print(f"[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 8
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import instaloader
    import os
    import json
    import requests
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print(f"[!] WARNING: Not all packages used in Mutuals have been installed !")
    sleep(2)
    print(f"[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print(f"[!] Root user not detected !")
            sleep(2)
            print(f"[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print(f"[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print(f"[1] Uninstall Mutuals")
                print(f"[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print(f"[!] Invalid number !")
                    sleep(1)
                    print(f"[+] Acceptable numbers: [1/2]")
                    sleep(2)
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
                    print(f"[✓] Files and dependencies uninstalled successfully !")
                else:
                    print(f"[+] Exiting...")
                    sleep(1)
                    print(f"[+] See you next time 👋")
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

sleep(0.8)
console.clear()
console.print("[bold dark_green][✓] Successfully loaded modules.")
sleep(0.8)
console.clear()

def checkUser(username:str) -> bool:
    return username in ['' , ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    fp = True if not fpath(f) == None else False
    fsize = 0 if not fp else os.stat(fpath(f)).st_size
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
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def banner() -> str:
    return f"""{YELLOW}
███╗░░░███╗██╗░░░██╗████████╗██╗░░░██╗░█████╗░██╗░░░░░░██████╗      ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
████╗░████║██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░██╔════╝      ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║░░░██║░░░██║░░░██║░░░██║███████║██║░░░░░╚█████╗░      █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║╚██╔╝██║██║░░░██║░░░██║░░░██║░░░██║██╔══██║██║░░░░░░╚═══██╗      ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░╚═╝░██║╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗██████╔╝      ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░      ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def nums():
    print(f"{YELLOW}[1] Find mutuals")
    print(f"{YELLOW}[2] Show Mutual's info")
    print(f"{YELLOW}[3] Update Mutuals")
    print(f"{YELLOW}[4] Uninstall Mutuals")
    print(f"{YELLOW}[5] Exit")

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
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

def main():
    print(banner())
    print(f"\n")
    print(f"{YELLOW} [-] -- Socials --")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print(f"{YELLOW}[+] Leetcode: @new92")
    print(f"\n")
    print(f"{YELLOW}[+] Python script to retrieve the mutual followers/followings between 2 accounts.")
    print(f"\n")
    nums()
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 5:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print(f'{YELLOW}|--------------------|LOGIN|--------------------|')
        user=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(user):
            if user in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
            sleep(1)
            user=str(input(f"{YELLOW}[::] Please enter again your username: "))
        user = user.lower().strip()
        while valUser(user):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            print(f"{YELLOW}[4] Uninstall Mutuals and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                sleep(2)
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(user):
                    if user in ['', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
                    sleep(1)
                    user=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using Mutuals 😁")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(2)
                quit(0)
        psw=str(input(f"{YELLOW}[::] Please enter your password: "))
        while psw in ['', ' ']:
            print(f"{RED}[!] This field can't be blank !")
            sleep(1)
            psw=str(input(f"{YELLOW}[::] Please enter again your password: "))
        print(f'{YELLOW}|-----------------------------------------------|')
        try:
            loader.login(user,psw)
        except Exception as ex:
            print(f"{RED}[!] Login error !")
            sleep(1)
            print(f"{YELLOW}[+] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            sleep(1)
            quit(0)
        print(f"{GREEN}[✓] Login successfull !")
        sleep(2)
        print(f"{YELLOW}[1] Find the mutual followers between 2 accounts")
        print(f"{YELLOW}[2] Find the mutual followees between 2 accounts")
        t=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while t < 1 or t > 2:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable numbers: [1/2]")
            sleep(2)
            print(f"{YELLOW}[1] Find mutual followers")
            print(f"{YELLOW}[2] Find mutual followees")
            t=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
        usernamef=str(input(f"{YELLOW}[::] Please enter the first username: "))
        while checkUser(usernamef):
            if usernamef in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length ! Acceptable length: <= 30 characters")
            sleep(1)
            usernamef=str(input(f"{YELLOW}[::] Please enter again the first username: "))
        usernamef = usernamef.lower().strip()
        while valUser(usernamef):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            print(f"{YELLOW}[4] Uninstall Mutuals and Exit")
            optf=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while optf < 1 or optf > 4:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                sleep(2)
                optf=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if optf == 1:
                usernamef=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(usernamef):
                    if usernamef in ['', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
                    sleep(1)
                    usernamef=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif optf == 2:
                clear()
                main()
            elif optf == 3:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                sleep(2)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(2)
                quit(0)
        usernames=str(input(f"{YELLOW}[::] Please enter the second username: "))
        while checkUser(usernames):
            if usernames in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
            sleep(1)
            usernames=str(input(f"{YELLOW}[::] Please enter again the second username: "))
        usernames = usernames.lower().strip()
        while valUser(usernames):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            print(f"{YELLOW}[4] Uninstall Mutuals and Exit")
            opts=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opts < 1 or opts > 4:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                sleep(1)
                opts=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opts == 1:
                usernames=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(usernames):
                    if usernames in ['', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length ! Acceptable length: <= 30 characters")
                    sleep(1)
                    usernames=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opts == 2:
                clear()
                main()
            else:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
        profilef=instaloader.Profile.from_username(loader.context, usernamef)
        profiles=instaloader.Profile.from_username(loader.context, usernames)
        ANS = ['yes','no']
        if t == 1:
            clear()
            FOLLOWERSF=[follower.username for follower in profilef.get_followers()]
            FOLLOWERSS=[follower.username for follower in profiles.get_followers()]
            if len(FOLLOWERSF) != 0 and len(FOLLOWERSS) != 0:
                allf = len(FOLLOWERSF) + len(FOLLOWERSS)
                if len(FOLLOWERSF) > len(FOLLOWERSS):
                    x = len(FOLLOWERSF) - len(FOLLOWERSS)
                    MUTUALS = [FOLLOWERSF[i] for i in range(len(FOLLOWERSF)) if FOLLOWERSF[i] in FOLLOWERSS]
                    if len(MUTUALS) == 0:
                        print(f"{RED}[!] No mutual followers found !")
                        sleep(2)
                        print(f"{YELLOW}[+] Exiting")
                        sleep(1)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        quit(0)
                    else:
                        print(f"{GREEN}[✓] Successfully found mutual followers !")
                        sleep(1)
                        per = (len(MUTUALS) / float(allf))*100
                        print(f"{YELLOW}[+] Number of mutual followers: {len(MUTUALS)}")
                        sleep(1)
                        print(f"{YELLOW}[+] Percentage of mutual followers: {per}%")
                        sleep(1)
                        print(f"{YELLOW}[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"{YELLOW}[+] Username No{k+1}: {MUTUALS[k]}")
                        sleep(3)
                        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                        sleep(1)
                        savem=str(input(f"{YELLOW}[?] Save the mutual followers ? "))
                        while savem.lower() not in ANS or savem in ['', ' ']:
                            print(f"{RED}[!] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                            sleep(1)
                            savem=str(input(f"{YELLOW}[?] Save the mutual followers ? "))
                        if savem.lower() == ANS[0]:
                            name = 'mutuals.txt'
                            with open(name, 'w', encoding='utf8') as f:
                                for i in range(len(MUTUALS)):
                                    f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            sleep(1.5)
                            print(f"{GREEN}[✓] Successfully saved the mutual followers !")
                            sleep(2)
                            print(f"{YELLOW}[↪] Name: {name}")
                            print(f"{YELLOW}[↪] Location: {fpath(name)}")
                            print(f"{YELLOW}[↪] Size: {(os.stat(fpath(name))).st_size} bytes")
                            sleep(2)
                    clear()
                    x = len(FOLLOWERSS) - len(FOLLOWERSF)
                    MUTUALS = [FOLLOWERSS[i] for i in range(len(FOLLOWERSF)+x) if FOLLOWERSS[i] in FOLLOWERSF]
                    if len(MUTUALS) == 0:
                        print(f"{RED}[!] No mutual followers found !")
                        sleep(2)
                        print(f"{YELLOW}[+] Exiting...")
                        sleep(1)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        quit(0)
                    else:
                        per = len(MUTUALS) / float(allf)*100
                        print(f"{YELLOW}[+] Number of mutual followers: {len(MUTUALS)}")
                        sleep(1)
                        print(f"{YELLOW}[+] Percentage of mutual followers: {per}%")
                        sleep(1)
                        print(f"{YELLOW}[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"{YELLOW}[+] Username No{k+1}: {MUTUALS[k]}")
                        sleep(3)
                        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                        sleep(1)
                        savem=str(input(f"{YELLOW}[?]  Save the mutual followers ? "))
                        while savem.lower() not in ANS or savem in ['', ' ']:
                            print(f"{RED}[!] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                            sleep(1)
                            savem=str(input(f"{YELLOW}[?] Save the mutual followers ? "))
                        if savem.lower() == ANS[0]:
                            name = 'mutuals.txt'
                            with open(name, 'w', encoding='utf8') as f:
                                for i in range(len(MUTUALS)):
                                    f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            sleep(1.5)
                            print(f"{GREEN}[✓] Successfully saved mutual followers !")
                            sleep(2)
                            print(f"{YELLOW}[↪] Name: {name}")
                            print(f"{YELLOW}[↪] Location: {fpath(name)}")
                            print(f"{YELLOW}[↪] Size: {os.stat(fpath(name)).st_size} bytes")
                            sleep(1)
            else:
                print(f"{RED}[!] No followers found !")
                sleep(2)
                if len(FOLLOWERSF) == 0:
                    print(f"{YELLOW}[+] No followers found on: {usernamef}")
                else:
                    print(f"{YELLOW}[+] No followers found on: {usernames}")
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                sleep(2)
                quit(0)
        else:
            clear()
            FOLLOWEESF=[followee.username for followee in profilef.get_followees()]
            FOLLOWEESS=[followee.username for followee in profiles.get_followees()]
            if len(FOLLOWEESF) != 0 and len(FOLLOWEESS) != 0:
                allfe = len(FOLLOWEESF) + len(FOLLOWEESS)
                if len(FOLLOWEESF) > len(FOLLOWEESS):
                    x = len(FOLLOWEESF) - len(FOLLOWEESS)
                    MUTUALS = [FOLLOWEESF[i] for i in range(len(FOLLOWEESS)+x) if FOLLOWEESF[i] in FOLLOWEESS]
                    if len(MUTUALS) == 0:
                        print(f"{RED}[!] No mutual followees found !")
                        sleep(2)
                        print(f"{YELLOW}[+] Exiting...")
                        sleep(1)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        quit(0)
                    else:
                        per = (len(MUTUALS) / float(allfe))*100
                        print(f"{YELLOW}[+] Number of mutual followees: {len(MUTUALS)}")
                        sleep(1)
                        print(f"{YELLOW}[+] Percentage of mutual followees: {per}%")
                        sleep(1)
                        print(f"{YELLOW}[+] The usernames of the mutual followees: ")
                        for k in range(len(MUTUALS)):
                            print(f"{YELLOW}[+] Username No{k+1}: {MUTUALS[k]}")
                        sleep(2)
                        print(f'{GREEN}[+] Acceptable answers: [yes/no]')
                        sleep(2)
                        savem=str(input(f"{YELLOW}[?] Save the mutual followees ? "))
                        while savem.lower() not in ANS or savem in ['', ' ']:
                            print(f"{RED}[!] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                            sleep(1)
                            savem=str(input(f"{YELLOW}[?] Save the mutual followees ? "))
                        if savem.lower() == ANS[0]:
                            name = 'mutualsf.txt'
                            with open(name, 'w', encoding='utf8') as f:
                                for i in range(len(MUTUALS)):
                                    f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            sleep(1)
                            print(f"{GREEN}[✓] Successfully saved mutual followees !")
                            sleep(2)
                            print(f"{YELLOW}[↪] Name: {name}")
                            print(f"{YELLOW}[↪] Location: {fpath(name)}")
                            print(f"{YELLOW}[↪] Size: {os.stat(fpath(name)).st_size}")
                        sleep(1)
            else:
                print(f"{RED}[!] No followees found !")
                sleep(1)
                if len(FOLLOWEESF) == 0:
                    print(f"{YELLOW}[+] Followees not found on: {usernamef}")
                else:
                    print(f"{YELLOW}[+] Followees not found on: {usernames}")
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                quit(0)
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")

    elif num == 3:
        clear()
        system('git pull')
        sleep(1)
        print(f"{GREEN}[✓] Script updated successfully !")
        sleep(1)
        
    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
        sleep(2)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
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
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(2)
        quit(0)

if __name__ == '__main__':
    main()
