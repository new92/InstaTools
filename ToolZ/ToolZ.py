"""
Author: new92
Github: @new92

Keeps track on the users which unfollowed you.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! ToolZ requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use ToolZ ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 9
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
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in ToolZ have been installed !")
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
                print("[1] Uninstall ToolZ")
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
                    print("[1] Uninstall ToolZ")
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

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def checkUser(username: str) -> bool:
    return len(username) > 30 or username == None or username == ''

def valUser(username: str) -> bool:
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
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    print(f"[+] Author: {conf['author']}")
    print(f"[+] Github: @{conf['author']}")
    print(f"[+] License: {conf['lice']}")
    print(f"[+] Natural language: {conf['lang']}")
    print(f"[+] Programming language(s) used: {conf['language']}")
    print(f"[+] Number of lines: {conf['lines']}")
    print(f"[+] Script's name: {conf['name']}")
    print(f"[+] API(s) used: {conf['api']}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] File path: {fpath(f)}")
    print(f"|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars: {conf['stars']}")
    print(f"[+] Forks: {conf['forks']}")
    print(f"[+] Open issues: {conf['issues']}")
    print(f"[+] Closed issues: {conf['clissues']}")
    print(f"[+] Open pull requests: {conf['prs']}")
    print(f"[+] Closed pull requests: {conf['clprs']}")
    print(f"[+] Discussions: {conf['discs']}")

def logo() -> str:
    return f"""{YELLOW}
         tttt                                            lllllll
      ttt:::t                                            l:::::l
      t:::::t                                            l:::::l
      t:::::t                                            l:::::l
ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l zzzzzzzzzzzzzzzzz
t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l z:::::::::::::::z
t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l z::::::::::::::z 
tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l zzzzzzzz::::::z  
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l       z::::::z   
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l      z::::::z    
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l     z::::::z     
      t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l    z::::::z      
      t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::l  z::::::zzzzzzzz
      tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::l z::::::::::::::z
        tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::lz:::::::::::::::z
          ttttttttttt     ooooooooooo      ooooooooooo   llllllllzzzzzzzzzzzzzzzzz
    """


def main():
    print(logo())
    print("\n")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print("\n")
    print(f"{YELLOW}[+] ToolZ: Python tool which keeps track on who unfollowed you.")
    print("\n")
    print(f"{YELLOW}[1] Start ToolZ")
    print(f"{YELLOW}[2] Display ToolZ's info")
    print(f"{YELLOW}[3] Clear log file")
    print(f"{YELLOW}[4] Uninstall ToolZ")
    print(f"{YELLOW}[5] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 5 or num == None:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{YELLOW}[1] Start ToolZ")
        print(f"{YELLOW}[2] Display ToolZ's info")
        print(f"{YELLOW}[3] Clear log file")
        print(f"{YELLOW}[4] Uninstall ToolZ")
        print(f"{YELLOW}[5] Exit")
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
                    print(f"{YELLOW}[+] Thank you for using ToolZ 😁")
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
        print(f'{GREEN}|-----------------------------------|')
        try:
            loader.login(username,password)
        except Exception as ex:
            print(f"{RED}[!] Login Error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        print(f"{GREEN}[✓] Login successfull !")
        sleep(1)
        print(f"{GREEN}[*] Initiating ToolZ...")
        sleep(2)
        print(f"{YELLOW}[*] Acceptable answers: [True/False]")
        sleep(1)
        kp=bool(input("[?] Keep log ? "))
        while kp == None:
            print(f"{RED}[!] Invalid answer !")
            sleep(1)
            kp=bool(input(f"{YELLOW}[?] Keep log ? "))
        op = False
        if kp:
            op = True
            f = open('log.txt','w')
        profile = instaloader.Profile.from_username(loader.context, username)
        FOLLOWERS = [follower.username for follower in profile.get_followers()]
        FOLLOWINGS = [following.username for following in profile.get_followees()]
        print("[1] Live unfollowers tracker")
        print("[2] One-time unfollowers tracker")
        opt=int(input("[::] Please enter a number (from the above ones): "))
        while opt < 1 or opt > 2 or opt == None:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1/2]")
            sleep(1)
            opt=int(input("[::] Please enter a number (from the above ones): "))
        if opt == 1:
            UNFOLLOWERS = []
            while len(FOLLOWERS) == len(FOLLOWINGS):
                print("[*] Checking for unfollowers...")
                sleep(5)
                profile = instaloader.Profile.from_username(loader.context, username)
                FOLLOWERS = [follower.username for follower in profile.get_followers()]
                FOLLOWINGS = [following.username for following in profile.get_followees()]
                print("[+] No unfollowers found...")
                sleep(5)
                print("[*] Sleeping for 20 secs...")
                sleep(20)
            for i in range(len(FOLLOWINGS)):
                verProf = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
                if FOLLOWINGS[i] not in FOLLOWERS and not verProf.is_verified:
                    UNFOLLOWERS.append(FOLLOWINGS[i])
            if op:
                f.write(f"[&] Detected a total of {len(UNFOLLOWERS)} unfollowers\n\n")
                print("-"*25+'\n\n')
                for i in range(len(UNFOLLOWERS)):
                    f.write(f"[>] Username >>> {UNFOLLOWERS[i]}\n")
                print(f"{GREEN}[✓] Successfully saved log !")
                sleep(2)
                print(f"{YELLOW}[↪] Log file name: log.txt")
                print(f"{YELLOW}[↪] Location path: {fpath('log.txt')}")
                print(f"{YELLOW}[↪] File size: {os.stat(fpath('log.txt')).st_size} bytes")
                sleep(3)
            sleep(5)
            print(f"[+] Found {len(UNFOLLOWERS)} unfollowers.")
            sleep(2)
            for i in range(len(UNFOLLOWERS)):
                print(f"[>] Username >>> {UNFOLLOWERS[i]}")
        else:
            if len(FOLLOWERS) == len(FOLLOWINGS):
                print(f"{YELLOW}[+] No unfollowers found !")
            else:
                L = []
                for i in range(len(FOLLOWINGS)):
                    verProf = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
                    if FOLLOWINGS[i] not in FOLLOWERS and not verProf.is_verified:
                        L.append(FOLLOWINGS[i])
                print(f"{YELLOW}[✓] OK")
                sleep(2)
                print(f"{YELLOW}[+] Found a total of: {len(L)} unfollowers")
                sleep(1)
                print(f"{YELLOW}[+] Usernames: ")
                print("\n")
                for i in range(len(L)):
                    print(f"{YELLOW}[>] Username{i+1} >>> {L[i]}")
                sleep(2)
                if op:
                    f.write(f"[&] Detected a total of {len(L)} unfollowers\n\n")
                    print("-"*25+'\n\n')
                    for i in range(len(L)):
                        f.write(f"[>] Username >>> {L[i]}\n")
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{YELLOW}[↪] Log file name: log.txt")
                    print(f"{YELLOW}[↪] Location path: {fpath('log.txt')}")
                    print(f"{YELLOW}[↪] File size: {os.stat(fpath('log.txt')).st_size} bytes")
                    sleep(3)
    elif num == 2:
        clear()
        ScriptInfo()
        print("\n\n")
        sleep(5)
    elif num == 3:
        clear()
        f = open('log.txt','w')
        f.close()
        print("[✓] Successfully cleared log file !")
        sleep(2)
    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{YELLOW}[+] Thank you for using ToolZ 😁")
        sleep(2)
        print(f"{YELLOW}[+] Hope you enjoyed it ! 👍")
        sleep(2)
        print(f"{YELLOW}[+] Until next time 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using ToolZ 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Back to menu")
    print(f"{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 2 or num == None:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{YELLOW}[+] Thank you for using ToolZ 😃")
        sleep(2)
        print(f"{YELLOW}[+] Until next time 🤗")
        sleep(1)
        print(f"{YELLOW}[+] Exiting...")
        quit(0)

if __name__ == '__main__':
    main()
