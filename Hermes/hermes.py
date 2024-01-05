"""
Author: new92
Contributors: [Itsfizziks, ProgramR4732]
Github: @new92
Leetcode: @new92
PyPI: @new92

Hermes is a python script which analyzes and returns data about the likers of a post.

For short code example >>> ./Photos/short_code_example.png

For analysis example >>> ./Photos/Hermes.png
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! Hermes requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Hermes ✅")
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
    mods = ('sys', 'time', 'platform', 'os', 'json', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'csv', 'prettytable')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay[/]')
    import instaloader
    import csv
    import json
    import logging
    import requests
    import os
    from os import system
    from colorama import init, Fore
    from prettytable import PrettyTable
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Hermes have been installed !")
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
                print("[1] Uninstall Hermes")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt not in range(1,3):
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers >>> [1,2]")
                    sleep(1)
                    print("[1] Uninstall Hermes")
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

def ScriptInfo():
    with open(fpath('config.json')) as config:
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

def banner() -> str:
    console.log("""[bold yellow]
                             __ __    ___  ____   ___ ___    ___   _____
                            |  T  T  /  _]|    \ |   T   T  /  _] / ___/
                            |  l  | /  [_ |  D  )| _   _ | /  [_ (   \_ 
                            |  _  |Y    _]|    / |  \_/  |Y    _] \__  T
                            |  |  ||   [_ |    \ |   |   ||   [_  /  \ |
                            |  |  ||     T|  .  Y|   |   ||     T \    |
                            l__j__jl_____jl__j\_jl___j___jl_____j  \___j
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

output = 'Hermes.csv'

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
    console.print("[bold yellow][+] Use Hermes to analyze a post and obtain useful data.[/]")
    print("\n")
    console.print("[bold yellow][1] Analyze post[/]")
    console.print("[bold yellow][2] Show Hermes's info[/]")
    console.print("[bold yellow][3] Uninstall Hermes[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] NUMBER >>> "))
    while num not in range(1,6):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-4]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] NUMBER >>> "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        if not fpath('cons.txt'):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ")
            while con.lower() not in ANS:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
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
                        print(f"{RED}[!] Please enter a valid number.")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
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
                    print(f"{YELLOW}[+] Thank you for using Hermes 🫡")
                    sleep(2)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(1)
                    quit()
        sleep(2)
        clear()
        print(f'{YELLOW}|--------------------LOGIN--------------------|')
        session=input(f"{YELLOW}[::] Cookie file path (<Enter> for default) >>> ")
        if not session:
            username=input(f"{YELLOW}[::] Please enter your username >>> ")
            while checkUser(username):
                if username in EMPTY:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid username !")
                username=input(f"{YELLOW}[::] Please enter your username >>> ")
            username = username.strip().lower()
            while ValUser(username):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                print(f"{YELLOW}[4] Uninstall Hermes and Exit")
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
                    print(f"{GREEN}[+] Thank you for using Hermes 😁")
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
                    print(f"{GREEN}[✓] Session loaded successfully !")
                    sleep(1)
            except instaloader.exceptions.ConnectionException as ex:
                print(f"{RED}[✕] Error loading session file !")
                sleep(1)
                print(f"{YELLOW}[+] Error message >>> {ex}")
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                quit()
        print(f"{GREEN}[✓] Login successfull !")
        sleep(0.85)
        clear()
        code=input(f"{YELLOW}[::] Short post code >>> ")
        while code in EMPTY:
            print(f"{RED}[!] Invalid short code !")
            sleep(0.7)
            print(f"{GREEN}[+] Post short code examples >>> Cz9LceVRZj2, Cz45ApnJLA5, CzwUIGvRa1a")
            sleep(0.5)
            code=input(f"{YELLOW}[::] Short post code >>> ")
        sleep(0.7)
        print(f"{GREEN}[+] Analyzing....")
        sleep(0.5)
        post = instaloader.Post.from_shortcode(loader.context, code)
        likers = post.get_likes()
        LIKERS = [liker.username for liker in likers]
        PUBS = []
        PRIVS = []
        VERS = []
        POSTS = []
        FOLLS = []
        STATUS = []
        for liker in LIKERS:
            profile = instaloader.Profile.from_username(loader.context, liker)
            posts = profile.mediacount
            followers = profile.followers
            if profile.is_private:
                PRIVS.append(liker)
                STATUS.append('boring 🥱')
            else:
                if profile.is_verified:
                    VERS.append(liker)
                else:
                    PUBS.append(liker)
                if (posts > 49 or followers > 7000) or profile.is_verified:
                    STATUS.append('interesting 🤔')
                    continue
                elif posts > 30:
                    STATUS.append('captivating 📸')
                    continue
                elif followers > 4000:
                    STATUS.append('famous 🌍')
                    continue
                else:
                    STATUS.append('ordinary 🤖')
            POSTS.append(posts)
            FOLLS.append(followers)
        PRIVS.extend([''] * (len(likers) - len(PRIVS)))
        PUBS.extend([''] * (len(likers) - len(PUBS)))
        VERS.extend([''] * (len(likers) - len(VERS)))
        table = PrettyTable()
        table.field_names = ['Likers', 'Publics', 'Privates', 'Verified', 'Posts', 'Followers', 'Status']
        for i in range(len(LIKERS)):
            table.add_row(row=[LIKERS[i], PUBS[i], PRIVS[i], VERS[i], POSTS[i], FOLLS[i], STATUS[i]])
        sleep(0.5)
        print(f"{GREEN}[✓] Success.")
        lks = len(LIKERS)
        privs = len(PRIVS)
        vers = len(VERS)
        posts = sum(POSTS)
        folls = sum(FOLLS)
        sleep(0.5)
        print(f"[+] Total likers >>> {lks}")
        sleep(0.4)
        print(f"[+] Total privates >>> {privs}")
        sleep(0.4)
        print(f"[+] Total verified >>> {vers}")
        sleep(0.4)
        print(f"[+] Total posts >>> {posts}")
        sleep(0.4)
        print(f"[+] Total followers >>> {folls}")
        sleep(1.3)
        clear()
        print(table)
        L = [
            ['Total likers', 'Total privates', 'Total verified', 'Total posts', 'Total followers'],
            [lks, privs, vers, posts, folls],
            ['Likers', 'Private', 'Verified', 'Posts', 'Followers', 'Status']
        ]
        for i in range(len(LIKERS)):
            L.append([LIKERS[i], PRIVS[i], VERS[i], POSTS[i], FOLLS[i]])
        with open(output, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(L)
        sleep(5)
        print("\n\n\n")
        print(f"{GREEN}[+] Successfully saved data at >>> ./{output}")

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
        print("\n\n")
    
    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Hermes 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 👋")
        sleep(2)
        quit()
    
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Hermes 😁")
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
