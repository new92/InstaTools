# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Hermes is a python script which analyzes a post and categorises its likers.

For short code example >>> ./Photos/short_code_example.png

For analysis example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Hermes.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Hermes requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Hermes ✅")
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
    import ctypes
    import os
    import argparse
    from os import system
    from colorama import init, Fore
    from prettytable import PrettyTable
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Hermes have been installed !")
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
                             __ __    ___  ____   ___ ___    ___   _____
                            |  T  T  /  _]|    \ |   T   T  /  _] / ___/
                            |  l  | /  [_ |  D  )| _   _ | /  [_ (   \_ 
                            |  _  |Y    _]|    / |  \_/  |Y    _] \__  T
                            |  |  ||   [_ |    \ |   |   ||   [_  /  \ |
                            |  |  ||     T|  .  Y|   |   ||     T \    |
                            l__j__jl_____jl__j\_jl___j___jl_____j  \___j
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

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Hermes.csv')).replace('\\', '/')

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

global username, session, code

def main(username: str, session: str, code: str):
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
    console.print("[bold yellow][+] Use Hermes to analyze a post and categorise its likers.[/]")
    print("\n")
    console.print("[bold yellow][1] Analyze post[/]")
    console.print("[bold yellow][2] Show Hermes's info[/]")
    console.print("[bold yellow][3] Clear csv file[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,6):
        print(f"{RED}[✘] Invalid number !")
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
        sleep(0.8)
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
                print(f"{YELLOW}[2] Uninstall Hermes and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Hermes and exit")
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
                    print(f"{YELLOW}[+] Thank you for using Hermes 🫡")
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
        print(f"{GREEN}[+] Analyzing....")
        sleep(0.5)
        post = instaloader.Post.from_shortcode(loader.context, code)
        likers = post.get_likes()
        LIKERS = [liker.username for liker in likers]
        if LIKERS:
            PUBS, PRIVS, VERS, POSTS, FOLLS, STATUS = [], [], [], [], [], []
            for liker in LIKERS:
                profile = instaloader.Profile.from_username(loader.context, liker)
                posts = profile.mediacount
                followers = profile.followers
                if profile.is_private:
                    PRIVS.append(liker)
                    STATUS.append('boring 🥱')
                else:
                    VERS.append(liker) if profile.is_verified else PUBS.append(liker)
                    if profile.is_verified:
                        STATUS.append('verified ✅')
                    elif posts > 49 or followers > 9999:
                        STATUS.append('interesting 🤔')
                    elif posts > 40:
                        STATUS.append('captivating 📸')
                    elif followers > 5000:
                        STATUS.append('famous 🌍')
                    else:
                        STATUS.append('ordinary 🤖')
                POSTS.append(posts)
                FOLLS.append(followers)
            lks = len(LIKERS)
            privs = len(PRIVS)
            vers = len(VERS)
            pubs = len(PUBS)
            posts = sum(POSTS)
            folls = sum(FOLLS)
            PRIVS.extend([''] * (len(LIKERS) - len(PRIVS)))
            PUBS.extend([''] * (len(LIKERS) - len(PUBS)))
            VERS.extend([''] * (len(LIKERS) - len(VERS)))
            table = PrettyTable()
            table.field_names = ['Likers', 'Publics', 'Privates', 'Verified', 'Posts', 'Followers', 'Status']
            for i in range(len(LIKERS)):
                table.add_row(row=[LIKERS[i], PUBS[i], PRIVS[i], VERS[i], POSTS[i], FOLLS[i], STATUS[i]])
            sleep(0.5)
            print(f"{GREEN}[✔] Success.")
            sleep(0.5)
            print(f"{YELLOW}[+] Total likers >>> {lks}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total privates >>> {privs}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total publics >>> {pubs}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total verified >>> {vers}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total posts >>> {posts}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total followers >>> {folls}")
            sleep(1.3)
            clear()
            print(f"{YELLOW}{table}")
            sleep(4)
            print(f"\n\n{GREEN}[*] Writing results to csv file...")
            sleep(0.4)
            L = [
                ['Total likers', 'Total privates', 'Total publics', 'Total verified', 'Total posts', 'Total followers'],
                [lks, privs, pubs, vers, posts, folls],
                ['Likers', 'Private', 'Public', 'Verified', 'Posts', 'Followers', 'Status']
            ]
            for i in range(len(LIKERS)):
                L.append([LIKERS[i], PRIVS[i], PUBS[i], VERS[i], POSTS[i], FOLLS[i]])
            with open(output, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(L)
            print(f"{GREEN}[✔] Done. Saved data at >>> {output}")
        else:
            print(f"{RED}[✘] Error: No likers found.")
            sleep(0.5)
            print(f"{RED}[+] Exiting...")
            sys.exit()

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        if os.path.exists(output):
            with open(output, 'w') as file:
                pass
            print(f"{GREEN}[✔] CSV file cleared successfully !")
            sleep(0.8)
        else:
            print(f"{RED}[✘] Unable to locate csv file.")
            sleep(0.8)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(1)
        print(f"{GREEN}[+] Thank you for using Hermes 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()
    
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Hermes 😁")
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
        sleep(1)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if number == 1:
        clear()
        main(username, session, code)
    else:
        clear()
        print(f"{RED}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        sys.exit()
try:
    if __name__ == '__main__':
        sleep(2)
        clear()
        parser = argparse.ArgumentParser(description='Hermes is a python script which analyzes a post and categorises its likers.')
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-p', '--code', help='The shortcode of the post to use. For exampe >> /Hermes/Photos/short_code_example.png')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 hermes.py -u <your_username> -p <posts_shortcode> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.code=input(f"{YELLOW}[::] Please enter the post's shortcode >>> ") if not args.code else args.code
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'), args.code.strip())
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()
