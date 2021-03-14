import subprocess
import pause
from datetime import datetime

#converts the unix time to 24 hour time and date
def getDatetimeFromReturnValue(unixTime):

    newDatetime = datetime.fromtimestamp(unixTime)
    print(newDatetime)

    #-----------------------------------------------------------------
    """ #splitDateAndTime [0]: "month/day/year [1]: hour:minute:second AM/PM"
    splitDateAndTime = input.split(", ")
    #splitDate [0]:month, [1]:day, [2]:year
    splitDate = splitDateAndTime[0].split("/")
    #converts 12 hour to 24 hour
    #ignore [0] only use [1] as it is the 24 hour time
    fullTime = datetime.datetime.strptime(splitDateAndTime[1], '%I:%M:%S %p')
    #splitTime [0]: hour, [1]: minute, [2]: second
    splitTime = fullTime.strftime('%H:%M:%S')
    splitTime = splitTime.split(":")
    newDatetime = datetime.datetime(int(splitDate[2]), int(splitDate[0]), 
        int(splitDate[1]), int(splitTime[0]), int(splitTime[1]), int(splitTime[2]))
    return newDatetime """
    #---------------------------------------------------------------------

def main():

    while(True):
        print("----------------------------------", flush=True)
        print("Running scan...", flush=True)
        #returned value format
        #{"current_price" : currentPrice, "last_updated" : last_updated, "next_update" : nextUpdate}
        process = subprocess.run(["python", "getPrice.py"], capture_output=True, text=True)
        returnedValues = eval(process.stdout)
        #the date returned is unix time and needs to be converted
        next_update = datetime.fromtimestamp(returnedValues["next_update"])
        last_updated = datetime.fromtimestamp(returnedValues["last_updated"])
        print("Laestrite Ore: " + str(returnedValues["current_price"]), flush=True)
        print("Last update: " + last_updated.strftime("%Y/%m/%d") + ", " + last_updated.strftime('%H:%M:%S'), flush=True)
        print("Pausing until: " + next_update.strftime("%Y/%m/%d") + ", " + next_update.strftime('%H:%M:%S'), flush=True)
        pause.until(next_update)
        #pausing for 2 minute to give the site time to refresh
        pause.minutes(2) 

if __name__ == "__main__":
    main()