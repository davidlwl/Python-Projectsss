from amazon.api import AmazonAPI
from twilio.rest import Client
amazon_in=AmazonAPI("")
# Region_options= ['US', 'FR', 'CN', 'UK', 'IN', 'CA', 'DE', 'JP', 'IT', 'ES']
product=amazon_in.lookup(ItemId='B00FEQ6TVO')
print(product.title)
price = product.price_and_currency[0]
print(price)
'''
def message(msg):
    account_sid = ""
    auth_token  = "e"
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg,
    to="+,    # Replace with your phone number
    from_="+) # Replace with your Twilio number
    print (message.sid)

message(product.title)'''

'''
def send_email(title,price):
    import smtplib

    gmail_user = 
    gmail_pwd = ""
    FROM = ''
    TO = [''] #must be a list
    SUBJECT = "Price drops"
    TEXT = "Your product is ready for the purchase"

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        print(server.ehlo())
        print(server.starttls())
        print(server.login(gmail_user, gmail_pwd))
        server.sendmail(FROM, TO, message)
        server.quit()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")'''

        
'''
print product.title
price = product.price_and_currency[0]
print price
expected_price =7000 # Enter your expected price

if price<=expected_price:
    message(product.title)
    send_email(product.title,price)'''

'''
from amazon.api import AmazonAPI
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
products = amazon.search(Keywords='kindle', SearchIndex='All')
for i, product in enumerate(products):
    print "{0}. '{1}'".format(i, product.title)
    product.price_and_currency'''


