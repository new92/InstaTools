# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Spammer is a python script used for spamming messages on user(s) on Instagram.

*********DISCLAIMER*********
This script must not, under any circumstances, be designed or utilized in a manner that violates any of Instagram's rules, terms of service, or community guidelines. It is the user's responsibility to ensure compliance with Instagram's policies when using this script. Any misuse or violation of Instagram's rules resulting from the use of this script is the sole responsibility of the user. This script is intended for legitimate and ethical purposes only. Use it responsibly and in full accordance with Instagram's guidelines.
The author (new92) has no responsibility for the user of this script. Please use it responsibly.
****************************

{*********IMPORTANT*********}
User's login credentials (such as: username, password) won't be stored ! 
Will be used only for the purpose of Spammer.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Spammer requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3 : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Spammer ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'rich', 'platform', 'os', 'ctypes', 'logging', 'instagrapi', 'requests', 'colorama', 'argparse')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import platform
    from os import system
    import instagrapi
    import os
    import logging
    import requests
    import ctypes
    import argparse
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Spammer have been installed !")
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
            sleep(2)
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

ANS = ('yes', 'no')
EMPTY = ('', ' ')

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

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

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            dirs = (os.path.join(root, dir) for dir in dirs)
        for i in dirs:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f"{GREEN}[✔] Files and dependencies removed successfully !"

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
    console.log("""[bold green]
  _____ _____        __  __ __  __ ______ _____  
 / ____|  __ \ /\   |  \/  |  \/  |  ____|  __ \ 
| (___ | |__) /  \  | \  / | \  / | |__  | |__) |
 \___ \|  ___/ /\ \ | |\/| | |\/| |  __| |  _  / 
 ____) | |  / ____ \| |  | | |  | | |____| | \ \ 
|_____/|_| /_/    \_\_|  |_|_|  |_|______|_|  \_\
[/]""", justify='center')

def main(username: str, password: str):
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
    console.print("[bold yellow][+] Spammer is a python script used for spamming messages on user(s) on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate Spammer[/]")
    console.print("[bold yellow][2] Show Spammer's info[/]")
    console.print("[bold yellow][3] Uninstall InstaTools[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,5):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if num == 1:
        clear()
        client = instagrapi.Client()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            while con not in ANS or con in EMPTY:
                print(f"{RED}[✘] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            if con == ANS[0]:
                logging.basicConfig(
                    filename='consent.txt',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall Spammer and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                while num not in range(1,3):
                    print(f"{RED}[✘] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                    sleep(2)
                    num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones) >>> "))
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(2)
                    sys.exit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for using Spammer 🫡")
                    sleep(2)
                    print(f"{GREEN}[+] Until we meet again 👋")
                    sleep(1)
                    sys.exit()
        sleep(0.8)
        clear()
        msg = 'hello world'
        print(f"{YELLOW}[*] Attempting to login...")
        sleep(0.4)
        try:
            client.login(username,password)
        except Exception as ex:
            print(f"{RED}[✘] Login error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        sleep(0.7)
        print(f"{GREEN}[✔] Successfully logged in !")
        sleep(0.9)
        print(f"{YELLOW}[*] Loading targets...")
        sleep(0.5)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'targets.txt')) as f:
            targets = [target.replace('\n', '') for target in f]
        IDS = [client.user_info_by_username(targets[i])['pk'] for i in range(len(targets))]
        sleep(0.4)
        print(f"{GREEN}[✔] Loaded {len(IDS)} target(s) !")
        sleep(0.8)
        print(f"{YELLOW}[*] Default message >>> {msg}")
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        change=input(f"{YELLOW}[?] Change the message ? ").strip().lower()
        while change not in ANS:
            print(f'{RED}[✘] Invalid answer !')
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(0.9)
            change=input(f"{YELLOW}[?] Change the message ? ").strip().lower()
        if change == ANS[0]:
            sleep(0.4)
            msg=input(f"{YELLOW}[::] Please enter the new message >>> ")
        msgs = 0
        sleep(1)
        clear()
        print(f"{GREEN}[+] To stop the process hit >>> <Ctrl> + <C>")
        sleep(1.5)
        try:
            while True:
                client.direct_send(msg,IDS)
                sleep(0.8)
                print(f"{GREEN}[✔] Message Sent | Message >>> {msg}")
                msgs += 1
        except (KeyboardInterrupt, EOFError):
            print(f"{GREEN}[✔] Successfully sent {msgs} to {len(IDS)} targets.")
        client.logout()

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(0.9)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(1)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(0.9)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.9)
        sys.exit()

    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num < 1 or num > 2:
        print(f"{RED}[✘] Invalid number !")
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{GREEN}[+] Thank you for using Spammer 🫡")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        print(f"{RED}[+] Exiting...")
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Spammer is a python script used for spamming messages on user(s) on Instagram.")
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-p', '--password', help='Your instagram password.')
        args = parser.parse_args()
        if len(sys.argv) < 3:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 spammer.py -u <your_username> -p <your_password>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.password=input(f"{YELLOW}[::] Please enter your password >>> ") if not args.password else args.password
        main(args.username.strip().lower(), args.password.strip().lower())
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()