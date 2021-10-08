import webbrowser
from googlesearch import search
from PyInquirer import prompt
questions = [
    {
        'type': 'input',
        'name': 'search_input',
        'message': 'What is your search ? ',
    }
]
answers = prompt(questions)
query = str(answers.get("search_input"))
loopnumber = 1
links=[]

for j in search(query):
    links.append(j)
    print(str(loopnumber) + "."+j)
    loopnumber += 1

questions2 = [
    {
        'type' : 'input',
        'name' : 'linktoopen',
        'message' : 'Which link do you want to open ? (input the number)',
        }
]
link_answer = prompt(questions2)
link_open = int(link_answer.get('linktoopen'))
number_list = link_open - 1
link_specific = links[number_list]
webbrowser.open(link_specific, new=2)
