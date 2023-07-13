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
        print("[!] Error ! This script requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        print("[+] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    import instaloader
    import os
    import requests
except ImportError:
    print("[!] WARNING: Not all packages used in this script are installed !")
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
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

def checkUser(user:str) -> bool:
    return user == None or len(user) > 30 or type(user) != str

def ScriptInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'en-US'
    language = 'Python'
    name = 'Mutuals'
    api = None
    lines = 663
    f = name+'.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 25
    forks = 6
    issues = 0
    issuescl = 1
    prs = 0
    prscl = 1
    discs = 1
    print(f"[+] Author: {author}")
    print(f"[+] Github: @{author}")
    print(f"[+] License: {lice}")
    print(f"[+] Natural language: {lang}")
    print(f"[+] Programming language(s) used: {language}")
    print(f"[+] Number of lines: {lines} lines")
    print(f"[+] Program's name: {name}")
    print(f"[+] API(s) used: {api}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] Path: {os.path.abspath(f)}")
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

def nums():
    print("[1] Find mutuals")
    print("[2] Show script's info and exit")
    print("[3] Uninstall script")
    print("[4] Exit")

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
    return "[✓] Files and dependencies uninstalled successfully !"

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
    while num < 1 or num > 4 or num == None or type(num) != int:
        if type(num) == int:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1,2,3,4]")
        else:
            print("[!] This input can't be blank !")
            sleep(1)
        nums()
        sleep(1)
        num=int(input("[::] Please enter again a number (from the above ones): "))
    if num == 1:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        loader = instaloader.Instaloader()
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        user=str(input("[::] Please enter your username: "))
        while checkUser(user):
            print("[!] Invalid username !")
            sleep(1)
            user=str(input("[::] Please enter again your username: "))
        user = user.lower().strip()
        resp = requests.get(f"https://www.instagram.com/{user}/")
        while resp.status_code == 404 or resp.status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            print("[4] Uninstall and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4 or opt == None or type(opt) != int:
                if type(opt) == int:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2,3,4]")
                else:
                    print("[!] This input can't be blank !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                print("[4] Uninstall and Exit")
                sleep(1)
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=str(input("[::] Please enter the username: "))
                while checkUser(user):
                    if user == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
                    sleep(1)
                    user=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                if platform.system() == 'Windows':
                    system("cls")
                else:
                    system("clear")
                main()
            elif opt == 3:
                if platform.system() == 'Windows':
                    system("cls")
                else:
                    system("clear")
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                if platform.system() == 'Windows':
                    system("cls")
                else:
                    system("clear")
                print(Uninstall())
                sleep(1)
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(2)
                quit(0)
        psw=str(input("[::] Please enter your password: "))
        while psw == None or type(psw) != str:
            if psw == None:
                print("[!] This input can't be blank !")
            else:
                print("[!] You must enter an integer !")
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
        while t < 1 or t > 2 or t == None or type(t) != int:
            if t == None:
                print("[!] This field can't be blank !")
            elif type(t) != int and t != None:
                print("[!] Number must be an integer !")
            else:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1,2]")
            sleep(1)
            print("[1] Find mutual followers")
            print("[2] Find mutual followees")
            t=int(input("[::] Please enter again a number (from the above ones): "))
        usernamef=str(input("[::] Please enter the first username: "))
        while checkUser(usernamef):
            if usernamef != None:
                print("[!] The length of the username must be 30 or lower !")
            else:
                print("[!] This input can't be blank !")
            sleep(1)
            usernamef=str(input("[::] Please enter again the first username: "))
        usernamef = usernamef.lower().strip()
        resp = requests.get(f"https://www.instagram.com/{usernamef}/")
        while resp.status_code == 404 or resp.status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            optf=int(input("[::] Please enter a number (from the above ones): "))
            while optf < 1 or optf > 3 or optf == None:
                if type(optf) == int:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2,3]")
                else:
                    print("[!] This input can't be blank !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                sleep(1)
                optf=int(input("[::] Please enter again a number (from the above ones): "))
            if optf == 1:
                usernamef=str(input("[::] Please enter the username: "))
                while checkUser(usernamef):
                    if usernamef == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
                    sleep(1)
                    usernamef=str(input("[::] Please enter again the username: "))
            elif optf == 2:
                main()
            else:
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
        usernames=str(input("[::] Please enter the second username: "))
        while checkUser(usernames):
            print("[!] Invalid username !")
            sleep(1)
            usernames=str(input("[::] Please enter again the second username: "))
        usernames = usernames.lower().strip()
        resp = requests.get(f"https://www.instagram.com/{usernames}/")
        while resp.status_code == 404 or resp.status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            opts=int(input("[::] Please enter a number (from the above ones): "))
            while opts < 1 or opts > 3 or opts == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                sleep(1)
                opts=int(input("[::] Please enter again a number (from the above ones): "))
            if opts == 1:
                usernames=str(input("[::] Please enter the username: "))
                while checkUser(usernames):
                    if usernames != None:
                        print("[!] The length of the username must be 30 or lower")
                    else:
                        print("[!] This input can't be blank !")
                    sleep(1)
                    usernames=str(input("[::] Please enter again the username: "))
            elif opts == 2:
                main()
            else:
                print("[+] Exiting...")
                sleep(1)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
        profilef=instaloader.Profile.from_username(loader.context, usernamef)
        profiles=instaloader.Profile.from_username(loader.context, usernames)
        ANS=['yes','Yes','y','Y','yEs','YES','yES','YeS','YEs','yeS','no','No','n','N','nO']
        if t == 1:
            if platform.system() == 'Windows':
                system("cls")
            else:
                system("clear")
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
                        print("[1] Return to menu")
                        print("[2] Exit")
                        n=int(input("[::] Please enter a number (from the above ones): "))
                        while n < 1 or n > 2 or n == None:
                            if type(n) == int:
                                print("[!] Invalid number !")
                            else:
                                print("[!] This input can't be blank")
                            sleep(1)
                            print("[1] Return to menu")
                            print("[2] Exit")
                            n=int(input("[::] Please enter again a number (from the above ones): "))
                        if n == 1:
                            if platform.system() == 'Windows':
                                system("cls")
                            else:
                                system("clear")
                            main()
                        else:
                            if platform.system() == 'Windows':
                                system("cls")
                            else:
                                system("clear")
                            print("[+] Exiting...")
                            sleep(1)
                            print("[+] Thank you for using my script 😁")
                            sleep(2)
                            print("[+] Until next time 👋")
                            sleep(1)
                            quit(0)
                    else:
                        per = (len(MUTUALS) / float(allf))*100
                        print("[+] Number of mutual followers: "+str(len(MUTUALS)))
                        sleep(0.5)
                        print("[+] Percentage of mutual followers: "+str(per)+"%")
                        sleep(0.5)
                        print("[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        savem=str(input("[?] Save the mutual followers ? [yes/no] "))
                        while savem not in ANS or savem == None:
                            if type(savem) == str:
                                print("[!] Invalid answer !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This input can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followers ? [yes/no] "))
                        if savem in ANS[:10]:
                            f = open("mutuals.txt",'w')
                            for i in range(len(MUTUALS)):
                                f.write("[+] Username No"+str(i+1)+": "+str(MUTUALS[i])+"\n")
                            f.close()
                            print("[+] Successfully saved the mutual followers to a text file named: mutuals.txt")
                            sleep(2)
                            print("[+] Path: "+os.path.abspath("mutuals.txt"))
                        else:
                            print("<ok>")
                            sleep(1)
                            print("[1] Return to menu")
                            print("[2] Exit")
                            op=int(input("[::] Please enter a number (from the above ones): "))
                            while op < 1 or op > 2 or op == None:
                                if type(op) == int:
                                    print("[!] Invalid number !")
                                    sleep(1)
                                    print("[+] Acceptable numbers: [1,2]")
                                else:
                                    print("[!] This input can't be blank !")
                                sleep(1)
                                print("[1] Return to menu")
                                print("[2] Exit")
                                op=int(input("[::] Please enter again a number (from the above ones): "))
                            if op == 1:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                main()
                            else:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                print("[+] Exiting...")
                                sleep(1)
                                print("[+] Thank you for using my script 😁")
                                sleep(2)
                                print("[+] Until next time 👋")
                                sleep(1)
                                quit(0)
                else:
                    if platform.system() == 'Windows':
                        system("cls")
                    else:
                        system("clear")
                    x = len(FOLLOWERSS) - len(FOLLOWERSF)
                    MUTUALS = [FOLLOWERSS[i] for i in range(len(FOLLOWERSF)+x) if FOLLOWERSS[i] in FOLLOWERSF]
                    if len(MUTUALS) == 0:
                        print("[!] No mutual followers found !")
                        sleep(2)
                        print("[+] Exiting")
                        sleep(1)
                        print("[+] Thank you for using my script 😁")
                        quit(0)
                    else:
                        per = (len(MUTUALS) / float(allf))*100
                        print("[+] Number of mutual followers: "+str(len(MUTUALS)))
                        sleep(1)
                        print("[+] Percentage of mutual followers: "+str(per)+"%")
                        sleep(1)
                        print("[+] The usernames of the mutual followers: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        savem=str(input("[?]  Save the mutual followers ? [yes/no] "))
                        while savem not in ANS or savem == None:
                            if type(savem) == str:
                                print("[!] Invalid input !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This input can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followers ? [yes/no] "))
                        if savem in ANS[:10]:
                            f = open("mutuals.txt",'w')
                            for i in range(len(MUTUALS)):
                                f.write("[+] Username No"+str(i+1)+": "+str(MUTUALS[i])+"\n")
                            f.close()
                            print("[+] Saved mutual followers to a text file named: mutuals.txt")
                            sleep(2)
                            print("[+] Path: "+os.path.abspath("mutuals.txt"))
                        else:
                            print("<ok>")
                            sleep(1)
                            print("[1] Return to menu")
                            print("[2] Exit")
                            num=int(input("[::] Please enter a number (from the above ones): "))
                            while num < 1 or num > 2 or num == None:
                                if num != None:
                                    print("[!] Invalid number !")
                                    sleep(1)
                                    print("[+] Acceptable numbers: 1, 2")
                                elif num == None:
                                    print("[!] This input can't be blank !")
                                    sleep(1)
                                print("[1] Return to menu")
                                print("[2] Exit")
                                sleep(1)
                                num=int(input("[::] Please enter again a number (from the above ones): "))
                            if num == 1:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                main()
                            else:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                print("[+] Exiting...")
                                sleep(1)
                                print("[+] Thank you for using my script 😁")
                                sleep(2)
                                print("[+] Until next time 👋")
                                sleep(1)
                                quit(0)
            else:
                print("[!] No followers found !")
                sleep(1)
                if FOLLOWERSF == 0:
                    print("[+] Followers not found on account: "+str(usernamef))
                else:
                    print("[+] Followers not found on account: "+str(usernames))
                sleep(2)
                print("[+] Exiting...")
                sleep(1)
                quit(0)
        else:
            if platform.system() == 'Windows':
                system("cls")
            else:
                system("clear")
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
                        print("[+] Thank you for using my script 😁")
                        quit(0)
                    else:
                        per = (len(MUTUALS) / float(allfe))*100
                        print("[+] Number of mutual followees: "+str(len(MUTUALS)))
                        sleep(1)
                        print("[+] Percentage of mutual followees: "+str(per)+"%")
                        sleep(1)
                        print("[+] The usernames of the mutual followees: ")
                        for k in range(len(MUTUALS)):
                            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
                        savem=str(input("[?] Save the mutual followees ? [yes/no] "))
                        while savem not in ANS or savem == None:
                            if type(savem) == str:
                                print("[!] Invalid answer !")
                                sleep(1)
                                print("[+] Acceptable answers: [yes/no]")
                            else:
                                print("[!] This input can't be blank !")
                            sleep(1)
                            savem=str(input("[?] Save the mutual followees ? [yes/no] "))
                        if savem in ANS[:10]:
                            f = open("mutualsf.txt",'w')
                            for i in range(len(MUTUALS)):
                                f.write("[+] Username No"+str(i+1)+": "+str(MUTUALS[i])+"\n")
                            f.close()
                            print("[+] Saved mutual followees to a text file named: mutualsf.txt")
                        else:
                            print("<ok>")
                            sleep(1)
                            print("[1] Return to menu")
                            print("[2] Exit")
                            op=int(input("[::] Please enter a number (from the above ones): "))
                            while op < 1 or op > 2 or op == None:
                                if type(op) == int:
                                    print("[!] Invalid number !")
                                    sleep(1)
                                    print("[+] Acceptable numbers: [1,2]")
                                else:
                                    print("[!] This input can't be blank !")
                                sleep(1)
                                print("[1] Return to menu")
                                print("[2] Exit")
                                op=int(input("[::] Please enter again a number (from the above ones): "))
                            if op == 1:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                main()
                            else:
                                if platform.system() == 'Windows':
                                    system("cls")
                                else:
                                    system("clear")
                                print("[+] Exiting...")
                                sleep(1)
                                print("[+] Thank you for using my script 😁")
                                sleep(2)
                                print("[+] Until next time 👋")
                                sleep(1)
                                quit(0)
            else:
                print("[!] No followees found !")
                sleep(1)
                if FOLLOWEESF == 0:
                    print("[+] Followees not found on account: "+usernamef)
                else:
                    print("[+] Followees not found on account: "+usernames)
                sleep(2)
                print("[+] Exiting...")
                sleep(1)
                quit(0)
    elif num == 2:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        ScriptInfo()
    elif num == 3:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print(Uninstall())
        sleep(1)
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] Hope you enjoyed it ! ☺️")
        sleep(2)
        print("[+] Until next time 👋")
        sleep(2)
        quit(0)
    else:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
