import qus_reader
import contests
import helps
import user
import colorama


while True:
    cmd = input("|>|> ")

    # No section
    if 'user_info' in cmd.lower():
        user.get_user_info()

    # problems command section
    elif 'show_problem' in cmd.lower():
        qus_reader.read_prompts()

        # not connected
        # - problemsets
        # - sort_problem

    # Contest command section

    elif "contest_list" in cmd.lower():
        contests.contest_list(cmd.lower())

    elif 'contest_problems' in cmd.lower():
        contests.contest_problems()

    elif 'contest_standings' in cmd.lower():
        contests.contest_standings(cmd.lower())

        # not Connected
        # - contest_standings => *
        # - contest_ratings_changes => *

    # Basics command section

    elif 'exit' in cmd.lower():
        break

    elif 'help' in cmd.lower():
        helps.show_help()

    else:
        print(colorama.Fore.RED + "No such command found. Pleas try" + colorama.Fore.GREEN + " Help " + colorama.Fore.RED + "to see the availabe list of commands" + colorama.Fore.RESET)

