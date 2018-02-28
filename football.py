#!/usr/bin/env python
import pandas as pd 

data = {"year":[2010,2011,2012,2011,2012,2010,2012,2011], 
        "team":["Bears","Lions","Bears", "Packers","Packers", 
            "Lions", "Bears", "Packers"], 
        "wins":[11,8,9,15,11,1,8,7],
        "losses":[5,8,6,1,5,10,6,12]}

football = pd.DataFrame(data)

print (football)
print()
print(football["team"])#printing team from football dataframe
print()
print (football.team)#similar to football["team"]
print ()
print (football["team"][football["losses"] > 8])
#print only team that has lost more than 8
print()
print(football[["year", "wins", "losses"]])
print()

#some of the basic and common method:
#slicing
#an individual index (through the function iloc or loc)
#Boolean indexing 
print (football.iloc[[4]])
print()
print (football.loc[[1]])
print ()
print (football[3:5])
print()
print (football[football.wins > 10])
print()
print (football[(football.wins > 10) & (football.team == "Packers")])
