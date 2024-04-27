# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Sphinx is a python tool designed to find and extract the offensive comments from an instagram post.

For short code example >>> ./Photos/short_code_example.png

For analysis example >>> ./Photos/output.png

For users categorization example >>> ./Photos/data.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored !
Will be used only for the purpose of Sphinx.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Sphinx requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python3 and then use Sphinx ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    import platform
    from os import system
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'csv', 'argparse', 'tabulate')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import instaloader
    import csv
    import logging
    import requests
    import argparse
    import os
    import ctypes
    from tabulate import tabulate
    from colorama import init, Fore
except (ImportError or ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Sphinx have been installed !")
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

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

ANS = ('yes', 'no')
EMPTY = ('', ' ')

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

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
    console.print(r"""[bold green]
             _      _
            | |    (_)
 ___  _ __  | |__   _  _ __  __  __
/ __|| '_ \ | '_ \ | || '_ \ \ \/ /
\__ \| |_) || | | || || | | | >  < 
|___/| .__/ |_| |_||_||_| |_|/_/\_\
     | |
     |_|
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

def filter(COMS, COMES):
    if COMS and COMES:
        COUNTERS = [COMS.count(COMS[i]) for i in range(len(COMS))]
        most_appeared_comment = COMS.index(max(COUNTERS))
        sum_ = sum(COUNTERS)
        return most_appeared_comment, [COMES[i] for i in range(len(COMES)) if COMS[i] == most_appeared_comment], [(str(round(float(COUNTERS[i]) / sum_, 3)) + '%') for i in range(len(COUNTERS))], str(round(float(max(COUNTERS) / sum_))) + '%'
    return '', [], [], ''

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sphinx.csv')).replace('\\', '/')

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
    console.print("[bold yellow][+] Sphinx is a python tool designed to find and extract the offensive comments from an instagram post.[/]")
    print("\n")
    console.print("[bold yellow][1] Analyze comments[/]")
    console.print("[bold yellow][2] Show Sphinx's info[/]")
    console.print("[bold yellow][3] Uninstall InstaTools[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,5):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            sleep(0.5)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            while con not in ANS:
                print(f"{RED}[✘] Invalid answer !")
                sleep(0.8)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            if con == ANS[0]:
                logging.basicConfig(
                    filename='consent.txt',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%d-%m-%Y | %H:%M:%S'
                )
                logging.info(f'Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to {username}.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall Sphinx and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Sphinx and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                        valErr = num in (1,2)
                    except ValueError:
                        print(f"{RED}[✘] Please enter a valid number.")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    sys.exit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Thank you for using Sphinx 🫡")
                    sleep(1)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(1)
                    sys.exit()
        sleep(2)
        clear()
        if session:
            print(f"{CYAN}[*] Using session file >>> {session}...")
            sleep(1.3)
            try:
                with open(session, 'rb') as sessionfile:
                    loader.context.load_session_from_file(username, sessionfile)
            except instaloader.exceptions.ConnectionException as ex:
                print(f"{RED}[✘] Error loading session file !")
                sleep(1)
                print(f"{YELLOW}[+] Error message >>> {ex}")
                sleep(2)
                print(f"{RED}[+] Exiting...")
                sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(1.4)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.9)
        print(f"{CYAN}[*] Loading shortcodes from file...")
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shortcodes.txt'), 'r', encoding='utf-8') as codes:
            codes = [code.strip().replace('\n', '') for code in codes]
        sleep(0.7)
        print(f"{GREEN}[✔] Loaded {len(codes)} shortcodes successfully !")
        sleep(0.9)
        clear()
        sleep(0.7)
        print(f"{CYAN}[*] Analyzing posts....")
        sleep(0.7)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'profanity.txt'), 'r', encoding='utf-8') as prof:
            PROF = [line.replace('\n', '') for line in prof]
        COMES, COMS, DUPS = [], [], []
        for code in codes:
            post = instaloader.Post.from_shortcode(loader.context, code)
            for comment in post.get_comments():
                text = comment.text.strip().lower().split(' ')
                for prof in PROF:
                    if prof in text:
                        if text in COMS:
                            DUPS.append(text)
                        if comment.owner.username not in COMES:
                            COMES.append(comment.owner.username)
                        COMS.append(' '.join(text))
        sleep(0.5)
        if COMS:
            COMES.extend([''] * (len(COMS) - len(COMES)))
            print(f"{GREEN}[✔] Success. Exctracted {len(COMS)} offensive comments & {len(COMES)} offensive commenters from {len(codes)} post.")
            sleep(1.2)
            clear()
            print(f"{CYAN}[*] Splitting the extracted users into categories...")
            sleep(0.8)
            PRIVS, PUBS, VERS, FOLS, FOLLS = [], [], [], [], []
            for i in range(len(COMES)):
                if COMES[i]:
                    profile = instaloader.Profile.from_username(loader.context, COMES[i])
                    VERS.append(COMES[i]) if profile.is_verified else PRIVS.append(COMES[i]) if profile.is_private else PUBS.append(COMES[i])
                    FOLS.append(profile.followers)
                    FOLLS.append(profile.followees)
            privs = len(PRIVS)
            pubs = len(PUBS)
            vers = len(VERS)
            fols = sum(FOLS)
            folls = sum(FOLLS)
            PRIVS.extend([''] * (len(COMS) - len(PRIVS)))
            PUBS.extend([''] * (len(COMS) - len(PUBS)))
            VERS.extend([''] * (len(COMS) - len(VERS)))
            FOLS.extend([''] * (len(COMS) - len(FOLS)))
            FOLLS.extend([''] * (len(COMS) - len(FOLLS)))
            sleep(0.4)
            print(f'{GREEN}[✔] Done.')
            sleep(0.5)
            print(f'{CYAN}[*] Writing data to data.txt...')
            sleep(0.4)
            data = [[PRIVS[i], PUBS[i], VERS[i], FOLS[i], FOLLS[i]] for i in range(len(COMS))]
            table = tabulate(data, headers=['Privates', 'Publics', 'Verified', 'Followers', 'Followings'])
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt'), 'w', encoding='utf-8') as f:
                f.write(str(table))
            sleep(0.5)
            print(f"{GREEN}[✔] Success.")
            sleep(0.5)
            print(f"{CYAN}[*] Writing offensive comments & commenters to Sphinx.txt...")
            sleep(0.3)
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sphinx.txt'), 'w', encoding='utf-8') as f:
                f.write('Offensive comments\t\t\tOffensive commenters\n' + '-' * 50)
                for i in range(len(COMS)):
                    f.write(f"{str(COMS[i])} -> {str(COMES[i])}\n")
            sleep(0.5)
            print(f"{GREEN}[✔] Success. Structure of Sphinx.txt: comment -> commenter")
            sleep(1.5)
            print(f"{YELLOW}[+] Total offensive comments >>> {len(COMS)}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total offensive commenters >>> {len(COMES)}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total privates >>> {privs}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total publics >>> {pubs}")
            sleep(0.4)
            print(f"{YELLOW}[+] Total verified >>> {vers}")
            sleep(0.5)
            print(f"{YELLOW}[+] Total followers >>> {fols}")
            sleep(0.5)
            print(f"{YELLOW}[+] Total followees >>> {folls}")
            sleep(3)
            clear()
            sleep(0.5)
            print(table)
            sleep(5)
            print(f"{CYAN}[*] Writing output to CSV file...")
            sleep(0.6)
            L = [
                ['Total offensive comments', 'Total offensive commenters', 'Total privates', 'Total publics', 'Total verified', 'Total followers', 'Total followings'],
                [len(COMS), len(COMES), privs, pubs, vers, fols, folls],
                ['Offensive comments', 'Offensive Commenters', 'Privates', 'Publics', 'Verified', 'Followers', 'Followings']
            ]
            for i in range(len(COMS)):
                L.append([COMS[i], COMES[i], PRIVS[i], PUBS[i], VERS[i], FOLS[i], FOLLS[i]])
            with open(output, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(L)
            sleep(1)
            print("\n")
            print(f"{GREEN}[✔] Successfully saved data at >>> {output}")
        else:
            print(f"{RED}[✘] Sphinx was unable to extract offensive comments from the given posts !")
            sleep(0.7)

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Sphinx 😁")
        sleep(1)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(0.8)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Sphinx 😁")
        sleep(1)
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
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        print(f"{RED}[+] Exiting...")
        sleep(0.4)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Sphinx is a python tool designed to find and extract the offensive comments from an instagram post.')
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 3:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 sphinx.py -u <username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()