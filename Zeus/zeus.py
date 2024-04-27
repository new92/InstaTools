# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Zeus is a powerful tool used for harvesting the mutual likers, commenters and their comments accross a range of posts.

For short code example >>> ./Photos/short_code_example.png

For analysis example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Zeus.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Zeus requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Zeus ✅")
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
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'csv', 'prettytable', 'argparse', 'ctypes')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import instaloader
    import csv
    import logging
    import requests
    import os
    import ctypes
    import argparse
    from os import system
    from colorama import init, Fore
    from prettytable import PrettyTable
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Zeus have been installed !")
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
CYAN = Fore.LIGHTBLUE_EX

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

def banner() -> str:
    console.log(r"""[bold green]
                                         ______ _____  _   _  _____ 
                                        |___  /|  ___|| | | |/  ___|
                                           / / | |__  | | | |\ `--.
                                          / /  |  __| | | | | `--. \
                                        ./ /___| |___ | |_| |/\__/ /
                                        \_____/\____/  \___/ \____/
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

def filter(L: list) -> list:
    USERS = []
    OS = []
    for i in range(len(L)):
        count = 0
        key = L[i]['commenter']
        if key in list(L[i].values()):
            for j in range(i, len(L), 1):
                if key in list(L[j].values()):
                    count += 1
            if count == len(L):
                OS.append(list(L[i]['comment']))
                if key not in USERS:
                    USERS.append(key)
    return USERS, OS

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Zeus.csv')).replace('\\', '/')

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

def main(username: str, session: str):
    console = Console()
    table = Table(show_footer=False)
    centered = Align.center(table)
    clear()
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Zeus is a powerful tool used for harvesting the mutual likers, commenters and their comments accross a range of posts.[/]")
    print("\n")
    console.print("[bold yellow][1] Analyze posts[/]")
    console.print("[bold yellow][2] Show Zeus's info[/]")
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
        loader = instaloader.Instaloader()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").lower()
            while con not in ANS:
                print(f"{RED}[✘] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con= input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").lower()
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
                print(f"{YELLOW}[2] Uninstall Zeus and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Zeus and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
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
                    sleep(0.8)
                    print(f"{YELLOW}[+] Thank you for using Zeus 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        sleep(2)
        clear()
        print(f"{GREEN}[*] Using session file >>> {session}...")
        sleep(1.3)
        try:
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✘] Error loading session file !")
            sleep(0.8)
            print(f"{YELLOW}[+] Error message >>> {ex}")
            sleep(1.5)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(0.8)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.85)
        clear()
        sleep(0.7)
        print(f"{CYAN}[*] Extracting codes from text file...")
        sleep(0.5)
        with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shortcodes.txt')).replace('\\', '/'), 'r', encoding='utf-8') as f:
            CODES = [code.replace('\n', '') for code in f]
        sleep(0.5)
        print(f"{GREEN}[✔] Successfully extracted {len(CODES)} shortcodes.")
        sleep(0.7)
        clear()
        sleep(0.4)
        print(f"{GREEN}[+] Starting the analysis process....")
        sleep(0.5)
        LIKERS, COMS = [], []
        for code in CODES:
            post = instaloader.Post.from_shortcode(loader.context, code)
            likers = [liker.username for liker in post.get_likes()]
            if likers:
                LIKERS.append(likers)
                for comment in post.get_comments():
                    COMS.append({
                        'commenter': comment.owner.username,
                        'comment': comment.text
                    })
        MULIK = [user for user in LIKERS[0] if any(user in sublist for sublist in LIKERS[1:])]
        MUTS, MUTCOM = filter(COMS)
        MUTS.extend([''] * (len(MULIK) - len(MUTS)))
        MUTCOM.extend([''] * (len(MULIK) - len(MUTCOM)))
        table = PrettyTable()
        table.field_names = ['Mutual likers', 'Mutual commenters', '(Mutual) Commenters comments']
        for i in range(len(MULIK)):
            table.add_row([MULIK[i], MUTS[i], MUTCOM[i]])
        sleep(0.5)
        print(f"{GREEN}[✔] Done.")
        lks = len(MULIK)
        muts = len(MUTS) if MUTS != list([''] * (len(MULIK) - len(MUTS))) else 0
        mutcm = len(MUTCOM) if MUTCOM != list([''] * (len(MULIK) - len(MUTCOM))) else 0
        coms = len(COMS)
        likers = 0
        for i in range(len(LIKERS)):
            likers += len(LIKERS[i])
        sleep(0.5)
        print(f"{YELLOW}[+] Total mutual likers >>> {lks} / {likers}")
        sleep(0.4)
        print(f"{YELLOW}[+] Total mutual commenters >>> {muts} / {coms}")
        sleep(0.4)
        print(f"{YELLOW}[+] Total (Mutual) Commenters comments >>> {mutcm} / {coms}")
        sleep(1.3)
        clear()
        print(f"{YELLOW}{table}")
        L = [
            ['Total mutual likers', 'Total mutual commenters', 'Total (Mutual) Commenters comments'],
            [lks, muts, mutcm],
            ['Mutual likers', 'Mutual commenters', '(Mutual) Commenters comments']
        ]
        sleep(5)
        print("\n\n\n")
        print(f"{CYAN}[*] Writing data to output file...")
        sleep(0.4)
        for i in range(len(MULIK)):
            L.append([MULIK[i], MUTS[i], MUTCOM[i]])
        with open(output, mode='w') as csvf:
            writer = csv.writer(csvf)
            writer.writerows(L)
        print(f"{GREEN}[✔] Done. Successfully saved data at >>> {output}")

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
    
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Zeus 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()
    
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Zeus 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
    
    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while number not in range(1,3):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(2)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if number == 1:
        clear()
        main(username, session)
    else:
        clear()
        print(f"{YELLOW}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(2)
        sys.exit()

try:
    if __name__ == '__main__':
        sleep(2)
        clear()
        parser = argparse.ArgumentParser(description='Zeus is a powerful tool used for harvesting the mutual likers, commenters and their comments accross a range of posts.')
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 3:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 zeus.py -u <your_username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()