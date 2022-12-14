import pywebio
from pywebio.input import input, TEXT
from pywebio.output import put_text,put_html,put_markdown,put_link,put_row
from QueryProcessing import query_processing
import os
import json


def display_results(query):
   
    f = open(os.path.join("data",'Results.txt'), 'r')
    id_list = [ ]
    
    for line in f:
        ll1, ll2 = line.split('\n')
        if(ll1=='[' or ll1==']'):
            id_list=[]
            break
        id_list.append(int(ll1))
    print(id_list)
    if len(id_list) == 0:
        put_text(f'There are no matching publications with your input -{query} - Please try again with a different term')
    else:

        if os.path.isfile(os.path.join("data", "output.json")):
            with open(os.path.join("data", "output.json"), "r") as read_file:
                publications= json.load(read_file)

        result = [ ]
        put_html('<center>')
        put_markdown('# **Results**')
        put_html('</center>')
        for id in id_list:
           link=publications["link"] [id]
           put_html('<b>')
           put_text(publications["title"][id ])
           put_html('</b>')
           put_text(publications["text"][id ],'[',publications["published"][id ],']')
           put_link(link, url=link, new_window=True, scope=None, position=-1)
           #put_text(publications["published"][id ])

           #for x in publications[ "authors" ][ id ]:
            #   put_link(x, url=x, new_window=True, scope=None, position=-1)

           put_html('<hr>')

def browser_fn():
    while True:
        query = input("Enter query:",type=TEXT)
        if query.strip() != "": 
            break
    print("Entered query: ",query)
    query_processing(query)
    display_results(query)

if __name__ == '__main__':
    pywebio.start_server(browser_fn,port=8000)

