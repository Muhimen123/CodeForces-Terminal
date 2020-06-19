import requests
import colorama
import json
from tabulate import tabulate
from datetime import datetime, timedelta


def contest_list(raw_cmd, adv=False):
    colorama.init()
    URL = 'https://codeforces.com/api/contest.list?'

    if 'true' in raw_cmd:
        adv = True

    if adv == True:
        print("Prompt for advanced commands")
    else:
        try:
            response = requests.get(URL)
            if response.status_code != 200:
                print(colorama.Fore.RED + "Sorry, we recieved a " + colorama.Fore.RESET, end='')
                print(f"{colorama.Back.RED}{colorama.Fore.WHITE} {response.status_code} {colorama.Style.RESET_ALL}", end='')
                print(colorama.Fore.RED, "response code from CODEFORCES. 😟", colorama.Fore.RESET)
            else:
                data = json.loads(response.text)
                contests_data= data['result']

                table_data = []
                headers = ['ID', 'NAME', 'TYPE', 'PHASE', 'START TIME', 'DURATION']

                for i in range(10):
                    ids = contests_data[i]['id']
                    name = contests_data[i]['name']
                    types = contests_data[i]['type']
                    phase = contests_data[i]['phase']
                    starttime = contests_data[i]['startTimeSeconds']
                    duration = contests_data[i]['durationSeconds']

                    starttime =  datetime.fromtimestamp(int(starttime))
                    starttime = starttime.strftime("%Y-%m-%d  %H:%M")

                    duration = timedelta(seconds=int(duration))

                    row = [ids, name, types, phase, starttime, duration]
                    table_data.append(row)

                table = tabulate(table_data, headers=headers, tablefmt='github')
                print(colorama.Fore.GREEN + table + colorama.Fore.RESET)

        except Exception:
            print(colorama.Fore.RED + "Please check your internet connection and then try", colorama.Fore.RESET)

    print(colorama.Style.RESET_ALL)


def contest_standings(adv=False):
    pass


def contest_ratings_change(adv=False):
    pass


def contest_info(contest_id):
    pass
