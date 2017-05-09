import requests
from bs4 import BeautifulSoup
from subprocess import check_output
url = 'https://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
href = soup.select('#ctl00_ctl00_MainEditable_mainContent_rptTranscript_ctl01_hypFile')
pdf_url = 'https://www.supremecourt.gov/oral_arguments/' + href[0].get('href')
res = requests.get(pdf_url)
with open(r', 'wb') as f:
    f.write(requests.get(pdf_url).content)

txt = check_output("pdftotext -layout abc.pdf", shell = True).decode()
f = open('abc.txt', 'r')
print(f.read().count("(Laughter.)"))


        



        



