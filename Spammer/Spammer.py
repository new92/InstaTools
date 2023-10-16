"""
Author: new92
Contributors: [Itsfizziks, ProgramR4732]
Github: @new92
Leetcode: @new92
PyPI: @new92

Spammer is a python script to spam messages on user(s) on Instagram.

*********DISCLAIMER*********
This script must not, under any circumstances, be designed or utilized in a manner that violates any of Instagram's rules, terms of service, or community guidelines. It is the user's responsibility to ensure compliance with Instagram's policies when using this script. Any misuse or violation of Instagram's rules resulting from the use of this script is the sole responsibility of the user. This script is intended for legitimate and ethical purposes only. Use it responsibly and in full accordance with Instagram's guidelines.
The author (new92) has no responsibility for the user of this script. Please use it responsibly.
****************************
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! Spammer requires Python version 3.X ! ")
        sleep(1)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use Spammer ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'rich', 'platform', 'os', 'json', 'logging', 'instagrapi', 'requests', 'colorama']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import platform
    from os import system
    import instagrapi
    import os
    import json
    import logging
    import requests
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Spammer have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
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
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall Spammer")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt not in range(1,3):
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print(f"[✓] Files and dependencies uninstalled successfully !")
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
console.log("[bold dark_green][✓] Successfully loaded modules.[/]")
sleep(1)
console.clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

ANS = ['yes', 'no']

def ScriptInfo():
    with open('Spammer/config.json') as configFile:
        conf = json.load(configFile)
    f = conf['name'] + '.py'
    fp = fpath(f) == None
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

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def banner() -> str:
    console.log("""[bold yellow]
    ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
    ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
    ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
    ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
    ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
    ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
    [/]""")

def checkUser(username:str) -> bool:
    return username in ['', ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

IDS = []

def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Spammer: A python script to spam messages on someone on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate Spammer[/]")
    console.print("[bold yellow][2] Show Spammer's info[/]")
    console.print("[bold yellow][3] Uninstall Spammer[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num not in range(1,5):
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-4]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        client = instagrapi.Client()
        print(f"{GREEN}[+] Acceptable answers: {ANS}")
        sleep(2)
        con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        while con.lower() not in ANS:
            print(f"{RED}[!] Invalid answer !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers: {ANS}")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        if con.lower() == ANS[0]:
            logging.basicConfig(
                filename='cons.txt',
                level=logging.INFO,
                format='%(asctime)s [%(levelname)s]: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account')
        else:
            print(f"{YELLOW}[OK]")
            sleep(1)
            print(f"{YELLOW}[1] Exit")
            print(f"{YELLOW}[2] Uninstall Researcher and exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            while num not in range(1,3):
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(2)
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(2)
                quit()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] Thank you for using Researcher 🫡")
                sleep(2)
                print(f"{GREEN}[+] Until we meet again 👋")
                sleep(1)
                quit()
        sleep(1)
        clear()
        msg = 'hello world'
        name = 'replies.txt'
        username=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(username):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            username=str(input(f"{YELLOW}[::] Please enter again your username: "))
        while valUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt not in range(1,4):
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(username):
                    print(f"{RED}[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using Spammer 😁")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit()
        username = username.lower().strip()
        password=str(input(f"{YELLOW}[::] Please enter your password: "))
        while password in ['', ' ']:
            print(f"{RED}[!] Invalid password !")
            sleep(1)
            password=str(input(f"{YELLOW}[::] Please enter again your password: "))
        password = password.strip()
        try:
            client.login(username,password)
        except Exception as ex:
            print(f"{RED}[!] Login error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit()
        sleep(1)
        count=int(input(f"{YELLOW}[::] Number of targets: "))
        while count < 1:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            count=int(input(f"{YELLOW}[::] Number of targets: "))
        for i in range(count):
            user=str(input(f"{YELLOW}[::] Please enter the target username: "))
            while checkUser(user) or valUser(user):
                print(f"{RED}[!] Invalid username !")
                sleep(1)
                user=str(input(f"{YELLOW}[::] Please enter again the target username: "))
            user=user.lower().strip()
            IDS.append(requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis').json()["logging_page_id"].strip("profilePage_"))
        inbox = client.direct_inbox(len(IDS))
        items = inbox['inbox']['threads']
        sleep(1)
        print(f"{YELLOW}[+] Default message: {msg}")
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: {ANS}")
        sleep(2)
        change=str(input(f"{YELLOW}[?] Change message ? "))
        while change.lower() not in ANS:
            print(f'{RED}[!] Invalid answer !')
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers: {ANS}")
            sleep(2)
            change=str(input(f"{YELLOW}[?] Change message ? "))
        if change.lower() == ANS[0]:
            sleep(1)
            msg=str(input(f"{YELLOW}[::] Please enter the message: "))
            sleep(2)
        msgs = 0
        sleep(1)
        print(f"{GREEN}[+] To stop enter: <Ctrl + C>")
        sleep(2.5)
        while True:
            client.direct_send(msg,IDS)
            sleep(0.8)
            print("[✓] Message Sent !")
            msgs += 1
        with open(name, 'w', encoding='utf8') as f:
            replies = 0
            for thread in items:
                lst = thread['items'][0]
                if lst['user_id'] != client.user_id:
                    replies += 1
                    f.write(lst['text'] + '\n')
        print(f"{GREEN}[✓] Successfully sent {msgs} to {len(IDS)} targets.")
        sleep(2)
        print(f"{GREEN}[✓] Replies received: {replies}/{msgs}")
        sleep(2)
        print(f"{GREEN}[✓] Successfully saved replies in: {name}")
        sleep(2)
        print(f"{GREEN}[↪] File name >>> {name}")
        print(f"{GREEN}[↪] Path >>> {fpath(name)}")
        print(f"{GREEN}[↪] File size >>> {os.stat(fpath(name)).st_size} bytes")
        sleep(4)
        client.logout()
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)
        print("\n\n")

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🫡")
        sleep(1)
        quit()
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()

    print(f"{YELLOW}[1] Back to menu")
    print(f"{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 2:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{GREEN}[+] Thank you for using Spammer 😃")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🤗")
        sleep(1)
        print(f"{YELLOW}[+] Exiting...")
        quit()

if __name__ == '__main__':
    main()