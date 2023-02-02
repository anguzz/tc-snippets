import datetime
from playsound import playsound


''' 
YEAR        = datetime.date.today().year     # the current year
MONTH       = datetime.date.today().month    # the current month
DATE        = datetime.date.today().day      # the current day
MINUTE      = datetime.datetime.now().minute # the current minute
HOUR        = datetime.datetime.now().hour   #current hour
SECONDS     = datetime.datetime.now().second #the current second

print(YEAR, MONTH, DATE, HOUR, MINUTE, SECONDS)

'''


def getMin():
    MINUTE = datetime.datetime.now().minute
    print(MINUTE)
    return MINUTE


def playSound():
    print("sound played")
    playsound('sound.wav')


def time():
    while True:
        if(getMin()%15==0):
            playSound()
            exit()
        else:
            print("not at 15 min time")    
time()