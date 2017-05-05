#Figure out the current time
import webbrowser
import random
import time
from time import strftime
currenttime = strftime("%H:%M")

#set target time
Alarm = input("What time do you want to wake up? \nUse this form.\nExample: 06:30 : ")

#open yt.txt file
with open('YT.txt', 'r') as f:
    content = f.readlines()

#Figure out the difference (target - current)
while currenttime != Alarm:
    print("This time is" + currenttime)
    time.sleep(1)

if currenttime == Alarm:
    print("Time to wakeup!")
    randomchoice=random.choice(content)
    webbrowser.open(randomchoice)
        
    
