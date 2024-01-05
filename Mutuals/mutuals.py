# -*- coding: utf-8 -*-
"""
Author: new92
Contributors: [Itsfizziks, ProgramR4732]
Github: @new92
Leetcode: @new92
PyPI: @new92

Mutuals is a powerful Python script designed to discover and display mutual followers and followings between two Instagram accounts. Whether you're looking to strengthen connections or gain insights into shared networks, Mutuals simplifies the process, allowing users to identify and connect with those who share mutual interests and connections on Instagram.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print(f"[!] Error ! Mutuals requires Python version 3.X ! ")
        sleep(2)
        print(f"""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print(f"[*] Please install Python 3 and then use Mutuals ✅")
        sleep(2)
        print(f"[+] Exiting...")
        sleep(1)
        quit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'rich', 'platform', 'os', 'requests', 'instaloader', 'logging', 'json', 'colorama')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay[/]')
    import platform
    from os import system
    import instaloader
    import os
    import json
    import logging
    import requests
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print(f"[!] WARNING: Not all packages used in Mutuals have been installed !")
    sleep(2)
    print(f"[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid():
            print(f"[!] Root user not detected !")
            sleep(2)
            print(f"[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print(f"[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print(f"[1] Uninstall Mutuals")
                print(f"[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt not in range(1,3):
                    print(f"[!] Invalid number !")
                    sleep(1)
                    print(f"[+] Acceptable numbers: [1/2]")
                    sleep(2)
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
                    print(f"[✓] Files and dependencies uninstalled successfully !")
                else:
                    print(f"[+] Exiting...")
                    sleep(1)
                    print(f"[+] See you next time 👋")
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
console.print("[bold dark_green][✓] Successfully loaded modules.[/]")
sleep(0.8)
console.clear()

def checkUser(username:str) -> bool:
    return username in EMPTY or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def validate(session: str) -> bool:
    return os.path.exists(session)

def ScriptInfo():
    with open('Mutuals/config.json') as config:
        conf = json.load(config)
    f = f"{conf['name']}.py"
    fp = fpath(f) is None
    fsize = os.stat(fpath(f)).st_size if fp else 0
    print(f"{YELLOW}[+] Author | {conf['author']}")
    print(f"{YELLOW}[+] Contributors | {conf['contributors']}")
    print(f"{YELLOW}[+] Github | @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode | @{conf['author']}")
    print(f"{YELLOW}[+] PyPI | @{conf['author']}")
    print(f"{YELLOW}[+] License | {conf['lice']}")
    print(f"{YELLOW}[+] Natural language | {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used | {conf['language']}")
    print(f"{YELLOW}[+] Number of lines | {conf['lines']}")
    print(f"{YELLOW}[+] Script's name | {conf['name']}")
    print(f"{YELLOW}[+] API(s) used | {conf['api']}")
    print(f"{YELLOW}[+] Latest update | {conf['update']}")
    print(f"{YELLOW}[+] File size | {fsize} bytes")
    print(f"{YELLOW}[+] File path | {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars | {conf['stars']}")
    print(f"{YELLOW}[+] Forks | {conf['forks']}")
    print(f"{YELLOW}[+] Open issues | {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues | {conf['clissues']}")
    print(f"{YELLOW}[+] Closed pull requests | {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions | {conf['discs']}")

def extract(raw_path: str):
    index = raw_path.find('session-')
    return raw_path[index + len('session-'):] if index != -1 else None

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

def banner() -> str:
    console.log("""[bold yellow]
███╗░░░███╗██╗░░░██╗████████╗██╗░░░██╗░█████╗░██╗░░░░░░██████╗
████╗░████║██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░██╔════╝
██╔████╔██║██║░░░██║░░░██║░░░██║░░░██║███████║██║░░░░░╚█████╗░
██║╚██╔╝██║██║░░░██║░░░██║░░░██║░░░██║██╔══██║██║░░░░░░╚═══██╗
██║░╚═╝░██║╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗██████╔╝
╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
[/]""")

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

def nums():
    console.print("[bold yellow][1] Find mutuals[/]")
    console.print("[bold yellow][2] Show Mutual's info[/]")
    console.print("[bold yellow][3] Update Mutuals[/]")
    console.print("[bold yellow][4] Uninstall Mutuals[/]")
    console.print("[bold yellow][5] Exit[/]")

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            
            DIRS = (os.path.join(root,dir) for dir in dirs)

        for i in DIRS:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Python script to retrieve the mutual followers/followings between 2 accounts.[/]")
    print("\n")
    nums()
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num not in range(1,6):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print(f"{GREEN}[+] Acceptable answers: {ANS}")
        sleep(1)
        con= input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
        while con.lower() not in ANS or con in EMPTY:
            if con in EMPTY:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: {ANS}")
            sleep(1)
            con= input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
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
                    valErr = num in (1,2)
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1,2]")
                    sleep(1)
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                quit()
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
                quit()
        sleep(2)
        clear()
        print(f'{YELLOW}|--------------------|LOGIN|--------------------|')
        session= input(f"{YELLOW}[::] Please enter the cookie file path: ")
        session = session.strip().lower()
        while not validate(session):
            print(f"{RED}[!] Invalid file path !")
            sleep(1)
            session= input(f"{YELLOW}[::] Please enter the cookie file path again: ")
        username = extract(session)
        sleep(0.5)
        print(f"{GREEN}[✓] Extracted username: {username}...")
        sleep(1)
        print(f"{GREEN}[+] Using session file: {session}...")
        sleep(2)
        try: 
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
                print(f"{GREEN}[✓] Session loaded successfully !")
                sleep(1)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✕] Error loading session file !")
            sleep(1)
            print(f"{YELLOW}[+] Error message: {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit()
        profile = None
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
        except instaloader.ProfileNotExistsException:
            print(f"{RED}[!] Profile not found")
            sleep(1)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[::] Please enter a number (from the above ones): "))
            while num not in range(1,3):
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(1)
                num=int(input("[::] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(2)
                quit()
        if profile:
            print(f"{GREEN}[✓] Login successfull !")
            sleep(0.85)
            clear()
            print(f"{YELLOW}[1] Find the mutual followers between 2 accounts")
            print(f"{YELLOW}[2] Find the mutual followees between 2 accounts")
            t=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while t not in range(1,3):
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(2)
                print(f"{YELLOW}[1] Find mutual followers")
                print(f"{YELLOW}[2] Find mutual followees")
                t=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            usernamef= input(f"{YELLOW}[::] Please enter the first username: ")
            while checkUser(usernamef):
                if usernamef in EMPTY:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid length ! Acceptable length: <= 30 characters")
                sleep(1)
                usernamef= input(f"{YELLOW}[::] Please enter again the first username: ")
            usernamef = usernamef.lower().strip()
            while valUser(usernamef):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                print(f"{YELLOW}[4] Uninstall Mutuals and Exit")
                optf=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while optf not in range(1,5):
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                    sleep(2)
                    optf=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if optf == 1:
                    usernamef= input(f"{YELLOW}[::] Please enter the username: ")
                    while checkUser(usernamef):
                        if usernamef in EMPTY:
                            print(f"{RED}[!] This field can't be blank !")
                        else:
                            print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
                        sleep(1)
                        usernamef= input(f"{YELLOW}[::] Please enter again the username: ")
                elif optf == 2:
                    clear()
                    main()
                elif optf == 3:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Until next time 👋")
                    sleep(1)
                    quit()
                else:
                    clear()
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                    sleep(2)
                    print(f"{GREEN}[+] Until next time 👋")
                    sleep(2)
                    quit()
            usernames= input(f"{YELLOW}[::] Please enter the second username: ")
            while checkUser(usernames):
                if usernames in EMPTY:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid length ! Acceptable length: 30 or less characters")
                sleep(1)
                usernames= input(f"{YELLOW}[::] Please enter again the second username: ")
            usernames = usernames.strip().lower()
            while valUser(usernames):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                print(f"{YELLOW}[4] Uninstall Mutuals and Exit")
                opts=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while opts not in range(1,5):
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                    sleep(1)
                    opts=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if opts == 1:
                    usernames= input(f"{YELLOW}[::] Please enter the username: ")
                    while checkUser(usernames):
                        if usernames in EMPTY:
                            print(f"{RED}[!] This field can't be blank !")
                        else:
                            print(f"{RED}[!] Invalid length ! Acceptable length: <= 30 characters")
                        sleep(1)
                        usernames= input(f"{YELLOW}[::] Please enter again the username: ")
                elif opts == 2:
                    clear()
                    main()
                else:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Until next time 👋")
                    sleep(1)
                    quit()
            profilef=instaloader.Profile.from_username(loader.context, usernamef)
            profiles=instaloader.Profile.from_username(loader.context, usernames)
            ANS = ('yes','no')
            if t == 1:
                clear()
                FOLLOWERSF=[follower.username for follower in profilef.get_followers()]
                FOLLOWERSS=[follower.username for follower in profiles.get_followers()]
                if len(FOLLOWERSF) and len(FOLLOWERSS):
                    allf = len(FOLLOWERSF) + len(FOLLOWERSS)
                    if len(FOLLOWERSF) > len(FOLLOWERSS):
                        MUTUALS = [i for i in FOLLOWERSF if i in FOLLOWERSS]
                        if not len(MUTUALS):
                            print(f"{RED}[!] No mutual followers found !")
                            sleep(2)
                            print(f"{YELLOW}[+] Exiting")
                            sleep(1)
                            print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                            quit()
                        else:
                            print(f"{GREEN}[✓] Successfully found mutual followers !")
                            sleep(1)
                            per = (len(MUTUALS) / float(allf))*100
                            print(f"{YELLOW}[+] Number of mutual followers: {len(MUTUALS)}")
                            sleep(1)
                            print(f"{YELLOW}[+] Percentage of mutual followers: {per}%")
                            sleep(1)
                            print(f"{YELLOW}[+] The usernames of the mutual followers: ")
                            for k in MUTUALS:
                                print(f"{YELLOW}[+] Username No{k+1}: {k}")
                            sleep(3)
                            print(f"{GREEN}[+] Acceptable answers: {ANS}")
                            sleep(1)
                            savem= input(f"{YELLOW}[?] Save the mutual followers ? ")
                            while savem.lower() not in ANS:
                                print(f"{RED}[!] Invalid answer !")
                                sleep(1)
                                print(f"{GREEN}[+] Acceptable answers: {ANS}")
                                sleep(1)
                                savem= input(f"{YELLOW}[?] Save the mutual followers ? ")
                            if savem.lower() == ANS[0]:
                                name = 'mutuals.txt'
                                with open(name, 'w', encoding='utf8') as f:
                                    for i in MUTUALS:
                                        f.write(f"[+] Username No{i+1}: {i}\n")
                                sleep(1.5)
                                print(f"{GREEN}[✓] Successfully saved the mutual followers !")
                                sleep(2)
                                print(f"{YELLOW}[↪] Name >>> {name}")
                                print(f"{YELLOW}[↪] Location >>> {fpath(name)}")
                                print(f"{YELLOW}[↪] Size >>> {(os.stat(fpath(name))).st_size} bytes")
                                sleep(2)
                        clear()
                        MUTUALS = [i for i in FOLLOWERSS if i in FOLLOWERSF]
                        if not len(MUTUALS):
                            print(f"{RED}[!] No mutual followers found !")
                            sleep(2)
                            print(f"{YELLOW}[+] Exiting...")
                            sleep(1)
                            print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                            quit()
                        else:
                            per = len(MUTUALS) / float(allf)*100
                            print(f"{YELLOW}[+] Number of mutual followers: {len(MUTUALS)}")
                            sleep(1)
                            print(f"{YELLOW}[+] Percentage of mutual followers: {per}%")
                            sleep(1)
                            print(f"{YELLOW}[+] The usernames of the mutual followers: ")
                            for k in MUTUALS:
                                print(f"{YELLOW}[+] Username No{k+1}: {k}")
                            sleep(3)
                            print(f"{GREEN}[+] Acceptable answers: {ANS}")
                            sleep(1)
                            savem= input(f"{YELLOW}[?]  Save the mutual followers ? ")
                            while savem.lower() not in ANS or savem in EMPTY:
                                print(f"{RED}[!] Invalid answer !")
                                sleep(1)
                                print(f"{GREEN}[+] Acceptable answers: {ANS}")
                                sleep(1)
                                savem= input(f"{YELLOW}[?] Save the mutual followers ? ")
                            if savem.lower() == ANS[0]:
                                name = 'mutuals.txt'
                                with open(name, 'w', encoding='utf8') as f:
                                    for i in MUTUALS:
                                        f.write(f"[+] Username No{i+1}: {i}\n")
                                sleep(1.5)
                                print(f"{GREEN}[✓] Successfully saved mutual followers !")
                                sleep(2)
                                print(f"{YELLOW}[↪] Name: {name}")
                                print(f"{YELLOW}[↪] Location: {fpath(name)}")
                                print(f"{YELLOW}[↪] Size: {os.stat(fpath(name)).st_size} bytes")
                                sleep(1)
                else:
                    print(f"{RED}[!] No followers found !")
                    sleep(2)
                    if not len(FOLLOWERSF):
                        print(f"{YELLOW}[+] No followers found on: {usernamef}")
                    else:
                        print(f"{YELLOW}[+] No followers found on: {usernames}")
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                    sleep(2)
                    quit()
            else:
                clear()
                FOLLOWEESF=[followee.username for followee in profilef.get_followees()]
                FOLLOWEESS=[followee.username for followee in profiles.get_followees()]
                if len(FOLLOWEESF) and len(FOLLOWEESS):
                    allfe = len(FOLLOWEESF) + len(FOLLOWEESS)
                    if len(FOLLOWEESF) > len(FOLLOWEESS):
                        MUTUALS = [i for i in FOLLOWEESF if i in FOLLOWEESS]
                        if not len(MUTUALS):
                            print(f"{RED}[!] No mutual followees found !")
                            sleep(2)
                            print(f"{YELLOW}[+] Exiting...")
                            sleep(1)
                            print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                            quit()
                        else:
                            per = (len(MUTUALS) / float(allfe))*100
                            print(f"{YELLOW}[+] Number of mutual followees: {len(MUTUALS)}")
                            sleep(1)
                            print(f"{YELLOW}[+] Percentage of mutual followees: {per}%")
                            sleep(1)
                            print(f"{YELLOW}[+] The usernames of the mutual followees: ")
                            for k in MUTUALS:
                                print(f"{YELLOW}[+] Username No{k+1}: {k}")
                            sleep(2)
                            print(f'{GREEN}[+] Acceptable answers: {ANS}')
                            sleep(2)
                            savem= input(f"{YELLOW}[?] Save the mutual followees ? ")
                            while savem.lower() not in ANS:
                                print(f"{RED}[!] Invalid answer !")
                                sleep(1)
                                print(f"{GREEN}[+] Acceptable answers: {ANS}")
                                sleep(1)
                                savem= input(f"{YELLOW}[?] Save the mutual followees ? ")
                            if savem.lower() == ANS[0]:
                                name = 'mutualsf.txt'
                                with open(name, 'w', encoding='utf8') as f:
                                    for i in range(len(MUTUALS)):
                                        f.write(f"[+] Username No{i+1}: {MUTUALS[i]}\n")
                                sleep(1)
                                print(f"{GREEN}[✓] Successfully saved mutual followees !")
                                sleep(2)
                                print(f"{YELLOW}[↪] Name >>> {name}")
                                print(f"{YELLOW}[↪] Location >>> {fpath(name)}")
                                print(f"{YELLOW}[↪] Size >>> {os.stat(fpath(name)).st_size}")
                            sleep(1)
                else:
                    print(f"{RED}[!] No followees found !")
                    sleep(1)
                    if not len(FOLLOWEESF):
                        print(f"{YELLOW}[+] Followees not found on: {usernamef}")
                    else:
                        print(f"{YELLOW}[+] Followees not found on: {usernames}")
                    sleep(2)
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    quit()

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
        print("\n\n")

    elif num == 3:
        clear()
        system('git pull')
        sleep(1)
        print(f"{GREEN}[✓] Script updated successfully !")
        sleep(1)
        
    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
        sleep(2)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()

    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while number not in range(1, 3):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(2)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if number == 1:
        clear()
        main()
    else:
        print(f"{YELLOW}[+] Exiting...")
        sleep(1)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(2)
        quit()

if __name__ == '__main__':
    main()
