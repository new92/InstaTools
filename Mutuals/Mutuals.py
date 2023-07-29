# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

Python script for fetching the mutual followers and/or followees between two accounts.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! Mutuals requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use Mutuals ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 7
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import instaloader
    import os
    import requests
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Mutuals have been installed !")
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
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
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

print("[✓] Successfully loaded modules !")
sleep(1)

def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or username == ''

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'en-US'
    language = 'Python'
    name = 'Mutuals'
    api = None
    lines = 608
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
███╗░░░███╗██╗░░░██╗████████╗██╗░░░██╗░█████╗░██╗░░░░░░██████╗      ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
████╗░████║██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░██╔════╝      ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║░░░██║░░░██║░░░██║░░░██║███████║██║░░░░░╚█████╗░      █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║╚██╔╝██║██║░░░██║░░░██║░░░██║░░░██║██╔══██║██║░░░░░░╚═══██╗      ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░╚═╝░██║╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗██████╔╝      ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░      ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def nums():
    print("[1] Find mutuals")
    print("[2] Show Mutual's info")
    print("[3] Update Mutuals")
    print("[4] Uninstall Mutuals")
    print("[5] Exit")

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
    return '[✓] Files and dependencies uninstalled successfully !'

def main():
    print(banner())
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] With this script you can find the mutual followers/followings between 2 accounts on Instagram !")
    print("\n")
    nums()
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 5:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1/2/3/4/5]")
        sleep(1)
        nums()
        sleep(2)
        num=int(input("[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        user=str(input("[::] Please enter your username: "))
        while checkUser(user):
            if user == None or user == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid username !")
            sleep(1)
            user=str(input("[::] Please enter again your username: "))
        user = user.lower().strip()
        while valUser(user):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall Mutuals and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall Mutuals and Exit")
                sleep(1)
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input("[::] Please enter the username: "))
                while checkUser(user):
                    if user == None or user == '':
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
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
                print("[+] Thank you for using Mutuals 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(2)
                quit(0)
        psw=str(input("[::] Please enter your password: "))
        while psw == None or psw == '':
            print("[!] This field can't be blank !")
            sleep(1)
            psw=str(input("[::] Please enter again your password: "))
        print("|"+"-"*45+"|")
        try:
            loader.login(user,psw)
        except Exception as ex:
            print("[!] Login error !")
            sleep(1)
            print(f"[+] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            sleep(1)
            quit(0)
        print("[1] Find the mutual followers between 2 accounts")
        print("[2] Find the mutual followees between 2 accounts")
        t=int(input("[::] Please enter a number (from the above ones): "))
        while t < 1 or t > 2:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1/2]")
            sleep(1)
            print("[1] Find mutual followers")
            print("[2] Find mutual followees")
            t=int(input("[::] Please enter again a number (from the above ones): "))
        usernamef=str(input("[::] Please enter the first username: "))
        while checkUser(usernamef):
            if usernamef != None:
                print("[!] The length of the username must be 30 or lower !")
            else:
                print("[!] This field can't be blank !")
            sleep(1)
            usernamef=str(input("[::] Please enter again the first username: "))
        usernamef = usernamef.lower().strip()
        while valUser(usernamef):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall Mutuals and Exit")
            optf=int(input("[::] Please enter a number (from the above ones): "))
            while optf < 1 or optf > 4:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall Mutuals and Exit")
                sleep(1)
                optf=int(input("[::] Please enter again a number (from the above ones): "))
            if optf == 1:
                usernamef=str(input("[::] Please enter the username: "))
                while checkUser(usernamef):
                    if usernamef == None or usernamef == '':
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
                    sleep(1)
                    usernamef=str(input("[::] Please enter again the username: "))
            elif optf == 2:
                clear()
                main()
            elif optf == 3:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                clear()
                print(Uninstall())
                sleep(2)
                print("[+] Thank you for using Mutuals 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(2)
                quit(0)
        usernames=str(input("[::] Please enter the second username: "))
        while checkUser(usernames):
            print("[!] Invalid username !")
            sleep(1)
            usernames=str(input("[::] Please enter again the second username: "))
        usernames = usernames.lower().strip()
        while valUser(usernames):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall Mutuals and Exit")
            opts=int(input("[::] Please enter a number (from the above ones): "))
            while opts < 1 or opts > 4 or opts == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall Mutuals and Exit")
                sleep(1)
                opts=int(input("[::] Please enter again a number (from the above ones): "))
            if opts == 1:
                usernames=str(input("[::] Please enter the username: "))
                while checkUser(usernames):
                    if usernames != None:
                        print("[!] The length of the username must be 30 or lower")
                    else:
                        print("[!] This field can't be blank !")
                    sleep(1)
                    usernames=str(input("[::] Please enter again the username: "))
            elif opts == 2:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
        profilef=instaloader.Profile.from_username(loader.context, usernamef)
        profiles=instaloader.Profile.from_username(loader.context, usernames)
        ANS = ['yes','Yes','y','Y','yEs','YES','yES','YeS','YEs','yeS','no','No','n','N','nO']
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
                        print("[!] No mutual followers found !")
                        sleep(2)
                    else:
                        per = (len(MUTUALS) / float(allf))*100
                        print(f"[+] Number of mutual followers: {len(MUTUALS)}")
                        sleep(1)
                        print(f"[+] Percentage of mutual followers: {per}%")
                        sleep(1)
                        print("[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        sleep(3)
                        print("[+] Acceptable answers: [yes/no]")
                        sleep(1)
                        savem=str(input("[?] Save the mutual followers ? "))
                        while savem not in ANS or savem == None or savem == '':
                            if type(savem) == str:
                                print("[!] Invalid answer !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This field can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followers ? "))
                        if savem in ANS[:10]:
                            name = 'mutuals.txt'
                            f = open(name,'w')
                            for i in range(len(MUTUALS)):
                                f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            f.close()
                            print("[✓] Successfully saved the mutual followers to a text file named: mutuals.txt")
                            sleep(2)
                            print(f"[↪] Name: {name}")
                            print(f"[↪] Path: {fpath(name)}")
                            print(f"[↪] File size: {(os.stat(fpath(name))).st_size} bytes")
                            sleep(2)
                    clear()
                    x = len(FOLLOWERSS) - len(FOLLOWERSF)
                    MUTUALS = [FOLLOWERSS[i] for i in range(len(FOLLOWERSF)+x) if FOLLOWERSS[i] in FOLLOWERSF]
                    if len(MUTUALS) == 0:
                        print("[!] No mutual followers found !")
                        sleep(2)
                        print("[+] Exiting")
                        sleep(1)
                        print("[+] Thank you for using Mutuals 😁")
                        quit(0)
                    else:
                        per = len(MUTUALS) / float(allf)*100
                        print(f"[+] Number of mutual followers: {len(MUTUALS)}")
                        sleep(1)
                        print(f"[+] Percentage of mutual followers: {per}%")
                        sleep(1)
                        print("[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        sleep(3)
                        print("[+] Acceptable answers: [yes/no]")
                        sleep(1)
                        savem=str(input("[?]  Save the mutual followers ? "))
                        while savem not in ANS or savem == None or savem == '':
                            if type(savem) == str:
                                print("[!] Invalid answer !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This field can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followers ? "))
                        if savem in ANS[:10]:
                            name = 'mutuals.txt'
                            f = open(name,'w')
                            for i in range(len(MUTUALS)):
                                f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            f.close()
                            print("[✓] Successfully saved mutual followers to a text file named: mutuals.txt")
                            sleep(2)
                            print(f"[↪] Name: {name}")
                            print(f"[↪] Path: {fpath(name)}")
                            print(f"[↪] File size: {os.stat(fpath(name)).st_size} bytes")
                            sleep(1)
            else:
                print("[!] No mutual followers found !")
                sleep(1)
                if FOLLOWERSF == 0:
                    print(f"[+] Followers not found on account: {usernamef}")
                else:
                    print(f"[+] Followers not found on account: {usernames}")
                sleep(2)
                print("[+] Exiting...")
                sleep(1)
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
                        print("[!] No mutual followees found !")
                        sleep(2)
                        print("[+] Exiting")
                        sleep(1)
                        print("[+] Thank you for using Mutuals 😁")
                        quit(0)
                    else:
                        per = (len(MUTUALS) / float(allfe))*100
                        print(f"[+] Number of mutual followees: {len(MUTUALS)}")
                        sleep(1)
                        print(f"[+] Percentage of mutual followees: {per}%")
                        sleep(1)
                        print("[+] The usernames of the mutual followees: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        savem=str(input("[?] Save the mutual followees ? [yes/no] "))
                        while savem not in ANS or savem == None or savem == '':
                            if type(savem) == str:
                                print("[!] Invalid answer !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This input can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followees ? [yes/no] "))
                        if savem in ANS[:10]:
                            name = 'mutualsf.txt'
                            f = open(name,'w')
                            for i in range(len(MUTUALS)):
                                f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                            f.close()
                            print("[✓] Successfully saved mutual followees to a text file !")
                            sleep(2)
                            print(f"[↪] Name: {name}")
                            print(f"[↪] Path: {fpath(name)}")
                            print(f"[↪] File size: {os.stat(fpath(name)).st_size}")
                        sleep(1)
            else:
                print("[!] No followees found !")
                sleep(1)
                if FOLLOWEESF == 0:
                    print(f"[+] Followees not found on account: {usernamef}")
                else:
                    print(f"[+] Followees not found on account: {usernames}")
                sleep(2)
                print("[+] Exiting...")
                sleep(1)
                quit(0)
    elif num == 2:
        clear()
        ScriptInfo()

    elif num == 3:
        clear()
        system('git pull')
        sleep(1)
        print("[✓] Script updated successfully !")
        
    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for using Researcher 😁")
        sleep(2)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

    else:
        clear()
        print("[+] Thank you for using Mutuals 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

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
        print("[+] Exiting...")
        sleep(1)
        print("[+] See you next time 👋")
        sleep(2)
        quit(0)

if __name__ == '__main__':
    main()
