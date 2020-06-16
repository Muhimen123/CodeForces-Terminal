import requests
from bs4 import BeautifulSoup
import re


# Sending request and geting the source code
ids = input("Enter the problem ID here(eg. 1352-d):")
ids = ids.split('-')

res = requests.get(f'https://codeforces.com/problemset/problem/{ids[0]}/{ids[1]}')
source = BeautifulSoup(res.text, "lxml")

# Collecting informations about the problem. i. e. title, time-limit, memory-limit

statement = source.find('div', {"class": "header"}).get_text()
title = source.find('div', {"class": "title"}).get_text()
time = source.find('div', {"class": "time-limit"}).get_text()
memory = source.find('div', {"class": "memory-limit"}).get_text()

print('\n\n')
print('=====================================')
print("Problem hearders: ")
print(title.title().strip())
print(time.title().strip())
print(memory.title().strip())
print('=====================================')
print('\n\n')

full_problem  = source.find('div', {"class": "problem-statement"})

ls = full_problem.contents

# Making of a list of div elements that contains inputs, output, test_cases

while " " in ls:
    ls.remove(" ")
problem = ls[1]
inputs = ls[2]
outputs = ls[3]
test_cases = ls[4].find('div', {'class': 'sample-test'})
try:
    notes = ls[5]
except:
    pass

for tag in problem.find_all(['p', 'ul']):
    values = tag.contents
    output = ""

    for txt in values:
        txt= str(txt)

        # string formatting
        txt = txt.replace("$", "").replace("\dots", "...").replace("       ", " ").replace("   ", " ")
        txt = txt.replace("\\le", "<=").replace("\\l", "<").replace("\\ge", ">=").replace("\\g", ">")
        txt = txt.replace("\\cdot", ".").replace("<li>", "").replace("</li>", "\n\n")
        txt = txt.replace('<span class="tex-font-style-it">', "")
        txt = txt.replace('<span class="tex-font-style-tt">', "")
        txt = txt.replace('<span class="tex-font-style-bf">', "")
        txt = txt.replace("</span>", "")

        tags = re.findall('<(.+?)>', str(txt))
        for tag in tags:
            txt = txt.replace('<' + tag + '>', "")

        output += txt
    
    print(output)
    print()

print('INPUT/OUTPUT\n')
print("Input format: ")
for tag in inputs.find_all(['p', 'ul']):
    values = tag.contents
    output = ""

    for txt in values:
        txt= str(txt)

        # string formatting
        txt = txt.replace("$", "").replace("\dots", "...").replace("       ", " ").replace("   ", " ")
        txt = txt.replace("\\le", "<=").replace("\\l", "<").replace("\\ge", ">=").replace("\\g", ">")
        txt = txt.replace("\\cdot", ".").replace("<li>", "").replace("</li>", "\n\n")
        txt = txt.replace('<span class="tex-font-style-it">', "")
        txt = txt.replace('<span class="tex-font-style-tt">', "")
        txt = txt.replace('<span class="tex-font-style-bf">', "")
        txt = txt.replace("</span>", "")
        tags = re.findall('<(.+?)>', str(txt))
        for tag in tags:
            txt = txt.replace('<' + tag + '>', "")

        output += txt

    print(output)
    print()

print('Output format')
for tag in outputs.find_all(['p', 'ul']):
    values = tag.contents
    output = ""

    for txt in values:
        txt= str(txt)

        # string formatting
        txt = txt.replace("$", "").replace("\dots", "...").replace("       ", " ").replace("   ", " ")
        txt = txt.replace("\\le", "<=").replace("\\l", "<").replace("\\ge", ">=").replace("\\g", ">")
        txt = txt.replace("\\cdot", ".").replace("<li>", "*").replace("</li>", "\n\n")
        txt = txt.replace('<span class="tex-font-style-it">', "")
        txt = txt.replace('<span class="tex-font-style-tt">', "")
        txt = txt.replace('<span class="tex-font-style-bf">', "")
        txt = txt.replace("</span>", "")

        tags = re.findall('<(.+?)>', str(txt))
        for tag in tags:
            txt = txt.replace('<' + tag + '>', "")

        output += txt

    print(output)
    print()

# Showing sample test cases

print("EXAMPLE\n")
sample_inputs = test_cases.find_all('div', {"class": "input"})
sample_outputs = test_cases.find_all('div', {"class": "output"})
for i in range(len(sample_inputs)):
    print('=================')
    print("SampleInput ==>")
    print(sample_inputs[i].pre.text)
    print("SampleOutput ==>")
    print(sample_outputs[i].pre.text)
    print()

# If notes are available in the problem then show notes

try:
    notes = notes.find_all(['p', 'ul'])
    print('NOTES ==>')
    for tag in notes:
        values = tag.contents
        output = ""

        for txt in values:
            txt= str(txt)

            # string formatting
            txt = txt.replace("$", "").replace("\dots", "...").replace("       ", " ").replace("   ", " ")
            txt = txt.replace("\\le", "<=").replace("\\l", "<").replace("\\ge", ">=").replace("\\g", ">")
            txt = txt.replace("\\cdot", ".").replace("<li>", "").replace("</li>", "\n\n")
            txt = txt.replace('<span class="tex-font-style-it">', "")
            txt = txt.replace('<span class="tex-font-style-tt">', "")
            txt = txt.replace('<span class="tex-font-style-bf">', "")
            
            tags = re.findall('<(.+?)>', str(txt))
            for tag in tags:
                txt = txt.replace('<' + tag + '>', "")

            output += txt
        
        print(output)
        print()
except:
    pass