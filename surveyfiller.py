from random import randint
import requests
dict1 = ["Yes,++I'll+be+there", "Sorry,+can't+make+it"]
dict2 = ['true','weh','uhhuh','alright']
dict3 = ['Website','Friend','Newsletter','Advertisement']
dict4 = ['true','weh','uhhuh','alright']

n = 0
while n < 5:
    a = randint(0,1)
    b = randint(0,3)
    c = randint(0,3)
    d = randint(0,3)    
    url = '='\
          + dict1[a] + '=' + dict2[b] +''+dict3[c]+ '&entry' + dict4[d]
    n += 1
    print(url)
    requests.get(url)
