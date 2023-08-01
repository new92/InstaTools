# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

Script in which the user enters a username and the script returns if the user with the specific username follows verified users.
If yes then:
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
    total_mods = 7
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import os
    from os import system
    import instaloader
    import requests
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
                while opt < 1 or opt > 2 or opt == None:
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

print("[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    author = 'new92'
    lice = 'MIT'
    name = 'IsVer'
    lang = 'en-US'
    language = 'Python'
    api = None
    lines = 432
    f = name+'.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    stars = 33
    forks = 7
    issues = 0
    issuescl = 0
    prs = 0
    prscl = 1
    discs = 1
    print(f"[+] Author: {author}")
    print(f"[+] Github: @{author}")
    print(f"[+] License: {lice}")
    print(f"[+] Natural language: {lang}")
    print(f"[+] Programming language(s) used: {language}")
    print(f"[+] Number of lines: {lines} lines")
    print(f"[+] Script's name: {name}")
    print(f"[+] API(s) used: {api}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] Path: {fpath(f)}")
    print("|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars: {stars}")
    print(f"[+] Forks: {forks}")
    print(f"[+] Open issues: {issues}")
    print(f"[+] Closed issues: {issuescl}")
    print(f"[+] Open pull requests: {prs}")
    print(f"[+] Closed pull requests: {prscl}")
    print(f"[+] Discussions: {discs}")
    
def banner() -> str:
    return """
██╗░██████╗██╗░░░██╗███████╗██████╗░
██║██╔════╝██║░░░██║██╔════╝██╔══██╗
██║╚█████╗░╚██╗░██╔╝█████╗░░██████╔╝
██║░╚═══██╗░╚████╔╝░██╔══╝░░██╔══██╗
██║██████╔╝░░╚██╔╝░░███████╗██║░░██║
╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝"""

def clear():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or username == ''

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
    return "[✓] Files and dependencies uninstalled successfully !"

def main():
    print(banner())
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] With IsVer you can see if a user follows verified accounts and if yes which and how many (on Instagram)")
    print("\n")
    print("[1] Initiate IsVer")
    print("[2] Show IsVer's info")
    print("[3] Uninstall IsVer")
    print("[4] Exit")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4:
        print("[!] Invalid number !")
        sleep(1)
        print("[1] Initiate IsVer")
        print("[2] Show IsVer's info")
        print("[3] Uninstall IsVer")
        print("[4] Exit")
        sleep(3)
        num=int(input("[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        user=str(input("[::] Please enter your username: "))
        while checkUser(user):
            if user == None or user == '':
                print("[!] This input can't be blank !")
            else:
                print("[!] Invalid length ! Acceptable length: <= 30 characters")
            sleep(1)
            print("[!] Invalid username !")
            sleep(1)
            user=str(input("[::] Please enter again your username: "))
        user = user.lower().strip()
        while ValUser(user):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall IsVer and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall IsVer and Exit")
                sleep(1)
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input("[::] Please enter the username: "))
                while checkUser(user):
                    if user == None or user == '':
                        print("[!] This input can't be blank !")
                    else:
                        print("[!] Invalid length ! Acceptable length: <= 30 characters")
                    sleep(1)
                    user=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print("[+] Thank you for using IsVer 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(2)
                quit(0)
        psw=str(input("[::] Please enter your password: "))
        while psw == None or psw == '':
            print("[!] This input can't be blank !")
            sleep(1)
            psw=str(input("[::] Please enter again your password: "))
        print("|"+"-"*45+"|")
        try:
            loader.login(user,psw)
        except Exception as ex:
            print("[!] Login error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            sleep(1)
            quit(0)
        username=str(input("[::] Please enter the username of the user: "))
        while checkUser(username):
            if username == None or username == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid username !")
            username=str(input("[::] Please enter again the username of the user: "))
        while ValUser(username):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall and Exit")
                sleep(1)
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    if username == None or username == '':
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print("[+] Thank you for using IsVer 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! 🙂")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(2)
                quit(0)
        profile=instaloader.Profile.from_username(loader.context, username)
        FOLLOWINGS = [following.username for following in profile.get_followees()]
        VERS = []
        for i in range(len(FOLLOWINGS)):
            ver_profile = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
            if ver_profile.is_verified:
                VERS.append(FOLLOWINGS[i])
        followees = profile.followees
        print(f"[+] Is {username} following verified accounts ? {len(VERS) == 0}")
        if len(VERS) == 0:
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[::] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                num=int(input("[::] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] Thank you for using IsVer 😁")
                quit(0)
        else:
            print(f"[+] {username.capitalize()} follows {len(VERS)} verified accounts")
            sleep(2)
            print("[+] Accounts:")
            print("\n")
            print("-"*10)
            print("\n")
            for i in range(len(VERS)):
                print(f"[+] Username: {VERS[i]}")
                print(f"[+] Followers: {VERS[i].followers}")
                print(f"[+] Followings: {VERS[i].followees}")
                sleep(2)
            print(f"[+] Percentage of verified accounts followed by user {username} ==> {float(len(VERS)) / len(FOLLOWINGS)*100}%")
            sleep(2)
            print(f"[+] Verified followings: {len(VERS)}/{followees}")
    elif num == 2:
        clear()
        ScriptInfo()
        print("\n\n")
        print("[1] Return to menu")
        print("[2] Exit")
        number=int(input("[::] Please enter a number (from the above ones): "))
        while number < 1 or number > 2 or number == None:
            if number == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid number !")
            number=int(input("[::] Please enter again a number (from the above ones): "))
        if number == 1:
            clear()
            main()
        else:
            clear()
            print("[+] Exiting...")
            sleep(1)
            print("[+] See you next time 👋")
            sleep(2)
            quit(0)
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for using IsVer 😁")
        sleep(2)
        print("[+] Hope you enjoyed it ! 🙂")
        sleep(2)
        print("[+] Until next time 👋")
        sleep(2)
        quit(0)
    else:
        clear()
        print("[+] Thank you for using IsVer 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
