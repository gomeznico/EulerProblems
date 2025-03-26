import requests
import os
from datetime import date
import browser_cookie3
from bs4 import BeautifulSoup
import sys

problem = "82"

print(f"Initializing problem {problem}")

if not os.path.isdir(f"problem{problem}"):
    os.mkdir(f"problem{problem}")
    os.chdir(f"problem{problem}")
    r = requests.get(f"https://projecteuler.net/problem={problem}")
    with open(f"problem{problem}.py","w") as f:
        soup = BeautifulSoup(r.content, 'html.parser')
        t = soup.get_text()[::]
        ## replace symbols
        t = t.replace('\\times','*')
        t = t.replace('\\begin{align}','')
        t = t.replace('\end{align}','')
        t = t.replace('\dots','...')
        t = t.replace('cdots','...')
        t = t.replace('&=','=')
        t = t.replace('$','')
        t = t.replace(' gt ',' > ')
        t = t.replace(' lt ',' < ')
        t = t.replace(' geq ',' >= ')
        t = t.replace(' leq ',' <= ')



        t = t.replace('\\','')

        i = t.find(f"Problem {problem}")
        j = t.find(f"Project Euler: Copyright Information | Privacy Policy")
        # t1 = soup.prettify()
        t = t[i:j-8]
        f.write(f'"""\n{t}"""')

        # f.write(f"""{r.text}\n\n""")
        # f.write(f"""puzzle_input = open("day{day}/input.txt",'r').read()\n""")
        # f.write("puzzle_input = puzzle_input[0:-1]")
