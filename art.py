def arts():
    import requests
    from bs4 import BeautifulSoup
    import webbrowser
    url = 'http://www.visual-arts-cork.com/famous-paintings/'
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    links = soup.select('p a')
    lister = []
    for i in range(14, len(links)-13):
        if links[i].get('href') == None:
            pass
        else:
            lister.append('http://www.visual-arts-cork.com/famous-paintings/'+ links[i].get('href'))

    print("Which painting would you like to learn about?")
    sucka = int(input('>'))
    url = lister[sucka]
    webbrowser.open(url)

arts()




        




            
    
        
    
    
