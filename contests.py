import requests
import colorama
import json
from tabulate import tabulate
from datetime import datetime, timedelta
from questions import con_questions
import error_msg

colorama.init()

def contest_list(raw_cmd, adv=False):
    colorama.init()
    URL = 'https://codeforces.com/api/contest.list?'

    if 'true' in raw_cmd:
        answer = con_questions.contest_main_qus()
        if answer['sort_by'].lower() == 'by_phases':
            answer2 = con_questions.contest_phase_qus()
        elif answer['sort_by'].lower() == 'by_divs':
            answer2 = con_questions.contest_div_qus()
        else:
            answer2 = {'ans': 'Null'}

        if answer2['ans'] == 'Null':
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

                    if int(answer['contest_numbers']) > len(contests_data):
                        answer['contest_numbers'] = len(contests_data)
                    else:
                        answer['contest_numbers'] = int(answer['contest_numbers'])

                    for i in range(answer['contest_numbers']):
                        ids = contests_data[i]['id']
                        name = contests_data[i]['name']
                        types = contests_data[i]['type']
                        phase = contests_data[i]['phase']
                        starttime = contests_data[i]['startTimeSeconds']
                        duration = contests_data[i]['durationSeconds']

                        if len(name) > 50:
                            name = name[:47] + '...'

                        starttime =  datetime.fromtimestamp(int(starttime))
                        starttime = starttime.strftime("%Y-%m-%d  %H:%M")

                        duration = timedelta(seconds=int(duration))

                        row = [ids, name, types, phase, starttime, duration]
                        table_data.append(row)

                    table = tabulate(table_data, headers=headers, tablefmt='github')
                    print(colorama.Fore.GREEN + table + colorama.Fore.RESET)

            except Exception:
                error_msg.error()

        elif answer['sort_by'].lower() == 'by_divs':
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

                    if int(answer['contest_numbers']) > len(contests_data):
                        answer['contest_numbers'] = len(contests_data)
                    else:
                        answer['contest_numbers'] = int(answer['contest_numbers'])

                    contest_div_match = 0

                    for i in range(len(contests_data)):
                        if contest_div_match == answer['contest_numbers']:
                            break

                        if answer2['ans'].lower() in contests_data[i]['name'].lower():
                            contest_div_match += 1

                            ids = contests_data[i]['id']
                            name = contests_data[i]['name']
                            types = contests_data[i]['type']
                            phase = contests_data[i]['phase']
                            starttime = contests_data[i]['startTimeSeconds']
                            duration = contests_data[i]['durationSeconds']

                            if len(name) > 50:
                                name = name[:47] + '...'

                            starttime =  datetime.fromtimestamp(int(starttime))
                            starttime = starttime.strftime("%Y-%m-%d  %H:%M")

                            duration = timedelta(seconds=int(duration))

                            row = [ids, name, types, phase, starttime, duration]
                            table_data.append(row)
                        else:
                            pass

                    table = tabulate(table_data, headers=headers, tablefmt='github')
                    print(colorama.Fore.GREEN + table + colorama.Fore.RESET)

            except Exception:
                error_msg.error()

        elif answer['sort_by'].lower() == 'by_phases':
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

                    if int(answer['contest_numbers']) > len(contests_data):
                        answer['contest_numbers'] = len(contests_data)
                    else:
                        answer['contest_numbers'] = int(answer['contest_numbers'])

                    contest_div_match = 0

                    for i in range(len(contests_data)):
                        if contest_div_match == answer['contest_numbers']:
                            break

                        if answer2['ans'].lower() in contests_data[i]['phase'].lower():
                            contest_div_match += 1

                            ids = contests_data[i]['id']
                            name = contests_data[i]['name']
                            types = contests_data[i]['type']
                            phase = contests_data[i]['phase']
                            starttime = contests_data[i]['startTimeSeconds']
                            duration = contests_data[i]['durationSeconds']

                            if len(name) > 50:
                                name = name[:47] + '...'

                            starttime =  datetime.fromtimestamp(int(starttime))
                            starttime = starttime.strftime("%Y-%m-%d  %H:%M")

                            duration = timedelta(seconds=int(duration))

                            row = [ids, name, types, phase, starttime, duration]
                            table_data.append(row)
                        else:
                            pass

                    table = tabulate(table_data, headers=headers, tablefmt='github')
                    print(colorama.Fore.GREEN + table + colorama.Fore.RESET)

            except Exception:
                error_msg.error()

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

                    if len(name) > 50:
                        name = name[:47] + '...'

                    starttime =  datetime.fromtimestamp(int(starttime))
                    starttime = starttime.strftime("%Y-%m-%d  %H:%M")

                    duration = timedelta(seconds=int(duration))

                    row = [ids, name, types, phase, starttime, duration]
                    table_data.append(row)

                table = tabulate(table_data, headers=headers, tablefmt='github')
                print(colorama.Fore.GREEN + table + colorama.Fore.RESET)

        except Exception:
                error_msg.error()

    print(colorama.Style.RESET_ALL)


def contest_standings(raw_cmd, adv=False):
    pass


def contest_ratings_change(raw_cmd, adv=False):
    pass


def contest_problems():
    print(f'{colorama.Fore.BLUE}Enter the contest id: {colorama.Fore.RESET}', end="")
    contest_id = input()
    URL = f'https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=1&showUnofficial=true'
    try:
        res  = requests.get(URL)
        if res.status_code != 200:
            print(colorama.Fore.RED + "Sorry, we recieved a " + colorama.Fore.RESET, end='')
            print(f"{colorama.Back.RED}{colorama.Fore.WHITE} {res.status_code} {colorama.Style.RESET_ALL}", end='')
            print(colorama.Fore.RED, "response code from CODEFORCES. 😟", colorama.Fore.RESET)
        else:
            data = json.loads(res.text)
            problems = data['result']['problems']
            header = ['Index', 'Name', 'Tags', 'Points']
            rows = []
            for i in range(len(problems)):
                idx = problems[i]['index']
                name = problems[i]['name']
                tags = problems[i]['tags']

                try:
                    points = problems[i]['points']
                except:
                    points = colorama.Fore.RED + 'NaN' + colorama.Fore.RESET + colorama.Fore.LIGHTBLUE_EX

                if len(tags) > 3:
                    tags = tags[:3]
                    tags.append('...')

                rows.append([idx, name, tags, points])

            table = tabulate(rows, headers=header, tablefmt='github')

            print(colorama.Fore.LIGHTBLUE_EX)
            print(table)
            print(colorama.Fore.RESET)

    except:
        error_msg.error()