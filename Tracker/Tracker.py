# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

Tracker: Track with this script the followers and followings of a user.
When the user specified add a new follower or start to follow a user the script will inform you about the specific user.
"""
try:
    import sys
    if sys.version_info[0] < 3:
        print("[!] Error ! Tracker requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(1)
        print("[*] Please install the Python 3 and then use Tracker ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    from time import sleep
    import os
    import instaloader
    import requests
    import datetime
    from colorama import Fore, init
    from tkinter import messagebox
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
                print("[1] Uninstall script")
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
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
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
                    rmdir(os.path.abspath('InstaTools'))
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
    rmdir(os.path.abspath('InstaTools'))
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def ScriptInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'es-US'
    language = 'Python'
    name = 'Tracker'
    api = None
    lines = 450
    f = name+'.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 10
    forks = 5
    issues = 0
    clissues = 0
    prs = 0
    clprs = 1
    discs = 1
    print(f"{YELLOW}[+] Author: {author}")
    print(f"{YELLOW}[+] Github: @{author}")
    print(f"{YELLOW}[+] License: {lice}")
    print(f"{YELLOW}[+] Natural language: {lang}")
    print(f"{YELLOW}[+] Programming language(s) used: {language}")
    print(f"{YELLOW}[+] Number of lines: {lines}")
    print(f"{YELLOW}[+] Script's name: {name}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] API(s) used: {api}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {stars}")
    print(f"{YELLOW}[+] Forks: {forks}")
    print(f"{YELLOW}[+] Open issues: {issues}")
    print(f"{YELLOW}[+] Closed issues: {clissues}")
    print(f"{YELLOW}[+] Open pull requests: {prs}")
    print(f"{YELLOW}[+] Closed pull requests: {clprs}")
    print(f"{YELLOW}[+] Discussions: {discs}")

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
    return username == None or len(username) > 30

def main():
    print(logo())
    print("\n")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print("\n")
    print(f"{YELLOW}[+] Tracker: Python script to keep track on the followers/followings of a user.")
    print("\n")
    print(f"{YELLOW}[1] Start Tracker")
    print(f"{YELLOW}[2] Show Tracker's info")
    print(f"{YELLOW}[3] Uninstall Tracker")
    print(f"{YELLOW}[4] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4 or num == None:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{YELLOW}[1] Start Tracker")
        print(f"{YELLOW}[2] Show Tracker's info")
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
        while requests.get(f"https://www.instagram.com/{username}/").status_code != 200:
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
                    main()
                else:
                    print(Uninstall())
                    sleep(2)
                    print(f"{YELLOW}[+] Thank you for using my script 😁")
                    sleep(2)
                    print(f"{YELLOW}[+] Hope you enjoyed it ! ☺️")
                    sleep(2)
                    print(f"{YELLOW}[+] Until next time 👋")
                    sleep(1)
                    quit(0)
        loader = instaloader.Instaloader()
        password=str(input(f"{YELLOW}[::] Please enter your password: "))
        while password == None:
            print(f"{RED}[!] You must enter a password !")
            sleep(1)
            password=str(input(f"{YELLOW}[::] Please enter again your password: "))
        try:
            loader.login(username,password)
        except Exception as ex:
            print(f"{RED}[!] Login Error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        print(f'{YELLOW}|-----------------------------------|')
        print("\n")
        print(f"{YELLOW}[1] Track followers")
        print(f"{YELLOW}[2] Track followees")
        print(f"{YELLOW}[3] Track both")
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while num not in range(1,4) or num == None:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{YELLOW}[1] Track followers")
            print(f"{YELLOW}[2] Track followees")
            print(f"{YELLOW}[3] Track both")
            num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        user=str(input(f"{YELLOW}[::] Please enter the username of the user: "))
        while checkUser(user):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            user=str(input(f"{YELLOW}[::] Please enter again the username of the user: "))
        user = user.lower().strip()
        while requests.get(f"https://www.instagram.com/{user}/").status_code != 200:
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
                main()
            else:
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using my script 😁")
                sleep(2)
                print(f"{YELLOW}[+] Hope you enjoyed it ! 👍")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
        name = 'additions.txt'
        if num == 1:
            profile = instaloader.Profile.from_username(loader.context, user)
            followers_bef = [follower.username for follower in profile.get_followers()]
            followers_af = [follower.username for follower in profile.get_followers()]
            while followers_bef == followers_af:
                sleep(7200)
                followers_bef = [follower.username for follower in profile.get_followers()]
                followers_af = [follower.username for follower in profile.get_followers()]
            if len(followers_af) - len(followers_bef) == 1:
                messagebox.showinfo('follower addition'.upper(),f'{user} added a new follower \n▶ {followers_af[-1]}')
            else:
                f = open(name,'a')
                count = 0
                f.write('-'*20+str(datetime.date.today())+'-'*20)
                for i in range(0,-(len(followers_af) - len(followers_bef))-1,-1):
                    f.write(f'▶ {followers_af[i]}\n')
                    count += 1
                f.write("-"*50)
                f.close()
                messagebox.showinfo('followers added'.upper(),f'{user} added a total of {count} followers') 
                sleep(2)
                messagebox.showinfo('file'.upper(),f'Saved usernames at {os.path.abspath(name)}')
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while numb < 1 or numb > 2 or numb == None:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if numb == 1:
                main()
            else:
                print(f"{YELLOW}[+] Thank you for using my script 😁")
                sleep(2)
                print(f"{YELLOW}[+] See you next time 👋")
                sleep(1)
                quit(0)
        elif num == 2:
            profile = instaloader.Profile.from_username(loader.context, user)
            followings_bef = [following.username for following in profile.get_followees()]
            followings_af = [following.username for following in profile.get_followees()]
            while followings_bef == followings_af:
                sleep(7200)
                followings_bef = [following.username for following in profile.get_followees()]
                followings_af = [following.username for following in profile.get_followees()]
            if len(followings_af) - len(followings_bef) == 1:
                messagebox.showinfo('following addition'.upper(),f'{user} started following \n ▶{followings_af[-1]}')
            else:
                f = open(name,'a')
                count = 0
                f.write('-'*20+str(datetime.date.today())+'-'*20)
                for i in range(0,-(len(followings_af) - len(followings_bef))-1,-1):
                    f.write(f'▶ {followings_af[i]}\n')
                    count += 1
                f.write('-'*50)
                f.close()
                messagebox.showinfo('followings added'.upper(),f'{user} started following a total of {count} users')
                sleep(2)
                messagebox.showinfo('file'.upper(),f'Saved usernames at {os.path.abspath(name)}')
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while numb < 1 or numb > 2 or numb == None:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if numb == 1:
                main()
            else:
                print(f"{YELLOW}[+] Thank you for using my script 😁")
                sleep(2)
                print(f"{YELLOW}[+] See you next time 👋")
                sleep(1)
                quit(0)
        elif num == 3:
            profile = instaloader.Profile.from_username(loader.context, user)
            followers_bef = [follower.username for follower in profile.get_followers()]
            followers_af = [follower.username for follower in profile.get_followers()]
            followings_bef = [following.username for following in profile.get_followees()]
            followings_af = [following.username for following in profile.get_followees()]
            while followers_af == followers_bef and followings_af == followings_bef:
                sleep(7200)
                followers_bef = [follower.username for follower in profile.get_followers()]
                followers_af = [follower.username for follower in profile.get_followers()]
                followings_bef = [following.username for following in profile.get_followees()]
                followings_af = [following.username for following in profile.get_followees()]
            if followers_af != followers_bef:
                if len(followers_af) - len(followers_bef) == 1:
                    messagebox.showinfo('follower addition'.upper(),f'{user} added a new follower \n▶ {followers_af[-1]}')
                else:
                    f = open(name,'a')
                    count = 0
                    f.write('-'*20+str(datetime.date.today())+'-'*20)
                    for i in range(0, -(len(followers_af) - len(followers_bef))-1,-1):
                        f.write(f'▶ {followers_af[i]}\n')
                        count += 1
                    f.write('-'*50)
                    f.close()
                    messagebox.showinfo('followers added'.upper(),f'{user} added a total of {count} followers')
                    sleep(2)
                    messagebox.showinfo('file'.upper(),f'Saved usernames at {os.path.abspath(name)}')
            else:
                if len(followings_af) - len(followings_bef) == 1:
                    messagebox.showinfo('following addition'.upper(),f'{user} started following \n▶ {followings_af[-1]}')
                else:
                    f = open(name,'a')
                    count = 0
                    f.write('-'*20+str(datetime.date.today())+'-'*20)
                    for i in range(0,-(len(followings_af) - len(followings_bef))-1, -1):
                        f.write(f'▶ {followings_af[i]}\n')
                        count += 1
                    f.write('-'*50)
                    f.close()
                    messagebox.showinfo('followings addedd'.upper(),f'{user} started following a total of {count} users')
                    sleep(2)
                    messagebox.showinfo('file'.upper(),f'Saved usernames at {os.path.abspath(name)}')
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while numb < 1 or numb > 2 or numb == None:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if numb == 1:
                main()
            else:
                print(f"{YELLOW}[+] Thank you for using my script 😁")
                sleep(2)
                print(f"{YELLOW}[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif num == 2:
        clear()
        ScriptInfo()
    elif num == 3:
        clear()
        print(Uninstall())
        print(f"{YELLOW}[+] Thank you for using my script 😁")
        sleep(2)
        print(f"{YELLOW}[+] Hope you enjoyed it ! 👍")
        sleep(2)
        print(f"{YELLOW}[+] Until next time 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using my script 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)
    

if __name__ == '__main__':
    main()
