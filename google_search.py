import re
import bs4
import requests

class get():
    def __init__(this, term):
        this.search_results = []
        this.suggestion = []
        this.fetch(term)

    def simple_suggestion(this):
        if this.suggestion == []: 
            print('no search is performed!')
            return
        print('------------------')
        for suggest in this.suggestion:
            print('>> ' + suggest)
        print('------------------')

    def simple_titles(this):
        if this.search_results == []: 
            print('no search is performed!')
            return
        print('------------------')
        for x in this.search_results:
            print('>> ' + x[0] )
        print('------------------')

    def simple_links(this):
        if this.search_results == []: 
            print('no search is performed!')
            return
        print('------------------')
        for x in this.search_results:
            print('>> ' + x[1] )
        print('------------------')



    def fetch(this, term):
        if term == '': return []
        this.req = requests.get('https://www.google.com/search?q=' + term)
        this.req_no_bold = ((str(this.req.text)).replace('<b>', '') ).replace('</b>', '')
        this.soup = bs4.BeautifulSoup(this.req_no_bold, 'html.parser')
        this.links_results = this.soup.find_all('a', href=re.compile('/url\?'))
        this.search_results = []

        for link in this.links_results:
            this.title = str(link.string)
            this.href = str(link['href']).replace('/url?q=', '')
            if (not this.title.lower() == 'cached') and (not this.title == 'None'):
                this.search_results.append((this.title, this.href))


        this.links_suggestion = this.soup.find_all('a', href=re.compile('/search\?ie='))
        this.suggestion = []
        for link in this.links_suggestion:
            this.title = str(link.string)
            if (not this.title.lower() == 'similar') and (not this.title.lower() == 'none') and (not this.title.lower() == 'more'):
                this.suggestion.append(this.title)

