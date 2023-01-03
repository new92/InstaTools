"""
Author: new92
Github: @new92

Python script for fetching the mutual followers between two accounts.
"""
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import instaloader
    import os
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
        else:
            system("sudo pip install -r requirements.txt")
            pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

def checkUser(user):
    return user == None or len(user) > 30

print("""
███╗░░░███╗██╗░░░██╗████████╗██╗░░░██╗░█████╗░██╗░░░░░░██████╗      ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
████╗░████║██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░██╔════╝      ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║░░░██║░░░██║░░░██║░░░██║███████║██║░░░░░╚█████╗░      █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║╚██╔╝██║██║░░░██║░░░██║░░░██║░░░██║██╔══██║██║░░░░░░╚═══██╗      ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░╚═╝░██║╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗██████╔╝      ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░      ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
""")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[+] This script finds the mutual followers between 2 accounts !")
print("\n")
print("[1] Find mutuals")
print("[2] Exit")
num=int(input("[::] Please enter the number of your choice: "))
while num < 1 or num > 2 or num == None:
    print("[!] Invalid number !")
    sleep(1)
    num=int(input("[::] Please enter again the number of your choice: "))
if num == 1:
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
    print("-"*45)
    try:
        loader.login(user,passw)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        quit(0)
    usernamef=str(input("[::] Please enter the first username: "))
    while checkUser(usernamef):
        print("[!] Invalid username !")
        sleep(1)
        usernamef=str(input("[::] Please enter again the first username: "))
    usernames=str(input("[::] Please enter the second username: "))
    while checkUser(usernames):
        print("[!] Invalid username !")
        sleep(1)
        usernames=str(input("[::] Please enter again the second username: "))
    FOLLOWERSF=[]
    FOLLOWERSS=[]
    profilef=instaloader.Profile.from_username(loader.context, usernamef)
    profiles=instaloader.Profile.from_username(loader.context, usernames)
    count = 0
    for follower in profilef.get_followers():
        FOLLOWERSF.append(follower.username)
        count += 1
    counter = 0
    allf = count
    for follower in profiles.get_followers():
        FOLLOWERSS.append(follower.username)
        counter += 1
    allf += counter
    if count > counter:
        mutual = 0
        MUTUALS = []
        x = len(FOLLOWERSF) - len(FOLLOWERSS)
        for i in range(len(FOLLOWERSS)+x):
            if FOLLOWERSF[i] in FOLLOWERSS:
                MUTUALS.append(FOLLOWERSF[i])
                mutual += 1
        per = (mutual / float(allf))*100
        print("[+] Number of mutual followers: "+str(mutual))
        print("[+] Percentage of mutual followers: "+str(per)+"%")
        print("[+] The usernames of the mutual followers: ")
        for k in range(len(MUTUALS)):
            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
    else:
        mutual = 0
        MUTUALS = []
        x = len(FOLLOWERSS) - len(FOLLOWERSF)
        for i in range(len(FOLLOWERSF)+x):
            if FOLLOWERSS[i] in FOLLOWERSF:
                MUTUALS.append(FOLLOWERSS[i])
                mutual += 1
        per = (mutual / float(allf))*100
        print("[+] Number of mutual followers: "+str(mutual))
        print("[+] Percentage of mutual followers: "+str(per)+"%")
        print("[+] The usernames of the mutual followers: ")
        for k in range(len(MUTUALS)):
            print(f"[+] Username No{k+1}: {MUTUALS[k]}")
    if len(MUTUALS) == 0:
        print("[!] No mutual followers found !")
        sleep(2)
        print("[+] Exiting")
        quit(0)
    else:
        f = open("mutuals.txt",'w')
        for i in range(len(MUTUALS)):
            f.write("[+] Username No"+str(i+1)+": "+str(MUTUALS[i]))
            f.write("\n")
        f.close()
        print("[+] Saved mutual followers to a text file named: mutuals.txt")
else:
    print("[+] Exiting...")
    quit(0)
