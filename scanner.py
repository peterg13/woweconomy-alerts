import subprocess
import pause
import datetime


def getDatetimeFromReturnValue(input):
    #splitDateAndTime [0]: "month/day/year [1]: hour:minute:second AM/PM"
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
    return newDatetime

def main():

    while(True):
        print("----------------------------------", flush=True)
        print("Running scan...", flush=True)
        #returned value format
        #{"current_price" : currentPrice, "last_updated" : last_updated, "next_update" : nextUpdate}
        process = subprocess.run(["python", "getPrice.py"], capture_output=True, text=True)
        returnedValues = eval(process.stdout)
        #datetime format (year, month, day, 24 hour, minute, second)
        
        nextUpdate = getDatetimeFromReturnValue(returnedValues["next_update"])
        print("Laestrite Ore: " + returnedValues["current_price"], flush=True)
        print("Last update: " + returnedValues["last_updated"])
        print("Pausing until: " + nextUpdate.strftime("%Y/%m/%d") + ", " + nextUpdate.strftime('%H:%M:%S'), flush=True)
        pause.until(nextUpdate)
        #pausing for 1 minute to give the site time to refresh
        pause.minutes(1) 

if __name__ == "__main__":
    main()