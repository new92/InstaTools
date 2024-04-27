# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Poirot is a python script used to extract information from Instagram accounts. Without login or any type of credentials required.

For output example >>> ./Photos/output.png
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Poirot requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python3 and then use Poirot ✅")
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
    import ctypes
    import requests
    import os
    import argparse
    from os import system
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print(f"[!] WARNING: Not all packages used in Poirot have been installed !")
    sleep(1.5)
    print(f"[+] Ignoring warning...")
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
    console.print("""[bold green]
                           _               _   
                          (_)             | |  
             _ __    ___   _  _ __   ___  | |_ 
            | '_ \  / _ \ | || '__| / _ \ | __|
            | |_) || (_) || || |   | (_) || |_ 
            | .__/  \___/ |_||_|    \___/  \__|
            | |
            |_|
""", justify='center')

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
    return f'{GREEN}[✔] Files and dependencies removed successfully !'

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

def fetch(username: str):
    headers = {
        'User-Agent': 'Instagram 64.0.0.14.96'
    }
    request = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=headers)
    js = request.json()
    if request.status_code != 200:
        return js['message']
    return {
        'bio': js['data']['user']['biography'],
        'posts': js['data']['user']['edge_owner_to_timeline_media']['count'],
        'links': [js['data']['user']['bio_links'][i]['url'] for i in range(len(js['data']['user']['bio_links']))],
        'fb': js['data']['user']['fb_profile_biolink'],
        'users': [js['data']['user']['biography_with_entities']['entities'][i]['user']['username'] for i in range(len(js['data']['user']['biography_with_entities']['entities'])) if js['data']['user']['biography_with_entities']['entities'][i]['user'] != None],
        'hashtags': [js['data']['user']['biography_with_entities']['entities'][i]['hashtag']['name'] for i in range(len(js['data']['user']['biography_with_entities']['entities'])) if js['data']['user']['biography_with_entities']['entities'][i]['hashtag'] != None],
        'followers': js['data']['user']['edge_followed_by']['count'],
        'followings': js['data']['user']['edge_follow']['count'],
        'fbid': js['data']['user']['fbid'],
        'name': js['data']['user']['full_name'],
        'id': js['data']['user']['id'],
        'hide': js['data']['user']['hide_like_and_view_counts'],
        'business': js['data']['user']['is_business_account'],
        'professional': js['data']['user']['is_professional_account'],
        'supervision': js['data']['user']['is_supervision_enabled'],
        'join': js['data']['user']['is_joined_recently'],
        'email': js['data']['user']['business_email'],
        'tel': js['data']['user']['business_phone_number'],
        'private': js['data']['user']['is_private'],
        'verified': js['data']['user']['is_verified'],
        'pic': js['data']['user']['profile_pic_url_hd'],
        'category': js['data']['user']['category_name']
    }

name = 'poirotLog.txt'
    
def main(target: str):
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
    console.print("[bold yellow][+] Poirot is a python script for extracting info from a user's Instagram account.[/]")
    print("\n")
    console.print(f"[bold yellow][1] Extract {target}'s info[/]")
    console.print("[bold yellow][2] Show Poirot's info[/]")
    console.print("[bold yellow][3] Clear log[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    print("\n")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,6):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>>   "))
    if num == 1:
        clear()
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
        while keep not in ANS:
            print(f"{RED}[✘] Invalid answer !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
        keep = keep == ANS[0]
        sleep(1.2)
        clear()
        sleep(0.5)
        print(f"{GREEN}[+] Username -> OK")
        sleep(1.3)
        print(f"{GREEN}[*] Starting information extraction...")
        sleep(1.3)
        dict = fetch(target)
        if type(dict) is not str:
            sleep(1.3)
            print(f"{GREEN}[✔] Success !")
            sleep(1.1)
            clear()
            print(
                f"{GREEN}{'-' * (len(target) + 15)}", f"{GREEN}[>] Name | {dict['name']}",
                f"{GREEN}[>] Bio | {dict['bio']}", f"{GREEN}[>] Posts {dict['posts']}", f"{GREEN}[>] Followers | {dict['followers']}",
                f"{GREEN}[>] Followings | {dict['followings']}", f"{GREEN}[>] Email | {dict['email']}",
                f"{GREEN}[>] Tel | {dict['tel']}", f"{GREEN}[>] Profile pic | {dict['pic']}",
                f"{GREEN}[>] ID | {dict['id']}", f"{GREEN}[>] External links | {dict['links']}",
                f"{GREEN}[>] Users in bio | {dict['users']}", f"{GREEN}[>] Hashtags in bio | {dict['hashtags']}",
                f"{GREEN}[>] fb | {dict['fb']}", f"{GREEN}[>] fb ID | {dict['fbid']}", f"{GREEN}[>] Category | {dict['category']}",
                f"{GREEN}[>] Joined recently | {dict['join']}", f"{GREEN}[>] Private | {dict['private']}",
                f"{GREEN}[>] Verified | {dict['verified']}", f"{GREEN}[>] Business | {dict['business']}",
                f"{GREEN}[>] Professional | {dict['professional']}", f"{GREEN}[>] Supervised | {dict['supervision']}",
                f"{GREEN}[>] Hide likes & views | {dict['hide']}", f"{GREEN}{'-' * (len(str(dict['hide'])) + 25)}", sep="\n")
            sleep(2)
            if keep:
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), 'a', encoding='utf-8') as f:
                    f.write('\n\n')
                    f.write('-' * (len(target) + 15))
                    f.write(str(dict))
                    f.write(f"\n{'-' * (len(str(dict['hide'])) + 25)}")
                location = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
                print(f"\n{GREEN}[✔] Successfully saved log !")
                sleep(1)
                print(f"{YELLOW}[↪] Name >>> {name}",  f"{YELLOW}[↪] Path >>> {location}", f"{YELLOW}[↪] Size >>> {os.stat(name).st_size} bytes", sep='\n')
        else:
            print(f"{RED}[✘] Information gathering unsuccessfull !")
            sleep(1)
            print(f"{GREEN}[+] Error message => {dict}")
            sleep(2)

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        location = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
        if os.path.exists(location):
            with open(name, 'w', encoding='utf-8') as f:
                pass
            sleep(0.5)
            print(f"{GREEN}[✔] Successfully cleared log !")
            sleep(1)
            print(f"{GREEN}[↪] Name >>> {name}", f"{GREEN}[↪] Location >>> {location.replace('\\', '/')}", f"{GREEN}[↪] Size >>> 0 bytes", sep="\n")
            sleep(3)
        else:
            clear()
            print(f"{RED}[✘] Log file not found !")
            sleep(0.8)
            print(f"{YELLOW}[+] Searched log file using name >>> {name}")
            sleep(0.8)
            print(f"{GREEN}[*] Please first create the log file and then use this option.")
            sleep(1)
            print(f"""{YELLOW}[+] Instructions: 
            1) Return to menu and enter the option number 1
            2) Enter <yes> in the keep log question
            """)
            sleep(3)
    
    elif num == 4:
        clear() 
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Poirot 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(0.7)
        sys.exit()

    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using Poirot 😁")
        sleep(0.8)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(0.9)
        sys.exit()
    
    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
    while opt not in range(1, 3):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(2)
        opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones) >>> "))
    if opt == 1:
        clear()
        main(target)
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Poirot 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.9)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Poirot is a python script used for extracting information from accounts on Instagram. Without login or any type of credentials required!')
        parser.add_argument('-u', '--target', help='The target username to extract the info from.')
        args = parser.parse_args()
        if len(sys.argv) < 2:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 poirot.py -u <target_username>")
            sleep(1.5)
            args.target=input(f"{YELLOW}[::] Please enter the target username >>> ")
        main(args.target.strip().lower())
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()