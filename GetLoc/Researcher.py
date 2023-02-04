"""
Author: new92
Github: @new92
Python script for retrieving the (possible) location of some followers of a user !
"""
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import os
    import instaloader
    import requests
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
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

def ScriptInfo():
    author = 'new92'
    license1 = 'MIT'
    lang = 'es-US'
    language = 'Python'
    name = 'Researcher'
    api = None
    lines = 0
    f = '/Instagram/GetLoc/Researcher.py'
    ptf = os.path.abspath(f)
    if os.path.exists(ptf):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 3
    forks = 1
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] License: "+str(license1))
    print("[+] Natural language: "+str(lang))
    print("[+] Programming language(s) used: "+str(language))
    print("[+] Number of lines: "+str(lines))
    print("[+] Program's name: "+str(name))
    print("[+] API(s) used: "+str(api))
    print("[+] File size: "+str(fsize)+" bytes")
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))

def checkUser(user):
    return user == None or len(user) > 30

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
    dir = os.path.abspath('Instagram')
    rmdir(dir)
    return "[+] Files and dependencies uninstalled successfully !"

def banner():
    return """
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
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] Description: Python script for getting the possible location of the followers of a user.")
    print("\n")
    print("[1] Find location")
    print("[2] Print script's info and exit")
    print("[3] Uninstall script")
    print("[4] Exit")
    op=int(input("[::] Please enter a number (from the above ones): "))
    while op < 1 or op > 4 or op == None:
        print("[!] Invalid number !")
        sleep(1)
        op=int(input("[::] Please enter a number (from the above ones): "))
    if op == 1:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print("[+] NOTE: The following username will be used to get the possible location of their followers.")
        sleep(4)
        username=str(input("[::] Please enter the username: "))
        while checkUser(username):
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        loc=str(input("[::] Please enter the location: "))
        while loc == None:
            print("[!] Invalid location !")
            sleep(1)
            loc=str(input("[::] Please enter again the location: "))
        loc = loc.capitalize()
        loader = instaloader.Instaloader()
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        user=str(input("[::] Please enter your username: "))
        while checkUser(user):
            print("[!] Invalid username !")
            sleep(1)
            user=str(input("[::] Please enter again your username: "))
        passw=input("[::] Please enter your password: ")
        while passw == None:
            print("[!] You must enter a password !")
            sleep(1)
            passw=input("[::] Please enter again your password: ")
        print("|"+"-"*45+"|")
        try:
            loader.login(user,passw)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)
        profile = instaloader.Profile.from_username(loader.context, username)
        followers = [follower.username for follower in profile.get_followers()]
        LIST = []
        for i in range(len(followers)):
            profile = instaloader.Profile.from_username(loader.context, followers[i])
            if loc in profile.biography:
                LIST.append(followers[i])
        if len(LIST) == 0:
            print("[!] No users with such location found on the followers of the prementioned user.")
            sleep(3)
            print("[+] Exiting...")
            quit(0)
        else:
            per = (float(len(followers)) / len(LIST)) * 100
            name = 'users_in_'+str(loc)+".txt"
            f = open(name,"w")
            print("[+] Location: "+loc.capitalize())
            print("[+] Searched in user's: "+username+" followers")
            print("[+] "+str(len(LIST))+" users in location: "+loc.capitalize())
            print("[+] Percentage of users with this location: "+str(per)+"%")
            print("|"+"-"*20+"users".upper()+"-"*20+"|")
            for i in range(len(LIST)):
                print("[=] Username: "+str(LIST[i]))
                f.write("[=] Username: "+str(LIST[i]))
                f.write("\n")
            f.close()
            print(f"[+] The usernames have been saved in a text file named: {name}")
    elif op == 2:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        ScriptInfo()
    elif op == 3:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print(Uninstall())
        print("[+] Thank you for using my script 😁")
        sleep(2)
        exit(0)
    else:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        exit(0)

if __name__ == '__main__':
    main()
