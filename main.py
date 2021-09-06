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
query = answers.get("search_input")
for j in search(query, tld="co.in", num=10, stop=10,pause=2):
    print(j)
