
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from obswebsocket import obsws, requests
import time
import os 

hidingImage = "hidingImageSceneName" # Replace with name of scene that blocks stranger 


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
 
    if iteration == total: 
        print()

os.system('cls')
print()

printProgressBar(0, 5, prefix = 'Initializing:', suffix = '', length = 24)

options_s1 = Options()
time.sleep(0.1)
printProgressBar(1, 5, prefix = 'Initializing:', suffix = '', length = 24)

options_s1.add_experimental_option("debuggerAddress", "localhost:9222")
time.sleep(0.1)
printProgressBar(2, 5, prefix = 'Initializing:', suffix = '', length = 24)

s1 = webdriver.Chrome(options=options_s1)  
time.sleep(0.1)
printProgressBar(3, 5, prefix = 'Initializing:', suffix = '', length = 24)

ws = obsws("localhost", 4444)
time.sleep(0.1)
printProgressBar(4, 5, prefix = 'Initializing:', suffix = '', length = 24)

ws.connect()
time.sleep(0.1)
printProgressBar(5, 5, prefix = 'Initializing:', suffix = '', length = 24)

print()
print("Initialized")
print("Have a good stream :)")
time.sleep(.8)

os.system('cls') 

checking = 1

def skip(): 
    ws.call(requests.SetCurrentScene(hidingImage)) 
    os.system('cls')
    print()
    print("Stranger has disconnected.")
    while(1 == 1):
        if(s1.page_source.find("Stranger has disconnected.") > -1):
            time.sleep(0.1)
        else:
            break
    os.system('cls') 
    

bar = [
    " [֍     ]",
    " [ ֍    ]",
    " [  ֍   ]",
    " [   ֍  ]",
    " [    ֍ ]",
    " [     ֍]",
    " [    ֍ ]",
    " [   ֍  ]",
    " [  ֍   ]",
    " [ ֍    ]",
]

x = 0

def checkSkip():
    print()
    print("Waiting for Skip")
    print()
    if s1.page_source.find("Stranger has disconnected.") > -1: 
        skip()
    else: 
        return
       

while(checking == 1):
    if x == 10:
        x = 0
    checkSkip()
    print(bar[x % len(bar)], end="\r")
    x += 1
    os.system('cls')