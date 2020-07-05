from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from questions import sub_questions
import time
import colorama
import clipboard
import error_msg



def sub_prob():
    # USER INFORMATIONS
    user_handle = input("Enter your handle(or email): ")
    user_password = sub_questions.pwd()

    LOGIN_URL = 'https://codeforces.com/enter?back=%2F'

    opt = Options()

    browser = Chrome()
    print(colorama.Fore.BLUE + 'Booting up a headless browser' + colorama.Fore.RESET, end='\r')
    browser.get(LOGIN_URL)
    print('                                                                   ', end='\r')
    print(colorama.Fore.BLUE + 'Logging you in...' + colorama.Fore.RESET, end='\r')
    # LOGGING IN 
        # Getting input fields

    try:
        browser_handle = browser.find_element_by_xpath('//*[@id="handleOrEmail"]')
        browser_password = browser.find_element_by_xpath('//*[@id="password"]')
        browser_submit = browser.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input')
    except Exception as error:
        error_msg.sub_sol_error_random()
        browser.close()
        return -1
    
    browser_handle.send_keys(user_handle)
    browser_password.send_keys(user_password)
    browser_submit.click()

    time.sleep(3)

    try: # Checking for an error message in the browser
        check_registration = browser.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[3]/td[2]/div/span')
        error_msg.sub_sol_error_log_in()
        browser.close()
        return -1
    except:

        print(colorama.Fore.GREEN + "Successfully logged in" + colorama.Fore.RESET, end='\r')
        try:
            browser_problemset = browser.find_element_by_xpath('//*[@id="body"]/div[3]/div[5]/ul/li[5]')
            browser_problemset.click()
        except:
            error_msg.sub_sol_error_random()
            browser.close()
            return -1

        print(colorama.Fore.BLUE + "Preparing to submit code" + colorama.Fore.RESET)


        time.sleep(5)

        try:
            browser_problem_submit = browser.find_element_by_xpath('//*[@id="pageContent"]/div[1]/ul[2]/li[3]')
            browser_problem_submit.click()
        except:
            error_msg.sub_sol_error_random()
            browser.close()
            return -1
            

        # Taking the solution as input
        print(colorama.Fore.CYAN)
        problem_index = input("Enter problem index: ")
        problem_language = sub_questions.sub_lang()
        problem_file_path = input("Enter the file path: ")
        print(colorama.Fore.RESET)

        try:
            browser_problem_index = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[1]/td[2]/input')
            browser_problem_index.send_keys(problem_index)

            browser_problem_language = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[3]/td[2]/select')
            browser_problem_language.click()
        except:
            error_msg.sub_sol_error_random()
            browser.close()
            return -1


        if problem_language == 'Python':
            browser_select_language = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[3]/td[2]/select/option[23]')
        elif problem_language == 'C++':
            browser_select_language = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[3]/td[2]/select/option[5]')
        elif problem_language == 'Java':
            browser_select_language = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[3]/td[2]/select/option[13]')

        browser_select_language.click()

        browser_code_area = browser.find_element_by_xpath('//*[@id="editor"]/textarea')

        browser_code_submit_button = browser.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[6]/td/div/div/input')


        try:
            with open(problem_file_path, 'r') as sol:
                print(colorama.Fore.BLUE + "Submiting solution" + colorama.Fore.RESET, end='\r')

                solution_code = sol.read()
                sol_code = clipboard.copy(solution_code)

                actions = ActionChains(browser)
                actions.click(browser_code_area)

                actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)

                actions.click(browser_code_submit_button)
                actions.perform()

                time.sleep(4)
                print(colorama.Fore.GREEN + "Sucessfully submitted the solution" + colorama.Fore.RESET, end='\n')
                print('                                                                      ', end='\n')
                browser.close()
        except Exception as err:
            error_msg.sub_sol_error_submit()
            return -1
            browser.close()
