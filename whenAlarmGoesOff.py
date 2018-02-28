currentTime=int(input("current time: "))
hrsToWait=int(input("hrs to wait: "))

#alarm goes off at
print("Alarm goes off at: %d") % ((currentTime + hrsToWait)%24)
                    
