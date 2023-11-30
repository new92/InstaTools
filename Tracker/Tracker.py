# -*- coding: utf-8 -*-
"""
Author: new92
Contributors: [Itsfizziks, ProgramR4732]
Github: @new92
Leetcode: @new92
PyPI: @new92

Tracker is a Python script designed to monitor and maintain a record of a user's Instagram followers and followings. With Tracker, you can effortlessly keep tabs on changes in your Instagram network over time, making it a valuable tool for social media enthusiasts, influencers, and businesses looking to manage their online presence.
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
        quit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'rich', 'platform', 'os', 'csv', 'json', 'logging', 'requests', 'instaloader', 'colorama')
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import platform
    from os import system
    import os
    import csv
    import json
    import logging
    import instaloader
    import requests
    from colorama import init, Fore
except ImportError:
    print("[!] WARNING: Not all packages used in Tracker have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid():
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
                while opt not in range(1, 3):
                    if opt is None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers >>> [1,2]")
                    sleep(1)
                    print("[1] Uninstall Tracker")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))

                    def rmdir(dire):
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))

                            DIRS = (os.path.join(root, dir) for dir in dirs)
                        
                        for i in DIRS:
                            os.rmdir(i)
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit()
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
EMPTY = ('', ' ')

sleep(0.8)
console.clear()
console.log("[bold dark_green][✓] Successfully loaded modules.[/]")
sleep(0.8)
console.clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))

            DIRS = (os.path.join(root, dir) for dir in dirs)
        
        for i in DIRS:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

TABLE = (
    (
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ),
    (
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ),
    (
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ),
    (
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    )
)

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

ANS = ('yes', 'no')

def ScriptInfo():
    with open('Tracker/config.json') as config:
        conf = json.load(config)
    f = f"{conf['name']}.py"
    fp = fpath(f) is None
    fsize = os.stat(fpath(f)).st_size if fp else 0
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Contributors : {conf['contributors']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] PyPI: @{conf['author']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] Latest update: {conf['update']}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def banner() -> str:
    console.log("""[bold yellow]
    ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    [/]""")

def checkUser(username:str) -> bool:
    return username in EMPTY or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def validate(session: str) -> bool:
    return os.path.exists(session)

def extract(raw_path: str):
    index = raw_path.find('session-')
    return raw_path[index + len('session-'):] if index != -1 else None

def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Tracker is a python script which keeps track on the followers / followings of a user and informs the (Tracker's) user for changes.[/]")
    print("\n")
    console.print("[bold yellow][1] Start Tracker[/]")
    console.print("[bold yellow][2] Display Tracker's info[/]")
    console.print("[bold yellow][3] Uninstall Tracker[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num not in range(1, 5):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
        while con.lower() not in ANS:
            print(f"{RED}[!] Invalid answer !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
        if con.lower() == ANS[0]:
            logging.basicConfig(
                filename='cons.txt',
                level=logging.INFO,
                format='%(asctime)s [%(levelname)s]: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.')
        else:
            print(f"{YELLOW}[OK]")
            sleep(1)
            print(f"{YELLOW}[1] Exit")
            print(f"{YELLOW}[2] Uninstall ToolZ and exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            valErr = num in (1, 2)
            while not valErr:
                try:
                    print(f"{YELLOW}[1] Exit")
                    print(f"{YELLOW}[2] Uninstall ToolZ and exit")
                    sleep(1)
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                    valErr = num in (1, 2)
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers >>> [1/2]")
                    sleep(1)
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Thank you for using ToolZ 🫡")
                sleep(2)
                print(f"{YELLOW}[+] Until we meet again 👋")
                sleep(1)
                quit(0)
        sleep(2)
        clear()
        print(f'{GREEN}|---------------|LOGIN|---------------|')
        session=input(f"{YELLOW}[::] Cookie file path (<Enter> for default) >>> ")
        if not session:
            username=input(f"{YELLOW}[::] Please enter your username >>> ")
            while checkUser(username):
                if username in EMPTY:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid username !")
                username=input(f"{YELLOW}[::] Please enter your username >>> ")
            sleep(0.4)
            username = username.strip().lower()
            while valUser(username):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                print(f"{YELLOW}[4] Uninstall Tracker and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while opt not in range(1,5):
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
                    sleep(1)
                    opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if opt == 1:
                    username=str(input(f"{YELLOW}[::] Please enter your username >>> "))
                    while checkUser(username):
                        if username in EMPTY:
                            print(f"{RED}[!] This field can't be blank !")
                        else:
                            print(f"{RED}[!] Invalid username !")
                        sleep(1)
                        username=input(f"{YELLOW}[::] Please enter your username >>> ")
                elif opt == 2:
                    clear()
                    main()
                elif opt == 3:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Until next time 👋")
                    sleep(1)
                    quit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{GREEN}[+] Thank you for using Tracker 😁")
                    sleep(2)
                    print(f"{GREEN}[+] Until next time 👋")
                    sleep(2)
                    quit()
            loader.interactive_login(username=username)
        else:
            session = session.strip().lower()
            username = extract(session)
            sleep(0.5)
            print(f"{GREEN}[✓] Extracted username >>> {username}...")
            sleep(1)
            print(f"{GREEN}[+] Using session file >>> {session}...")
            sleep(2)
            try: 
                with open(session, 'rb') as sessionfile:
                    loader.context.load_session_from_file(username, sessionfile)
            except instaloader.exceptions.ConnectionException as ex:
                print(f"{RED}[✕] Error loading session file !")
                sleep(1)
                print(f"{YELLOW}[+] Error message >>> {ex}")
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                quit()
            print(f"{GREEN}[✓] Session loaded successfully !")
            sleep(1)
        print(f"{GREEN}[✓] Login successfull !")
        sleep(1.5)
        print(f'{YELLOW}[+] User ID >>> {profile.userid}')
        print(f'{YELLOW}[+] Full name >>> {profile.full_name}')
        sleep(1)
        print("[*] Initiating Tracker...")
        sleep(1)
        print(f"{YELLOW}[1] Track followers")
        print(f"{YELLOW}[2] Track followees")
        print(f"{YELLOW}[3] Track both")
        number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while number not in range(1,4):
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{YELLOW}[1] Track followers")
            print(f"{YELLOW}[2] Track followees")
            print(f"{YELLOW}[3] Track both")
            number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        user=input(f"{YELLOW}[::] Please enter the username of the target user: ")
        while checkUser(user):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            user=input(f"{YELLOW}[::] Please enter again the username of the target user: ")
        user = user.strip().lower()
        while valUser(user):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt not in range(1, 4):
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                user=input(f"{YELLOW}[::] Please enter the username: ")
                while checkUser(user):
                    print(f"{RED}[!] Invalid username !")
                    sleep(1)
                    user=input(f"{YELLOW}[::] Please enter again the username: ")
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using Tracker 😁")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit()
        name = 'trackerResults.txt'
        output = 'tracker.csv'
        if number == 1:
            profile = instaloader.Profile.from_username(loader.context, username)
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
            FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
            while FOLLOWERS == FOLLOWERSAF:
                print(f"{YELLOW}[+] No new additions found on >>> {user}")
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
                            print(f"{YELLOW}[⇒] Username >>> {follower}")
                else:
                    print(f"{GREEN}[*] {user} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for follower in FOLLOWERSAF:
                        if follower not in FOLLOWERS:
                            print(f"{YELLOW}[⇒] Username >>> {follower}")
                sleep(4)
            else:
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    print(f"{GREEN}[*] {user} removed 1 follower.")
                    sleep(1)
                    print(f"{YELLOW}[+] Username >>> {[follower for follower in FOLLOWERS if follower not in FOLLOWERSAF][0]}")
                else:
                    print(f"{GREEN}[*] {user} added 1 follower.")
                    sleep(2)
                    print(f"{YELLOW}[+] Username >>> {[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}")
            sleep(2)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            kp=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
            while kp.lower() not in ANS:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                kp=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
            kp = kp.lower() == ANS[0]
            if kp:
                ADD, REM = []
                with open(name, 'w', encoding='utf8') as f:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        for i in FOLLOWERS:
                            if i not in FOLLOWERSAF:
                                f.write(f'{i+1}) {i}\n')
                                REM.append(i)
                    else:
                        for i in FOLLOWERSAF:
                            if i not in FOLLOWERS:
                                f.write(f'{i+1}) {i}\n')
                                ADD.append(i)
                L = [
                    ['Followers removed', 'Followers added'],
                ]
                ADD.extend([''] * (len(REM) - len(ADD))) if len(REM) > len(ADD) else REM.extend([''] * len(ADD) - len(REM))
                for i in range(len(ADD)):
                    L.append([REM[i], ADD[i]])
                with open(output, mode='w', encoding='utf8') as file:
                    writer = csv.writer(file)
                    writer.writerows(L)
                print(f"{GREEN}[✓] Successfully saved log / CSV.")
                sleep(1.3)
                print(f"{YELLOW}[↪] Log file name >>> {name}")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file name >>> {output}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {fpath(name)}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {fpath(output)}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(fpath(name)).st_size} bytes")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(fpath(name)).st_size} bytes")
                sleep(2)
        elif number == 2:
            profile = instaloader.Profile.from_username(loader.context, username)
            FOLLOWEES = [followee.username for followee in profile.get_followees()]
            FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
            while FOLLOWEES == FOLLOWEESAF:
                print(f"{YELLOW}[+] No new additions found on >>> {user}")
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
                            print(f"{YELLOW}[⇒] Username >>> {followee}")
                else:
                    print(f"{GREEN}[*] {user} started following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for followee in FOLLOWEESAF:
                        if followee not in FOLLOWEES:
                            print(f"{YELLOW}[⇒] Username >>> {followee}")
                sleep(4)
            else:
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    print(f"{GREEN}[*] {user} stopped following 1 user.")
                    sleep(1)
                    print(f"{YELLOW}[+] Username >>> {[followee for followee in FOLLOWEES if followee not in FOLLOWEESAF][0]}")
                else:
                    print(f"{GREEN}[*] {user} started following 1 user.")
                    sleep(2)
                    print(f"{YELLOW}[+] Username >>> {[followee for followee in FOLLOWEESAF if followee not in FOLLOWEES][0]}")
            sleep(2)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            kp=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
            while kp.lower() not in ANS:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                kp=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
            kp = kp.lower() == ANS[0]
            if kp:
                ADD, REM = []
                with open(name, 'w', encoding='utf8') as f:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        for i in FOLLOWEES:
                            if i not in FOLLOWEESAF:
                                f.write(f'{i+1}) {i}\n')
                                REM.append(i)
                    else:
                        for i in FOLLOWEESAF:
                            if i not in FOLLOWEES:
                                f.write(f'{i+1}) {i}\n')
                                ADD.append(i)
                    L = [
                        ['Following removed', 'Followings added']
                    ]
                    ADD.extend([''] * (len(REM) - len(ADD))) if len(REM) > len(ADD) else REM.extend([''] * len(ADD) - len(REM))
                    for i in range(len(ADD)):
                        L.append([REM[i], ADD[i]])
                    with open(output, mode='w', encoding='utf8') as file:
                        writer = csv.writer(file)
                        writer.writerows(L)
                print(f"{GREEN}[✓] Successfully saved log / CSV.")
                sleep(1.3)
                print(f"{YELLOW}[↪] Log file name >>> {name}")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file name >>> {output}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {fpath(name)}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {fpath(output)}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(fpath(name)).st_size} bytes")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(fpath(name)).st_size} bytes")
                sleep(2)
        else:
            profile = instaloader.Profile.from_username(loader.context, username)
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
                                print(f"{YELLOW}[⇒] Username >>> {follower}")
                    else:
                        print(f"{GREEN}[*] {user} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for follower in FOLLOWERSAF:
                            if follower not in FOLLOWERS:
                                print(f"{YELLOW}[⇒] Username >>> {follower}")
                    sleep(4)
                else:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        print(f"{GREEN}[*] {user} removed 1 follower.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username >>> {[usr for usr in FOLLOWERS if usr not in FOLLOWERSAF][0]}")
                        sleep(1)
                    else:
                        print(f"{GREEN}[*] {user} added 1 follower.")
                        sleep(1)
                        print(f"{YELLOW}[*] Username >>> {[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}")
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
                                print(f"{YELLOW}[⇒] Username >>> {followee}")
                    else:
                        print(f"{GREEN}[*] {user} started following {len(FOLLOWEESAF) - len(FOLLOWEES)}")
                        sleep(2)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(1)
                        for followee in FOLLOWEESAF:
                            if followee not in FOLLOWEES:
                                print(f"{YELLOW}[⇒] Username >>> {followee}")
                    sleep(4)
                else:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        print(f"{GREEN}[*] {user} stopped following 1 user.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username >>> {[FOLLOWEES[i] for i in range(len(FOLLOWEES)) if FOLLOWEES[i] not in FOLLOWEESAF][0]}")
                    else:
                        print(f"{GREEN}[*] {user} started following 1 user.")
                        sleep(1)
                        print(f"{YELLOW}[⇒] Username >>> {[FOLLOWEESAF[i] for i in range(len(FOLLOWEESAF)) if FOLLOWEESAF[i] not in FOLLOWEES][0]}")
                    sleep(2)
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        keep=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
        while keep in EMPTY or keep.lower() not in ANS:
            print(f"{RED}[!] Invalid answer !")
            sleep(1)
            print(f"{YELLOW}[+] Acceptable answers >>> {ANS}")
            sleep(2)
            keep=input(f"{YELLOW}[?] Keep log (save to CSV) ? ")
        keep = keep.lower() == ANS[0]
        if keep:
            ADDFL, REMFL, ADD, RM = []
            with open(name, 'w', encoding='utf8') as f:
                if len(FOLLOWERS) != len(FOLLOWERSAF):
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        f.write(f'[*] {user} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} followers.\n')
                        f.write('USERNAMES\n'+'-'*20+'\n')
                        for i in FOLLOWERS:
                            if i not in FOLLOWERSAF:
                                f.write(f'[⇒] Username >>> {i}\n')
                                REMFL.append(i)
                        f.write('-'*20)
                    else:
                        f.write(f'[*] {user} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers\n')
                        f.write('USERNAMES'+'-'*20+'\n')
                        for i in FOLLOWERSAF:
                            if i not in FOLLOWERS:
                                f.write(f'[⇒] Username >>> {i}\n')
                                ADDFL.append(i)
                        f.write('-'*20)
                else:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        f.write(f'[*] {user} stopped following {len(FOLLOWEES) - len(FOLLOWEESAF)} users\n')
                        f.write('USERNAMES'+'-'*20+'\n')
                        for i in FOLLOWEES:
                            if i not in FOLLOWEESAF:
                                f.write(f'[⇒] Username >>> {i}\n')
                                ADD.append(i)
                        f.write('-'*20)
                    else:
                        f.write(f'[*] {user} started following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.\n')
                        f.write('USERNAMES' + '-' * 20 + '\n')
                        for i in FOLLOWEESAF:
                            if i not in FOLLOWEES:
                                f.write(f'[⇒] Username >>> {i}\n')
                            RM.append(i)
                        f.write('-'*20)
            L = [
                ['Followers removed', 'Followers added', 'Followings removed', 'Followings added']
            ]
            ADDFL.extend([''] * len(REMFL) - len(ADDFL)) if len(REMFL) > len(ADDFL) else REMFL.extend([''] * len(ADDFL) - len(REMFL))
            ADD.extend([''] * len(RM) - len(ADD)) if len(RM) > len(ADD) else RM.extend([''] * len(ADD) - len(RM))
            for i in range(len(ADDFL)):
                L.append([REMFL[i], ADDFL[i]])
            for i in range(len(ADD)):
                L.append([RM[i], ADD[i]])
            with open(output, mode='w', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerows(L)
            print(f"{GREEN}[✓] Successfully saved log / CSV.")
            sleep(1.3)
            print(f"{YELLOW}[↪] Log file name >>> {name}")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV file name >>> {output}")
            sleep(0.4)
            print(f"{YELLOW}[↪] Log location >>> {fpath(name)}")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV location >>> {fpath(output)}")
            sleep(0.4)
            print(f"{YELLOW}[↪] Log file size >>> {os.stat(fpath(name)).st_size} bytes")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV file size >>> {os.stat(fpath(output)).st_size} bytes")
            sleep(2)
    
    elif num == 2:
        clear()
        ScriptInfo()
        print("\n\n")
        sleep(5)

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🫡")
        sleep(1)
        quit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()

    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while numb not in range(1, 3):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(1)
        numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if numb == 1:
        clear()
        main()
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()

if __name__ == '__main__':
    main()
