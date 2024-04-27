"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

ToolZ is a python script for keeping track on the users which unfollowed a user on Instagram.

For results example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of ToolZ.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! ToolZ requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python3 and then use ToolZ ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'argparse')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import platform
    from os import system
    import os
    import logging
    import instaloader
    import requests
    import ctypes
    import argparse
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in ToolZ have been installed !")
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
console.print("[bold green][✔] Successfully loaded modules.")
sleep(0.8)
clear()

ANS = ('yes', 'no')
EMPTY = ('', ' ')

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
    return f"{GREEN}[✔] Files and dependencies removed successfully !"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

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
    console.print("""[bold green]
         tttt                                            lllllll
      ttt:::t                                            l:::::l
      t:::::t                                            l:::::l
      t:::::t                                            l:::::l
ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l zzzzzzzzzzzzzzzzz
t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l z:::::::::::::::z
t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l z::::::::::::::z 
tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l zzzzzzzz::::::z  
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l       z::::::z   
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l      z::::::z    
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l     z::::::z     
      t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l    z::::::z      
      t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::l  z::::::zzzzzzzz
      tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::l z::::::::::::::z
        tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::lz:::::::::::::::z
          ttttttttttt     ooooooooooo      ooooooooooo   llllllllzzzzzzzzzzzzzzzzz
[/]""", justify='center')

name = 'ToolZLog.txt'

def main(username: str, target: str, session: str):
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
    console.print("[bold yellow][+] ToolZ is a python tool which keeps track on the users who unfollowed a user on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate ToolZ[/]")
    console.print("[bold yellow][2] Display ToolZ's info[/]")
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
                    datefmt='%d-%m-%Y | %H:%M:%S'
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
                        print(f"{RED}[✘] Invalid number.")
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
                    print(f"{YELLOW}[+] Thank you for using ToolZ 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        loader = instaloader.Instaloader()
        sleep(2)
        clear()
        print(f"{CYAN}[*] Loading session file >>> {session}...")
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
        print(f"{CYAN}[*] Loading profile...")
        profile = None
        try:
            profile = instaloader.Profile.from_username(loader.context, target)
        except instaloader.ProfileNotExistsException as ex:
            print(f"{RED}[✘] Profile not found")
            sleep(1)
            print(f"{YELLOW}[+] Error message: {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            sys.exit()
        if profile:
            sleep(0.8)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.8)
            clear()
            sleep(0.8)
            print(f"{GREEN}[*] Acceptable answers >>> {ANS}")
            sleep(1)
            kp=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
            while kp not in ANS:
                print(f"{RED}[✘] Invalid answer !")
                sleep(0.8)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                kp=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
            sleep(0.8)
            print(f"{CYAN}[*] Initiating ToolZ...")
            sleep(0.8)
            clear()
            sleep(0.5)
            INIT, FOLLOWERS = [follower.username for follower in profile.get_followers()], [follower.username for follower in profile.get_followers()]
            while len(INIT) == len(FOLLOWERS):
                FOLLOWERS = [follower.username for follower in profile.get_followers()]
                print(f"{CYAN}[*] Checking for unfollowers...")
                sleep(0.9)
                print(f"{CYAN}[*] No unfollowers found yet...")
                sleep(0.9)
                print(f"{CYAN}[*] Sleeping for 1 minute before checking again...")
                sleep(60)
                print("\n")
            UNFOLLOWERS = [unfollower for unfollower in INIT if unfollower not in FOLLOWERS]
            sleep(0.4)
            print(f"{GREEN}[→] ToolZ detected a total of {len(UNFOLLOWERS)} unfollowers\n\n")
            sleep(0.7)
            print(f'{YELLOW}|--------|UNFOLLOWERS|--------|')
            sleep(0.75)
            for unfollower in UNFOLLOWERS:
                print(f"{YELLOW}[>] Username >>> {unfollower}")
            if kp == ANS[0]:
                loc = os.path.join(os.path.dirname(os.path.abspath(__file__), name)).replace('\\', '/')
                with open(loc, 'w', encoding='utf-8') as f:
                    f.write(f"[→] ToolZ detected a total of {len(UNFOLLOWERS)} unfollowers\n\n" + "-"*25 + '\n\n')
                    for unfollower in UNFOLLOWERS:
                        f.write(f"[>] Username >>> {unfollower}\n")
                    sleep(1)
                    print(f"{GREEN}[✔] Successfully saved log !")
                    sleep(0.8)
                    print(f"{YELLOW}[↪] Name >>> {name}", f"{YELLOW}[↪] Location >>> {loc}", f"{YELLOW}[↪] Size >>> {os.stat(loc).st_size} bytes", sep='\n')
                    sleep(2)
            
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name).replace('\\', '/'), 'w', encoding='utf-8'):
            pass
        print(f"{GREEN}[✔] Log file cleared successfully !")
        sleep(0.8)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using ToolZ 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 🫡")
        sleep(1)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using ToolZ 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        sys.exit()

    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,3):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{GREEN}[+] Thank you for using ToolZ 😃")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🤗")
        sleep(1)
        print(f"{YELLOW}[+] Exiting...")
        sys.exit()

try:
    if __name__ == '__main__':
        sleep(2)
        clear()
        parser = argparse.ArgumentParser(description='ToolZ is a python script for keeping track on the unfollowers of a user on Instagram.')
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-t', '--target', help='The target username to track its followers.')
        parser.add_argument('-s', '--session', help='The path to the generated session file. To generate it >>> python3 ./cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 toolz.py -u <your_username> -t <target_username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.target=input(f"{YELLOW}[::] Please enter the post's shortcode >>> ") if not args.target else args.target
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.target.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()