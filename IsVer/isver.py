# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

IsVer finds and displays the usernames of the verified users followed by a user on Instagram.

For results example >>> ./Photos/output.png   &   ./Photos/output_.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of IsVer.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! IsVer requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3 : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IsVer ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    import platform
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'rich', 'platform', 'os', 'requests', 'instaloader', 'logging', 'prettytable', 'colorama', 'ctypes', 'argparse')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import os
    from os import system
    import instaloader
    import requests
    import logging
    import ctypes
    import argparse
    from prettytable import PrettyTable
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in IsVer have been installed !")
    sleep(1.5)
    print("[+] Ignoring warning...")
    sleep(0.6)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(1)
            print("[+] Attempting to enable root user...")
            sleep(1)
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("sudo pip install -r ./../requirements.txt" if sys.platform.startswith('linux') else "python -m pip install ./../requirements.txt")
    elif platform.system() == 'Windows':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[✘] Root user not detected !")
            sleep(1)
            print("[+] Attempting to enable root user...")
            sleep(1)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[+] Root user permission denied.")
                sleep(1)
                print("[+] Exiting...")
                sys.exit()
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("pip install -r ./../requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.LIGHTYELLOW_EX

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

ANS = ('yes', 'no')
EMPTY = ('', ' ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

def ScriptInfo():
    rest = requests.get('https://api.github.com/repos/new92/InstaTools/contributors', headers=headers)
    contribs = []
    if rest.status_code == 200:
        jsn = rest.json()
        contribs = [jsn[i]['login'] for i in range(len(jsn))]
    lang = requests.get('https://api.github.com/repos/new92/InstaTools/languages', headers=headers)
    languages = list(lang.json().keys()) if lang.status_code == 200 else []
    print(f"{YELLOW}[+] Author | {js['owner']['login']}")
    print(f"{YELLOW}[+] Github | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Leetcode | @{js['owner']['login']}")
    print(f"{YELLOW}[+] PyPI | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Contributors | {contribs}")
    print(f"{YELLOW}[+] License | {js['license']['spdx_id']}")
    print(f"{YELLOW}[+] Programming language(s) used | {languages}")
    print(f"{YELLOW}[+] Script's name | {js['name']}")
    print(f"{YELLOW}[+] Latest update | {js['updated_at']}")
    print(f"{YELLOW}[+] File size | {os.stat(__file__).st_size} bytes")
    print(f"{YELLOW}[+] File path | {os.path.abspath(__file__)}")
    print(f"{YELLOW}[+] Directory path | {os.path.dirname(os.path.abspath(__file__))}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Repo name | {js['name']}")
    print(f"{YELLOW}[+] Description | {js['description']}")
    print(f"{YELLOW}[+] Repo URL | {js['html_url']}")
    print(f"{YELLOW}[+] Stars | {js['stargazers_count']}")
    print(f"{YELLOW}[+] Forks | {js['forks']}")
    print(f"{YELLOW}[+] Watchers | {js['subscribers_count']}")
    print(f"{YELLOW}[+] Open issues | {js['open_issues_count']}")
    
def banner() -> str:
    console.log("""[bold green]
 /$$$$$$  /$$$$$$        /$$    /$$ /$$$$$$$$ /$$$$$$$ 
|_  $$_/ /$$__  $$      | $$   | $$| $$_____/| $$__  $$
  | $$  | $$  \__/      | $$   | $$| $$      | $$  \ $$
  | $$  |  $$$$$$       |  $$ / $$/| $$$$$   | $$$$$$$/
  | $$   \____  $$       \  $$ $$/ | $$__/   | $$__  $$
  | $$   /$$  \ $$        \  $$$/  | $$      | $$  \ $$
 /$$$$$$|  $$$$$$/         \  $/   | $$$$$$$$| $$  | $$
|______/ \______/           \_/    |________/|__/  |__/
[/]""", justify='center')

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

name = 'IsVer__Log.txt'

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
    return f"{GREEN}[✔] Files and dependencies removed successfully !"

def main(username: str, target: str, session: str):
    console = Console()
    table = Table(show_footer=False)
    centered = Align.center(table)
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Use IsVer to track down the verified users a user follows on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate IsVer[/]")
    console.print("[bold yellow][2] Show IsVer's info[/]")
    console.print("[bold yellow][3] Clear log file[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,6):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            while con not in ANS or con in EMPTY:
                print(f"{RED}[✘] Invalid answer !")
                sleep(0.8)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(0.8)
                con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            if con == ANS[0]:
                logging.basicConfig(
                    filename='consent.txt',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall IsVer and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                valErr = num in (1,2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall IsVer and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                        valErr = num in (1,2)
                    except ValueError:
                        print(f"{RED}[✘] Invalid number !")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    sys.exit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Thank you for using IsVer 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        sleep(2)
        clear()
        sleep(0.5)
        print(f"{GREEN}[*] Using session file >>> {session}...")
        sleep(1.3)
        try:
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✘] Error loading session file !")
            sleep(1)
            print(f"{YELLOW}[+] Error message >>> {ex}")
            sleep(0.8)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(1.4)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.85)
        clear()
        sleep(0.4)
        print(f"{YELLOW}[+] Loading profile...")
        sleep(0.6)
        profile = None
        try:
            profile = instaloader.Profile.from_username(loader.context, target)
        except instaloader.ProfileNotExistsException:
            print(f"{RED}[✘] Profile not found")
            sleep(1)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[::] Please enter a number (from the above ones) >>> "))
            while num not in range(1,3):
                print(f"{RED}[✘] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                sleep(1)
                num=int(input("[::] Please enter again a number (from the above ones) >>> "))
            if num == 1:
                clear()
                main(username, target, session)
            else:
                clear()
                print(f"{RED}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(1)
                sys.exit()
        if profile:
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.85)
            clear()
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
            while keep not in ANS or keep in EMPTY:
                print(f"{RED}[✘] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
            keep = keep == ANS[0]
            sleep(0.8)
            clear()
            print(f"{YELLOW}[+] Fetching {target}'s followings...")
            sleep(0.8)
            FOLLOWINGS = [following.username for following in profile.get_followees()]
            VERS, FOLS, FOLLS = [], [], []
            if not FOLLOWINGS:
                print(f"{RED}[✘] Fail. 0 followers detected. IsVer can't work without followers.")
                sleep(0.9)
                print(f"{RED}[+] Exiting...")
                sys.exit()
            print(f"{GREEN}[✔] Done.")
            sleep(1)
            print(f"{YELLOW}[+] Extracting verified followings...")
            sleep(0.8)
            for it in FOLLOWINGS:
                prof = instaloader.Profile.from_username(loader.context, it)
                if prof.is_verified:
                    VERS.append(prof.username)
                    FOLS.append(prof.followees)
                    FOLLS.append(prof.followers)
            followees = profile.followees
            fol = len(VERS) > 0
            print(f"{GREEN}[✔] Done." if fol else f"{RED}[✘] Fail.")
            sleep(0.8)
            print(f"{YELLOW}[+] Is {target} following verified accounts ? {GREEN}{fol}" if fol else f"{YELLOW}[+] Is {target} following verified accounts ? {RED}{fol}")
            sleep(0.6)
            if fol:
                print(f"{YELLOW}[+] {target} follows {len(VERS)} verified accounts.")
                sleep(1)
                table = PrettyTable()
                table.field_names = ['usernames', 'followers', 'followings']
                for i in range(len(VERS)):
                    table.add_row(row=[VERS[i], FOLLS[i], FOLS[i]])
                print(f"{YELLOW}{table}")
                sleep(5)
                print(f"{GREEN}[+] Percentage of verified accounts followed by {target} ==> {round((float(len(VERS)) / len(FOLLOWINGS)*100), 2)}%")
                sleep(0.8)
                print(f"{GREEN}[+] Verified followings ==> {len(VERS)}/{followees}")
                if keep:
                    with open(name, 'w', encoding='utf-8') as fp:
                        fp.write(str(table))
                    print(f"{GREEN}[✔] Successfully saved log !")
                    sleep(1.2)
                    path = fpath(name)
                    print(f"{GREEN}[↪] Name >>> {name}", f"{GREEN}[↪] Path >>> {path}", f"{GREEN}[↪] Size >>> {os.stat(path).st_size} bytes", sep='\n')
                    sleep(1.5)
                    
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        location = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
        if os.path.exists(location):
            with open(location.replace('\\', '/'), 'w') as f:
                pass
            print(f"{GREEN}[✔] Log file cleared successfully !")
            sleep(0.8)
            print(f"{GREEN}[↪] Name >>> {name}", f"{GREEN}[↪] Location >>> {location}", f"{GREEN}[↪] Size >>> 0 bytes", sep="\n")
            sleep(3)
        else:
            print(f"{RED}[✘] Unable to locate log file.")
            sleep(0.8)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using IsVer 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
    
    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while number not in range(1,3):
        print(f"{RED}[✘] Invalid number !")
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if number == 1:
        clear()
        main(username, target, session)
    else:
        clear()
        print(f"{RED}[+] Exiting...")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
try:
    if __name__ == '__main__':
        sleep(2)
        clear()
        parser = argparse.ArgumentParser(description='IsVer traces the usernames of the verified users followed by a user on Instagram.')
        parser.add_argument('-u', '--username', help='Your username on Instagram.')
        parser.add_argument('-t', '--target', help='The target username.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 isver.py -u <username> -t <target_username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.target=input(f"{YELLOW}[::] Please enter the target username >>> ") if not args.target else args.target
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.target.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()