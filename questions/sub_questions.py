from PyInquirer import style_from_dict, Token, prompt, Separator

def pwd():
    questions = [
        {
            'type': 'password',
            'name': 'pwd',
            'message': 'Enter your password: '
        }
    ]

    answer = prompt(questions)
    return answer['pwd']

def sub_lang():
    questions = [
        {
            'type': 'list',
            'name': 'lang',
            'message': 'Choose a programming language: ',
            'choices': ['Python', 'C++', 'Java']
        }
    ]

    answer = prompt(questions)
    return answer['lang']