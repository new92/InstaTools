# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Python script for retrieving the (possible) location of the followers of an Instagram user !

*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only for the purpose of this script.
***************************
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 10
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import os
    import json
    import instaloader
    import requests
    from colorama import init, Fore
    from datetime import datetime
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Researcher have been installed !")
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
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
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
                    print("[1] Uninstall script")
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
YELLOW = Fore.YELLOW
RED = Fore.RED

print(f"{GREEN}[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def checkUser(user: str) -> bool:
    return user in ['None', '', ' '] or len(user) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def nums():
    print(f"{YELLOW}[1] Initiate Researcher")
    print(f"{YELLOW}[2] Show Reseacher's info")
    print(f"{YELLOW}[3] Uninstall Reseacher")
    print(f"{YELLOW}[4] Exit")

ANS = ['yes', 'no']

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

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

def banner():
    return f"""{YELLOW}
██████╗░███████╗░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗
██████╔╝█████╗░░╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝
██╔══██╗██╔══╝░░░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

def main():
    print(banner())
    print("\n")
    print(f"{YELLOW} [-] -- Socials --")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print(f"{YELLOW}[+] Leetcode: @new92")
    print("\n")
    print(f"{YELLOW}[+] Researcher: Python script for retrieving the possible location of the followers of a user on Instagram.")
    print("\n")
    nums()
    op=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while op < 1 or op > 4:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [1-4]")
        sleep(1)
        op=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if op == 1:
        clear()
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(2)
        con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        while con.lower() not in ANS or con in ['None', '', ' ']:
            if con in ['None', '', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        if con.lower() == ANS[0]:
            with open('cons.txt', 'a', encoding='utf8') as f:
                f.write(f"\n[=] Date: {datetime.now()}\n")
                f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
                f.write("-"*40)
        else:
            print(f"{YELLOW}[OK]")
            sleep(1)
            print(f"{YELLOW}[1] Exit")
            print(f"{YELLOW}[2] Uninstall Researcher and exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(2)
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(2)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Thank you for using Researcher 🫡")
                sleep(2)
                print(f"{GREEN}[+] Until we meet again 👋")
                sleep(1)
                quit(0)
        print(f"{YELLOW}[+] NOTE: The following username will be used to get the possible location of their followers.")
        sleep(4)
        username=str(input(f"{YELLOW}[::] Please enter the username: "))
        while checkUser(username):
            if username in ['None', '', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable username length: 30 or less characters")
            sleep(1)
            username=str(input(f"{YELLOW}[::] Please enter again the username: "))
        username = username.lower().strip()
        while valUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1.5)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-3]")
                sleep(2)
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(username):
                    if username in ['None', '', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length !")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable username length: 30 or less characters")
                    sleep(1)
                    username=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{GREEN}[+] Thank you for using Researcher 😁")
                sleep(2)
                print(f"{GREEN}[+] Until next time 👋")
                sleep(1)
                quit(0)
        loc=str(input(f"{YELLOW}[::] Please enter the location: "))
        while loc in ['None', '', ' ']:
            print(f"{YELLOW}[!] Invalid location !")
            sleep(1)
            loc=str(input(f"{YELLOW}[::] Please enter again the location: "))
        loc = loc.capitalize().strip()
        loader = instaloader.Instaloader()
        print(f'{YELLOW}|--------------------LOGIN--------------------|')
        user=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(user):
            if user in ['None', '', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable username length: 30 or less characters")
            sleep(1)
            user=str(input(f"{YELLOW}[::] Please enter again your username: "))
        user = user.lower().strip()
        while valUser(user):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-3]")
                sleep(2)
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(username):
                    if username in ['None', '', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length !")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable username length: 30 or less characters")
                    sleep(1)
                    username=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{GREEN}[+] Thank you for using Researcher 😁")
                sleep(2)
                print(f"{GREEN}[+] Until we meet again 🫡")
                sleep(1)
                quit(0)
        passw=str(input(f"{YELLOW}[::] Please enter your password: "))
        while passw in ['None', '', ' ']:
            print(f"{RED}[!] This field can't be blank !")
            sleep(1)
            passw=str(input(f"{YELLOW}[::] Please enter again your password: "))
        print(f'{YELLOW}|---------------------------------------------|')
        try:
            loader.login(user,passw)
        except Exception as ex:
            print(f"{RED}[!] Login Error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        profile = instaloader.Profile.from_username(loader.context, username)
        followers = [follower.username for follower in profile.get_followers()]
        LIST = []
        for i in range(len(followers)):
            profile = instaloader.Profile.from_username(loader.context, followers[i])
            if loc in profile.biography:
                LIST.append(followers[i])
        if len(LIST) == 0:
            print(f"{RED}[!] No users with such location found on the followers of {username}")
            sleep(3)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        else:
            per = (float(len(followers)) / len(LIST)) * 100
            name = f'users_in_{loc}.txt'
            with open(name, 'w', encoding='utf8') as f:
                print(f"{YELLOW}[+] Location: {loc}")
                print(f"{YELLOW}[+] Searched in user's: {username} followers")
                print(f"{YELLOW}[+] {len(LIST)} users in location: {loc}")
                print(f"{YELLOW}[+] Percentage of users with this location: {per}%")
                print(f'{YELLOW}\n|--------------------USERS--------------------|\n')
                for i in range(len(LIST)):
                    print(f"{YELLOW}[=] Username: {LIST[i]}")
                    f.write(f"[=] Username: {LIST[i]}")
                    f.write("\n")
            print(f"{GREEN}[✓] Successfully saved usersnames !")
            sleep(1)
            print(f"{GREEN}[↪] File name: {name}")
            print(f"{GREEN}[↪] Path: {fpath(name)}")
            print(f"{GREEN}[↪] File size: {os.stat(fpath(name)).st_size} bytes")
            sleep(3)

    elif op == 2:
        clear()
        ScriptInfo()
        print("\n\n")

    elif op == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Researcher 😁")
        sleep(2)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Researcher 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while number < 1 or number > 2:
        if number == None:
            print(f"{RED}[!] This field can't be blank !")
        else:
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
