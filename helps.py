from tabulate import tabulate
import colorama


yes = colorama.Fore.GREEN + 'True' + colorama.Fore.RESET
no = colorama.Fore.RED + 'Null' + colorama.Fore.RESET

data = [
    ['user_info', 'shows information about the specified user', no],
    ['user_subs', 'Returns the list of submissions the user has', yes],
    [' ', ' ', ' '],
    ['show_problem', 'shows the problem statement(problem index needed)', no],
    ['problemset', 'Shows list of top 50 problems from the CF problemsets page', no],
    ['sort_problem', 'Sorts problem and output list of 30 problems', no],
    ['sub_sol', 'Submit a problem solution via command line', no]
    [' ', ' ', ' '],
    ['contest_list', 'Shows the information of 10 latest contests', yes],
    ['contest_standings', 'Shows the leaderboard for top 20 participants', yes],
    ['contest_ratings_changes', 'Shows the list of top 20 ratings change', yes],
    ['contest_problems', 'Shows all the problems of the specified contest', no],
    [' ', ' ', ' '],
    ['Exit', 'Closes this application', no],
    ['Help', 'Shows all the available commands', no]
]

def show_help():
    headers = ['Commands', 'Operations', 'Optional Parameters']

    table = tabulate(data, headers=headers, tablefmt='github')
    print()
    print(table)

    print()
    print("You can trigger optional paramaters by adding the parameter after the command")
    print("EXAMPLE: " + colorama.Fore.GREEN + "contest_list true")
    print(colorama.Fore.RED + "Uppercase lowercase doesn't matter")

    print(colorama.Fore.RESET)

