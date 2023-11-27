# -*- coding: utf-8 -*-
"""
Author: new92
Contributors: [Itsfizziks, ProgramR4732]
Github: @new92
Leetcode: @new92
PyPI: @new92

Script in which the user enters a username and the script returns if the user with the specific username follows verified users.
If true then:
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
        sys.exit()
    import platform
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'rich', 'platform', 'os', 'requests', 'instaloader', 'logging', 'prettytable' ,'json', 'colorama')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay[/]')
    import os
    import json
    from os import system
    import instaloader
    import requests
    import logging
    from prettytable import PrettyTable
    from colorama import init, Fore
except ImportError:
    print("[!] WARNING: Not all packages used in IsVer have been installed !")
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
                print("[1] Uninstall IsVer")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt not in range(1,3):
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

sleep(0.8)
console.clear()
console.print("[bold dark_green][✓] Successfully loaded modules.[/]")
sleep(0.8)
console.clear()

ANS = ('yes', 'no')
EMPTY = ('', ' ')

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
    with open('config.json') as config:
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
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] Latest update: {conf['update']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")
    
def banner() -> str:
    console.log("""[bold yellow]
    ██╗░██████╗██╗░░░██╗███████╗██████╗░
    ██║██╔════╝██║░░░██║██╔════╝██╔══██╗
    ██║╚█████╗░╚██╗░██╔╝█████╗░░██████╔╝
    ██║░╚═══██╗░╚████╔╝░██╔══╝░░██╔══██╗
    ██║██████╔╝░░╚██╔╝░░███████╗██║░░██║
    ╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    [/]""")

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

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

def checkUser(username:str) -> bool:
    return username in EMPTY or len(username) > 30

name = 'IsVer_log.txt'

def ValUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

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
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] With IsVer you can see if a user follows verified accounts and if yes which and how many (on Instagram).[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate IsVer[/]")
    console.print("[bold yellow][2] Show IsVer's info[/]")
    console.print("[bold yellow][3] Clear log file[/]")
    console.print("[bold yellow][4] Uninstall IsVer[/]")
    console.print("[bold yellow][5] Exit[/]")
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
        con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
        while con.lower() not in ANS:
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
        print(f'{YELLOW}|--------------------LOGIN--------------------|')
        session=input(f"{YELLOW}[::] Please enter the cookie file path: ")
        session = session.strip().lower()
        while not validate(session):
            print(f"{RED}[!] Invalid file path !")
            sleep(1)
            session=input(f"{YELLOW}[::] Please enter the cookie file path again: ")
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
            username= input(f"{YELLOW}[::] Please enter the username of the target user: ")
            while checkUser(username):
                if username in EMPTY:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid username !")
                username= input(f"{YELLOW}[::] Please enter again the username of the target user: ")
            username = username.strip().lower()
            while ValUser(username):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                print(f"{YELLOW}[4] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while opt not in range(1,5):
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1-4]")
                    sleep(1)
                    opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if opt == 1:
                    username=str(input(f"{YELLOW}[::] Please enter the username: "))
                    while checkUser(username):
                        if username in EMPTY:
                            print(f"{RED}[!] This field can't be blank !")
                        else:
                            print(f"{RED}[!] Invalid username !")
                        sleep(1)
                        username= input(f"{YELLOW}[::] Please enter again the username: ")
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
                    print(f"{GREEN}[+] Thank you for using IsVer 😁")
                    sleep(2)
                    print(f"{GREEN}[+] Until next time 👋")
                    sleep(2)
                    quit()
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers: {ANS}")
            sleep(1)
            keep= input(f"{YELLOW}[?] Keep log ? ")
            while keep.lower() not in ANS:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: {ANS}")
                sleep(2)
                keep= input(f"{YELLOW}[?] Keep log ? ")
            keep = keep.lower() == ANS[0]
            FOLLOWINGS = [following.username for following in profile.get_followees()]
            VERS = []
            for i in FOLLOWINGS:
                ver_profile = instaloader.Profile.from_username(loader.context, i)
                if ver_profile.is_verified:
                    VERS.append(i)
            followees = profile.followees
            print(f"{YELLOW}[+] Is {username} following verified accounts ? {not len(VERS)}")
            if not len(VERS):
                sleep(2)
                print(f"{YELLOW}[1] Return to menu")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
                while num not in range(1,3):
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                    sleep(2)
                    num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
                if num == 1:
                    clear()
                    main()
                else:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for using IsVer 😁")
                    quit()
            else:
                print(f"{YELLOW}[+] {username} follows {len(VERS)} verified accounts")
                sleep(2)
                table = PrettyTable()
                table.field_names = ('usernames', 'followers', 'followings')
                for i in range(len(VERS)):
                    table.add_row([VERS[i], VERS[i].followers, VERS[i].followings])
                print(table)
                sleep(5)
                print(f"{GREEN}[+] Percentage of verified accounts followed by {username} ==> {float(len(VERS)) / len(FOLLOWINGS)*100}%")
                sleep(2)
                print(f"{GREEN}[+] Verified followings: {len(VERS)}/{followees}")
                if keep:
                    with open(name, 'w', encoding='utf8') as fp:
                        fp.write(str(table))
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] Name >>> {name}")
                    print(f"{GREEN}[↪] Path >>> {fpath(name)}")
                    print(f"{GREEN}[↪] Size >>> {os.stat(fpath(name)).st_size} bytes")
                    sleep(3)
                    
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
        print("\n\n")

    elif num == 3:
        clear()
        f = open(name,'w')
        f.close()
        print(f"{GREEN}[✓] Log file cleared successfully !")
        sleep(2)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(2)
        quit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while number not in range(1,3):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(2)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if number == 1:
        clear()
        main()
    else:
        clear()
        print(f"{YELLOW}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(2)
        quit()

if __name__ == '__main__':
    main()
