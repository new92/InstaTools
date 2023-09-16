# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Tracker: Track with this script the followers and followings of a user.
When the script notice a change in the followers or the followings of the specified user it will inform you about that change
Feature --> Tracker will also inform you if the specified user removed a follower or followee
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! Tracker requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use Tracker ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 13
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
    from instaloader import ConnectionException
except ImportError:
    print("[!] WARNING: Not all packages used in Tracker have been installed !")
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
                print("[1] Uninstall Tracker")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall Tracker")
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

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

print(f"{GREEN}[✓] Successfully loaded modules !")
sleep(1)

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

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(f).st_size
    else:
        fsize = 0
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def logo() -> str:
    return f"""{YELLOW}
    ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """

def checkUser(username:str) -> bool:
    return username in [None, '', ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def main():
    print(logo())
    print("\n")
    print(f"{YELLOW} [-] -- Socials --")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print(f"{YELLOW}[+] Leetcode: @new92")
    print("\n")
    print(f"{YELLOW}[+] Tracker: Python script to keep track on the followers/followings of a user.")
    print("\n")
    print(f"{YELLOW}[1] Start Tracker")
    print(f"{YELLOW}[2] Display Tracker's info")
    print(f"{YELLOW}[3] Uninstall Tracker")
    print(f"{YELLOW}[4] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4 or num == None:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{YELLOW}[1] Start Tracker")
        print(f"{YELLOW}[2] Display Tracker's info")
        print(f"{YELLOW}[3] Uninstall Tracker")
        print(f"{YELLOW}[4] Exit")
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        print(f'{GREEN}|---------------|LOGIN|---------------|')
        username=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(username):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            username=str(input(f"{YELLOW}[::] Please enter again the username: "))
        username = username.lower().strip()
        while valUser(username):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 3 or opt == None:
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{YELLOW}[1] Try with another username")
                    print(f"{YELLOW}[2] Return to menu")
                    print(f"{YELLOW}[3] Uninstall and Exit")
                    opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if opt == 1:
                    username=str(input(f"{YELLOW}[::] Please enter the username: "))
                    while checkUser(username):
                        print(f"{RED}[!] Invalid username !")
                        sleep(1)
                        username=str(input(f"{YELLOW}[::] Please enter again the username: "))
                elif opt == 2:
                    clear()
                    main()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{YELLOW}[+] Thank you for using Tracker 😁")
                    sleep(2)
                    print(f"{YELLOW}[+] Hope you enjoyed it ! ☺️")
                    sleep(2)
                    print(f"{YELLOW}[+] Until next time 👋")
                    sleep(1)
                    quit(0)
        loader = instaloader.Instaloader()
        password=str(input(f"{YELLOW}[::] Please enter your password: "))
        while password in ['', ' ', None]:
            print(f"{RED}[!] This field can't be blank !")
            sleep(1)
            password=str(input(f"{YELLOW}[::] Please enter again your password: "))
        print(f'{GREEN}|-----------------------------------|')
        try:
            loader.login(username,password)
        except ConnectionException as ex:
            print(f"{RED}[!] Login Error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        print(f"{GREEN}[✓] Login successfull !")
        sleep(1)
        print(f"{YELLOW}[1] Track followers")
        print(f"{YELLOW}[2] Track followees")
        print(f"{YELLOW}[3] Track both")
        number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while number < 1 or number > 3 or number == None:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{YELLOW}[1] Track followers")
            print(f"{YELLOW}[2] Track followees")
            print(f"{YELLOW}[3] Track both")
            number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        user=str(input(f"{YELLOW}[::] Please enter the username of the user: "))
        while checkUser(user):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            user=str(input(f"{YELLOW}[::] Please enter again the username of the user: "))
        user = user.lower().strip()
        while valUser(user):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(user):
                    print(f"{RED}[!] Invalid username !")
                    sleep(1)
                    user=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using Tracker 😁")
                sleep(2)
                print(f"{YELLOW}[+] Hope you enjoyed it ! 👍")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
        name = 'trackerResults.txt'
        if number == 1:
            profile = instaloader.Profile.from_username(loader.context, user)
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
            FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
            while FOLLOWERS == FOLLOWERSAF:
                print(f"{YELLOW}[+] No new additions found on: {user}")
                sleep(1)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                FOLLOWERS = [follower.username for follower in profile.get_followers()]
                FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
            if abs(len(FOLLOWERSAF) - len(FOLLOWERS)) > 1:
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    print(f"{GREEN}[*] {user} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} followers.")
                    sleep(2)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for follower in FOLLOWERS:
                        if follower not in FOLLOWERSAF:
                            print(f"{YELLOW}[⇒] Username: {follower}")
                else:
                    print(f"{GREEN}[*] {user} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for follower in FOLLOWERSAF:
                        if follower not in FOLLOWERS:
                            print(f"{YELLOW}[⇒] Username: {follower}")
                sleep(4)
            else:
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    print(f"{GREEN}[*] {user} removed 1 follower.")
                    sleep(1)
                    print(f"{YELLOW}[+] Username: {[follower for follower in FOLLOWERS if follower not in FOLLOWERSAF][0]}")
                else:
                    print(f"{GREEN}[*] {user} added 1 follower.")
                    sleep(2)
                    print(f"{YELLOW}[+] Username: {[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}")
            sleep(2)
            print(f"{GREEN}[+] Acceptable answers: [true/false]")
            sleep(1)
            kp=str(input(f"{YELLOW}[?] Keep log ? "))
            while kp in [None, '', ' '] or kp.lower() not in ['true', 'false']:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable asnwers: [true/false]")
                sleep(1)
                kp=str(input(f"{YELLOW}[?] Keep log ? "))
            if kp.lower() == 'true':
                f = open(name, 'w')
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    for i in range(len(FOLLOWERS)):
                        if FOLLOWERS[i] not in FOLLOWERSAF:
                            f.write(str(i+1) + ') ' + FOLLOWERS[i])
                else:
                    for i in range(len(FOLLOWERSAF)):
                        if FOLLOWERSAF[i] not in FOLLOWERS:
                            f.write(str(i+1) + ') ' + FOLLOWERSAF[i])
                f.close()
                print(f"{GREEN}[✓] Successfully saved log !")
                sleep(2)
                print(f"{YELLOW}[↪] Log file name: {name}")
                print(f"{YELLOW}[↪] Location: {fpath(name)}")
                print(f"{YELLOW}[↪] File size: {os.stat(fpath(name)).st_size} bytes")
                sleep(3)
        elif number == 2:
            profile = instaloader.Profile.from_username(loader.context, user)
            FOLLOWEES = [followee.username for followee in profile.get_followees()]
            FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
            while FOLLOWEES == FOLLOWEESAF:
                print(f"{YELLOW}[+] No new additions found on: {user}")
                sleep(1)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                FOLLOWEES = [followee.username for followee in profile.get_followees()]
                FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
            if abs(len(FOLLOWEESAF) - len(FOLLOWEES)) > 1:
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    print(f"{GREEN}[*] {user} stopped following {len(FOLLOWEES) - len(FOLLOWEESAF)} users.")
                    sleep(2)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for followee in FOLLOWEES:
                        if followee not in FOLLOWEESAF:
                            print(f"{YELLOW}[⇒] Username: {followee}")
                else:
                    print(f"{GREEN}[*] {user} started following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for followee in FOLLOWEESAF:
                        if followee not in FOLLOWEES:
                            print(f"{YELLOW}[⇒] Username: {followee}")
                sleep(4)
            else:
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    print(f"{GREEN}[*] {user} stopped following 1 user.")
                    sleep(1)
                    print(f"{YELLOW}[+] Username: {[followee for followee in FOLLOWEES if followee not in FOLLOWEESAF][0]}")
                else:
                    print(f"{GREEN}[*] {user} started following 1 user.")
                    sleep(2)
                    print(f"{YELLOW}[+] Username: {[followee for followee in FOLLOWEESAF if followee not in FOLLOWEES][0]}")
            sleep(2)
            print(f"{GREEN}[+] Acceptable answers: [true/false]")
            sleep(1)
            kp=str(input(f"{YELLOW}[?] Keep log ? "))
            while kp in [None, '', ' '] or kp.lower() not in ['true', 'false']:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [true/false]")
                sleep(1)
                kp=str(input(f"{YELLOW}[?] Keep log ? "))
            if kp.lower() == 'true':
                f = open(name, 'w')
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    for i in range(len(FOLLOWEES)):
                        if FOLLOWEES[i] not in FOLLOWEESAF:
                            f.write(str(i+1) + ') ' + FOLLOWEES[i])
                else:
                    for i in range(len(FOLLOWEESAF)):
                        if FOLLOWEESAF[i] not in FOLLOWEES:
                            f.write(str(i+1) + ') ' + FOLLOWEESAF[i])
                f.close()
                print(f"{GREEN}[✓] Successfully saved log !")
                sleep(2)
                print(f"{YELLOW}[↪] Log file name: {name}")
                print(f"{YELLOW}[↪] Location path: {fpath(name)}")
                print(f"{YELLOW}[↪] File size: {os.stat(fpath(name)).st_size} bytes")
                sleep(3)
        else:
            profile = instaloader.Profile.from_username(loader.context, user)
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
            FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
            FOLLOWEES = [followee.username for followee in profile.get_followees()]
            FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
            while FOLLOWERS == FOLLOWERSAF or FOLLOWEES == FOLLOWEESAF:
                print(f"{YELLOW}[+] No new additions found on {user}")
                sleep(1)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                FOLLOWERS = [follower.username for follower in profile.get_followers()]
                FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
                FOLLOWEES = [followee.username for followee in profile.get_followees()]
                FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
            if FOLLOWERS != FOLLOWERSAF:
                print(f"{GREEN}[*] Detected change on the user's followers...")
                sleep(2)
                if abs(len(FOLLOWERSAF) - len(FOLLOWERS)) > 1:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        print(f"{GREEN}[*] {user} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} followers.")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for follower in FOLLOWERS:
                            if follower not in FOLLOWERSAF:
                                print(f"{YELLOW}[⇒] Username: {follower}")
                    else:
                        print(f"{GREEN}[*] {user} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for follower in FOLLOWERSAF:
                            if follower not in FOLLOWERS:
                                print(f"{YELLOW}[⇒] Username: {follower}")
                    sleep(4)
                else:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        print(f"{GREEN}[*] {user} removed 1 follower.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username: {[usr for usr in FOLLOWERS if usr not in FOLLOWERSAF][0]}")
                        sleep(1)
                    else:
                        print(f"{GREEN}[*] {user} added 1 follower.")
                        sleep(1)
                        print(f"{YELLOW}[*] Username: {[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}")
                        sleep(1)
            else:
                print(f"{GREEN}[*] Detected change on the user's followings...")
                sleep(2)
                if abs(len(FOLLOWEESAF) - len(FOLLOWEES)) > 1:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        print(f"{GREEN}[*] {user} stopped following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for followee in FOLLOWEES:
                            if followee not in FOLLOWEESAF:
                                print(f"{YELLOW}[⇒] Username: {followee}")
                    else:
                        print(f"{GREEN}[*] {user} started following {len(FOLLOWEESAF) - len(FOLLOWEES)}")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for followee in FOLLOWEESAF:
                            if followee not in FOLLOWEES:
                                print(f"{YELLOW}[⇒] Username: {followee}")
                    sleep(4)
                else:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        print(f"{GREEN}[*] {user} stopped following 1 user.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username: {[FOLLOWEES[i] for i in range(len(FOLLOWEES)) if FOLLOWEES[i] not in FOLLOWEESAF][0]}")
                    else:
                        print(f"{GREEN}[*] {user} started following 1 user.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username: {[FOLLOWEESAF[i] for i in range(len(FOLLOWEESAF)) if FOLLOWEESAF[i] not in FOLLOWEES][0]}")
                    sleep(2)
            print(f"{GREEN}[+] Acceptable answers: [true/false]")
            sleep(1)
            keep=str(input(f"{YELLOW}[?] Keep log ? "))
            while keep in [None, '', ' '] or keep.lower() not in ['true', 'false']:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{YELLOW}[+] Acceptable answers: [true/false]")
                sleep(2)
                keep=str(input(f"{YELLOW}[?] Keep log ? "))
            if keep.lower() == 'true':
                f = open(name, 'w')
                if len(FOLLOWEES) != len(FOLLOWEESAF):
                    pass

    elif num == 2:
        clear()
        ScriptInfo()
        print("\n\n")
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{YELLOW}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{YELLOW}[+] Hope you enjoyed it ! 👍")
        sleep(2)
        print(f"{YELLOW}[+] Until next time 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while numb < 1 or numb > 2 or numb == None:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if numb == 1:
        clear()
        main()
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()