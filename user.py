import requests
import json
import colorama
import error_msg
from datetime import datetime
from tabulate import tabulate



colorama.init()
def get_user_info():
    print(colorama.Fore.BLUE + "Enter a valid user handle: " + colorama.Fore.RESET, end=" ")
    user_handle = input()

    URL = f'https://codeforces.com/api/user.info?handles={user_handle}'

    response = requests.get(URL)
    try:
        if response.status_code != 200:
            print(colorama.Fore.RED + "Sorry, we recieved a " + colorama.Fore.RESET, end='')
            print(f"{colorama.Back.RED}{colorama.Fore.WHITE} {response.status_code} {colorama.Style.RESET_ALL}", end='')
            print(colorama.Fore.RED, "response code from CODEFORCES. 😟", colorama.Fore.RESET)

        else:
            data = json.loads(response.text)
            data = data['result'][0]
            try:
                first_name = data['firstName']
            except:
                first_name = ' '

            try:
                last_name = data['lastName']
            except:
                last_name = ' '

            try:
                country = data['country']
            except:
                country = ' '

            contribution = data['contribution']
            try:
                rank = data['rank']
                max_rank = data['maxRank']
            except:
                rank = 'unrated'
                max_rank = 'unrated'
            try:
                ratings = data['rating']
                max_ratings = data['maxRating']
            except:
                ratings = 0
                max_ratings = 0

            last_online = data['lastOnlineTimeSeconds']
            registration = data['registrationTimeSeconds']
            number_of_friend = data['friendOfCount']

            print('UserName: ', first_name + ' ' + last_name)
            print('Country: ', country)
            print('Contribution: ', contribution)

            if rank == 'unrated':
                print("Current_rank: " + rank)
            elif rank == 'newbie':
                print("Current_rank: " + colorama.Fore.LIGHTBLACK_EX + rank + colorama.Fore.RESET)
            elif rank == 'pupil':
                print("Current_rank: " + colorama.Fore.GREEN + rank + colorama.Fore.RESET)
            elif rank == 'specialist':
                print("Current_rank: " + colorama.Fore.CYAN + rank + colorama.Fore.RESET)
            elif rank == 'expert':
                print("Current_rank: " + colorama.Fore.BLUE + rank + colorama.Fore.RESET)
            elif rank == 'candidate master':
                print("Current_rank: " + colorama.Fore.MAGENTA + rank + colorama.Fore.RESET)
            elif rank == 'master':
                print("Current_rank: " + colorama.Fore.LIGHTYELLOW_EX + rank + colorama.Fore.RESET)
            elif rank == 'international master':
                print("Current_rank: " + colorama.Fore.YELLOW + rank + colorama.Fore.RESET)
            elif rank == 'grandmaster' or rank == 'international grandmaster':
                print("Current_rank: " + colorama.Fore.RED + rank + colorama.Fore.RESET)
            else:
                print("Current_rank: " + colorama.Fore.BLACK + rank[:1] + colorama.Fore.RED + rank[1:] + colorama.Fore.RESET)

            if max_rank == 'unrated':
                print("Max_rank: " + rank)
            elif max_rank == 'newbie':
                print("Max_rank: " + colorama.Fore.LIGHTBLACK_EX  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'pupil':
                print("Max_rank: " + colorama.Fore.GREEN  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'specialist':
                print("Max_rank: " + colorama.Fore.CYAN  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'expert':
                print("Max_rank: " + colorama.Fore.BLUE  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'candidate master':
                print("Max_rank: " + colorama.Fore.MAGENTA  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'master':
                print("Max_rank: " + colorama.Fore.LIGHTYELLOW_EX  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'international master':
                print("Max_rank: " + colorama.Fore.YELLOW  + max_rank + colorama.Fore.RESET)
            elif max_rank == 'grandmaster' or rank == 'international grandmaster':
                print("Max_rank: " + colorama.Fore.RED + max_rank + colorama.Fore.RESET)
            else:
                print("Max_rank: " + colorama.Fore.BLACK  + max_rank[:1] + colorama.Fore.RED + rank[1:] + colorama.Fore.RESET)

            print("Current Ratings:",ratings)
            print("Max Ratings:", max_ratings)

            last_online = datetime.fromtimestamp(last_online)
            last_online = datetime.strftime(last_online, "%Y/%m/%d %H:%M:%S")
            print("Last online: ", last_online)

            registration = datetime.fromtimestamp(registration)
            registration = datetime.strftime(registration, "%Y/%m/%d %H:%M:%S")
            print("Registered: "  + registration)
    except:
        error_msg.error()

def user_subs(raw_cmd):
    def get_sub_history(handle, start=1, count=5):
        URL = f'https://codeforces.com/api/user.status?handle={handle}&from={start}&count={count}'

        try:
            response = requests.get(URL)
            if response.status_code != 200:
                print(colorama.Fore.RED + "Sorry, we recieved a " + colorama.Fore.RESET, end='')
                print(f"{colorama.Back.RED}{colorama.Fore.WHITE} {response.status_code} {colorama.Style.RESET_ALL}", end='')
                print(colorama.Fore.RED, "response code from CODEFORCES. 😟", colorama.Fore.RESET)
            
            else:
                data = json.loads(response.text)
                data = data['result']

                table_header = ['Problem Index', 'Problem Name', 'Verdict', 'Time', 'Memory']
                table_row = []

                idx = 0
                while idx < len(data) and idx < count:
                    problem_index = str(data[idx]['problem']['contestId']) + str(data[idx]['problem']['index'])
                    problem_name = data[idx]['problem']['name']
                    
                    try:
                        verdict = data[idx]['verdict']
                    except Exception:
                        verdict = 'None'

                    time = str(data[idx]['timeConsumedMillis']) + ' ms'
                    memory = str(data[idx]['memoryConsumedBytes'] // 1024) + ' kb'

                    table_row.append([problem_index, problem_name, verdict, time, memory])
                    idx += 1

                table = tabulate(table_row, headers=table_header, tablefmt='github')
                print(colorama.Fore.GREEN)
                print(table)
                print(colorama.Fore.RESET)


        except Exception as error:
            # error_msg.error()
            raise error

    if 'true' in raw_cmd:
        print(colorama.Fore.BLUE + "Enter a valid user handle: " + colorama.Fore.RESET, end="")
        user_handle = input()

        print(colorama.Fore.BLUE + "Enter the starting index: " + colorama.Fore.RESET, end="")
        starting_index = int(input())

        print(colorama.Fore.BLUE + "How many submissions do you want to check? " + colorama.Fore.RESET, end="")
        counts = int(input())

        get_sub_history(user_handle, starting_index, counts)

    else:
        print(colorama.Fore.BLUE + "Enter a valid user handle: " + colorama.Fore.RESET, end="")
        user_handle = input()

        get_sub_history(user_handle)

