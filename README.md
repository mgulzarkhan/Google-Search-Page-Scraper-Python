# Google-Search-Page-Scraper-Python

Takes a keyword from user and search it on google and returns respective results to the user.


# USAGE:

Download module to your current directory and use it according to the instructions given below.

Example:

import google_search    #--- import module

g = google_search.get('hello world')    #--- create an object and provide a keyword to search

g.search_results   #--- return a list containing tuples. each tuple contains title and link of each result.

g.search_suggestion   #--- return a list containing suggested keyword related to keyword provided by user

g.simple_titles()   #--- print titles of all results.

g.simple_links()   #--- print links of all results.

g.simple_suggestion()   #--- print all suggested keywords.

