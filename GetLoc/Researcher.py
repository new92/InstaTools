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
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Please enable root access with the command: sudo su")
            sleep(2)
            print("[+] And execute again the script !")
            sleep(1)
            exit(0)
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

def info():
    author = 'new92'
    github = '@new92'
    name = 'Researcher'
    lang = 'en-US'
    language = 'Python'
    lns = 148
    stars = 1
    forks = 0
    url = 'https://github.com/new92/Instagram'
    print("[+] Author: "+str(author))
    print("[+] Github: "+str(github))
    print("[+] Script name: "+str(name))
    print("[+] Language: "+str(lang))
    print("[+] Programming name: "+str(language))
    print("[+] Lines of code: "+str(lns))
    print("[+] Github stars: "+str(stars))
    print("[+] Github forks: "+str(forks))
    print("[+] Url to repository: "+str(url))

def checkUser(user):
    return user == None or len(user) > 30

print("""
██████╗░███████╗░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗
██████╔╝█████╗░░╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝
██╔══██╗██╔══╝░░░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[+] Description: Python script for getting the possible location of the followers of a user.")
print("\n")
print("[1] Find location")
print("[2] Print script's info")
print("[4] Exit")
op=int(input("[::] Please enter the number of your option: "))
while op < 1 or op > 3 or op == None:
    print("[!] Invalid option !")
    sleep(1)
    op=int(input("[::] Please enter the number of your option: "))
if op == 1:
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
    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)
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
        f = open("users_in_"+str(loc)+".txt","w")
        name = 'users_in_'+str(loc)+".txt"
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
        print(f"[+] The usernames have been written in a text file named: {name}")
elif op == 2:
    info()
else:
    print("[+] Exiting...")
    quit(0)