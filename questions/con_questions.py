from PyInquirer import style_from_dict, Token, prompt, Separator

def contest_main_qus():
    questions = [
        {
            'type': 'input',
            'name': 'contest_numbers',
            'message': 'How many answers do you want to see?',
            'default': '10'
        },
        {
            'type': 'list',
            'name': 'sort_by',
            'message': 'Choose how you want to sort the problem',
            'choices': ['Null', 'By_divs', 'By_phases']
        }
    ]

    answers = prompt(questions)
    return answers


def contest_div_qus():
    questions = [
        {
            'type': 'list',
            'name': 'ans',
            'message': 'Please select a div',
            'choices': ['Div. 1', 'Div. 2', 'Div. 3', 'Div. 4']
        }
    ]

    answers = prompt(questions)
    return answers


def contest_phase_qus():
    question = [
        {
            'type': 'list',
            'name': 'ans',
            'message': 'Please choose a phase',
            'choices': ['Before', 'Coding', 'Finished']
        }
    ]

    answers = prompt(question)
    return answers
