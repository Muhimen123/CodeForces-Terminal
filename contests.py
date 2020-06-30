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

    def standings(start=1, count=20, unofficial=True):
        print(colorama.Fore.BLUE + "Enter the contest id: " + colorama.Fore.RESET, end="")
        contest_id = input()
        URL = f'https://codeforces.com/api/contest.standings?contestId={contest_id}&from={start}&count={count}&showUnofficial={unofficial}'
        try:
            response = requests.get(URL)
            if response.status_code != 200:
                print(colorama.Fore.RED + "Sorry, we recieved a " + colorama.Fore.RESET, end='')
                print(f"{colorama.Back.RED}{colorama.Fore.WHITE} {response.status_code} {colorama.Style.RESET_ALL}",end='')
                print(colorama.Fore.RED, "response code from CODEFORCES. 😟", colorama.Fore.RESET)

            else:
                data = json.loads(response.text)
                data = data['result']
                problems = data['problems']
                standings = data['rows']

                table_headers = ['#', 'HANDLE', 'POINTS', 'PENALTY']
                table_rows = []

                # Getting all the problems ID
                for problem in problems:
                    table_headers.append(problem['index'])

                for contestant in standings:
                    handle = contestant['party']['members'][0]['handle']
                    rank = contestant['rank']
                    points = contestant['points']
                    penalty = contestant['penalty']

                    solved_problems = []

                    for solved in contestant['problemResults']:
                        solved_prob = solved['points']
                        wrong_sub = solved['rejectedAttemptCount']

                        if wrong_sub != 0:
                            wrong_sub = '-' + str(wrong_sub)

                        add_data = f"{solved_prob} ({wrong_sub})"

                        solved_problems.append(add_data)

                    table_rows.append([rank, handle, points, penalty] + solved_problems)

                print(colorama.Fore.GREEN)
                table = tabulate(table_rows, headers=table_headers)
                print(table)
                print(colorama.Fore.RESET)

        except Exception as error:
            print(error)

    if 'true' in raw_cmd:
        answers = con_questions.contest_standing_qus()
        standings(start=answers['start'], count=answers['count'], unofficial=answers['unofficial'])

    else:
        standings()


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
            header = ['Index', 'Name', 'Tags', 'Ratings']
            rows = []
            for i in range(len(problems)):
                idx = problems[i]['index']
                name = problems[i]['name']
                tags = problems[i]['tags']

                try:
                    points = problems[i]['rating']
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

