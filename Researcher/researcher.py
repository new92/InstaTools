# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Researcher is a python script designed to retrieve the possible location of a part of followers from an Instagram user.

For output example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Researcher.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Researcher requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3 : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Researcher ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'csv', 'argparse', 'prettytable')
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
    import csv
    import argparse
    from colorama import init, Fore
    from prettytable import PrettyTable
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Researcher have been installed !")
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
YELLOW = Fore.LIGHTYELLOW_EX
RED = Fore.RED
CYAN = Fore.LIGHTBLUE_EX

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

ANS = ('yes', 'no')
EMPTY = ('', ' ')

def filter(spaces: list, followers: list, bios: list) -> tuple:
    space_followers = []
    if spaces:
        followers.extend([''] * (len(spaces) - len(followers)))
        bios.extend([''] * (len(spaces) - len(bios)))
        COUNTERS = [spaces.count(space) for space in spaces]
        index = COUNTERS.index(max(COUNTERS))
        sum_ = sum(COUNTERS)
        appear = [(str(round(float(COUNTERS[i]) / sum_, 3)) + '%') for i in range(len(COUNTERS))]
        for i in range(len(spaces)):
            if spaces[index] in bios[i] and followers[i] not in space_followers:
                space_followers.append(followers[i])
        return spaces[index], appear, appear[index], space_followers
    else:
        return '', [], '', []

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
    return f"{GREEN}[✔] Files and dependencies removed successfully !"

output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Researcher.csv')).replace('\\', '/')

def banner():
    console.print("""[bold green]
.______       _______     _______. _______     ___      .______        ______  __    __   _______ .______      
|   _  \     |   ____|   /       ||   ____|   /   \     |   _  \      /      ||  |  |  | |   ____||   _  \     
|  |_)  |    |  |__     |   (----`|  |__     /  ^  \    |  |_)  |    |  ,----'|  |__|  | |  |__   |  |_)  |    
|      /     |   __|     \   \    |   __|   /  /_\  \   |      /     |  |     |   __   | |   __|  |      /     
|  |\  \----.|  |____.----)   |   |  |____ /  _____  \  |  |\  \----.|  `----.|  |  |  | |  |____ |  |\  \----.
| _| `._____||_______|_______/    |_______/__/     \__\ | _| `._____| \______||__|  |__| |_______|| _| `._____|
[/]""", justify='center')

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
    console.print("[bold yellow][+] Researcher is a python script for retrieving the possible location of the followers of a user on Instagram.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate Researcher[/]")
    console.print("[bold yellow][2] Show Reseacher's info[/]")
    console.print("[bold yellow][3] Clear log file[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    op=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while op not in range(1,6):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers >>> [1-5]")
        sleep(0.9)
        op=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if op == 1:
        clear()
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(0.9)
        keep=input(f"{YELLOW}[::] Keep log ? ").strip().lower()
        while keep not in ANS or keep in EMPTY:
            print(f"{RED}[✘] Invalid answer !")
            sleep(0.6)
            keep=input(f"{YELLOW}[::] Keep log ? ").strip().lower()
        keep = keep == ANS[0]
        name = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ResearcherLog.txt')).replace('\\', '/')
        loader = instaloader.Instaloader()
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
                print(f"{YELLOW}[2] Uninstall Researcher and exit")
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
                    print(f"{GREEN}[+] Thank you for using Researcher 🫡")
                    sleep(2)
                    print(f"{GREEN}[+] Until we meet again 👋")
                    sleep(1)
                    sys.exit()
        sleep(0.8)
        clear()
        sleep(0.5)
        print(f"{CYAN}[*] Using session file >>> {session}...")
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
        print(f"{CYAN}[*] Loading profile...")
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
                sleep(0.8)
                sys.exit()
        if profile:
            sleep(1)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.85)
            clear()
            print(f"{CYAN}[*] Extracting followers...")
            sleep(0.5)
            with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/countries.txt')).replace('\\', '/'), 'r', encoding='utf-8') as countriez:
                COUNTRIES = [country.replace('\n', '') for country in countriez]
            with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files/cities.txt')).replace('\\', '/'), 'r', encoding='utf-8') as citiez:
                CITIES = [city.replace('\n', '') for city in citiez]
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
            print(f"{GREEN}[✔] Success ! Extracted {len(FOLLOWERS)} followers from {username}.")
            sleep(1.5)
            clear()
            sleep(0.6)
            print(f"{CYAN}[*] Categorizing followers...")
            sleep(0.6)
            followers, cities, countries, bios = [], [], [], []
            for i in range(len(FOLLOWERS)):
                profile = instaloader.Profile.from_username(loader.context, FOLLOWERS[i])
                bio = str(profile.biography).lower().split(' ')
                for city in CITIES:
                    if city in bio:
                        if profile.username not in followers:
                            followers.append(profile.username)
                        cities.append(city)
                        if ' '.join(bio) not in bios:
                            bios.append(' '.join(bio))
                for country in COUNTRIES:
                    country = country.split(' ')
                    if country[0] in bio or country[1] in bio or country[2] in bio:
                        if profile.username not in followers:
                            followers.append(profile.username)
                        countries.append(country[1])
                        if ' '.join(bio) not in bios:
                            bios.append(' '.join(bio))
            sleep(0.5)
            print(f"{GREEN}[✔] Successfully splitted followers into categories !")
            sleep(0.4)
            table = PrettyTable()
            print(f"{CYAN}[*] Filtering results...")
            sleep(0.5)
            country, country_appear, country_rate, country_followers = filter(countries, followers, bios)
            city, city_appear, city_rate, city_followers = filter(cities, followers, bios)
            country_followers.extend([''] * (len(followers) - len(country_followers)))
            city_followers.extend([''] * (len(followers) - len(city_followers)))
            countries.extend([''] * (len(followers) - len(countries)))
            cities.extend([''] * (len(followers) - len(cities)))
            country_appear.extend([''] * (len(followers) - len(country_appear)))
            city_appear.extend([''] * (len(followers) - len(city_appear)))
            table.field_names = ['Followers', 'Countries', 'Cities', 
                                 'Appearance rate for each country',
                                 'Appearance rate for each city',
                                 'Followers in the most appeared country',
                                 'Followers in the most appeared city']
            for i in range(len(followers)):
                table.add_row(row=[followers[i], countries[i], cities[i], country_appear[i], city_appear[i], country_followers[i], city_followers[i]])
            sleep(0.4)
            print(f"{GREEN}[✔] Filtering successfull.")
            sleep(0.4)
            clear()
            sleep(0.4)
            print(f"\n\n{YELLOW}{table}")
            sleep(2)
            print(f'{CYAN}[-] Additional data:')
            sleep(0.2)
            print(f"{CYAN}[>] Most appeared city >>> {city}", f"{CYAN}[>] Most appeared country >>> {country}", f"{CYAN}[>] Most appeared city's appearance rate >>> {city_rate}", f"{CYAN}[>] Most appeared country's appearance rate >>> {country_rate}", sep="\n")
            if keep:
                print(f"{YELLOW}\n[+] Writing output to log file...")
                sleep(0.8)
                with open(name, 'a', encoding='utf-8') as f:
                    f.write(f'\n\n{str(table)}')
                sleep(1)
                print(f"{GREEN}[✔] Results written to text file.")
                sleep(0.4)
                print(f"{GREEN}[↪] Name >>> {name}", f"{GREEN}[↪] Path >>> {name}", f"{GREEN}[↪] Size >>> {os.stat(name).st_size} bytes", sep="\n")
                sleep(2)
        print(f"{CYAN}[*] Writing output to CSV file...")
        sleep(0.4)
        L = [
            ['Followers', 'Countries', 'Cities', 
            'Appearance rate for each country',
            'Appearance rate for each city',
            'Followers in the most appeared country',
            'Followers in the most appeared city'],
        ]    
        for i in range(len(followers)):
            L.append([followers[i], countries[i], cities[i], country_appear[i], city_appear[i], country_followers[i], city_followers[i]])
        with open(output, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(L)
        sleep(0.9)
        print(f"{GREEN}[✔] Done. Path >>> {output}.")

    elif op == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif op == 3:
        clear()
        if os.path.exists(name):
            with open(name, 'w', encoding='utf-8') as f:
                pass
            print(f"{GREEN}[✔] Successfully cleared log !")
            sleep(0.6)
            print(f"{GREEN}[↪] Name >>> ResearcherLog.txt", f"{GREEN}[↪] Location >>> {name}", f"{GREEN}[↪] Size >>> 0 bytes", sep="\n")
            sleep(1)
        else:
            clear()
            print(f"{RED}[✘] Log file not found !")
            sleep(0.8)
            print(f"{YELLOW}[+] Searched log file using name >>> ResearcherLog.txt")
            sleep(0.8)
            print(f"{GREEN}[*] Please first create the log file and then use this option 😀")
            sleep(1)
            print(f"""{YELLOW}[+] Instructions: 
            1) Return to menu and enter the option number 1
            2) Enter <yes> in the keep log question
            """)
            sleep(3)

    elif op == 4:
        clear()
        print(Uninstall())
        sleep(1)
        print(f"{GREEN}[+] Thank you for using Researcher 😁")
        sleep(1)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Researcher 😁")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
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
        print(f"{RED}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(2)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Researcher is a python script designed to retrieve the location of the followers of a user on Instagram.')
        parser.add_argument('-u', '--username', help='Your username on Instagram.')
        parser.add_argument('-t', '--target', help='The target username.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >>> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 researcher.py -u <username> -t <target_username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.target=input(f"{YELLOW}[::] Please enter the target username >>> ") if not args.target else args.target
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.target.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()