import pdfcrowd
from bs4 import BeautifulSoup, SoupStrainer
import requests
       
#print to_crawl

def get_page(page):
    r = requests.get(page)
    soup=BeautifulSoup(r.content,'lxml')
    return soup


def save_as_pdf(s):
    try:
        client = pdfcrowd.Client("-")
        html=get_page(s)
        output_file = open('true.pdf', 'wb')
        # convert an HTML file
        
        client.convertHtml(html, output_file)
        output_file.close()
        print ("Finished")
    except pdfcrowd.Error:
        print ('Failed:')


save_as_pdf('http://www.geeksforgeeks.org/ropes-data-structure-fast-string-concatenation/')

