#Name: Haira Aguilar
#Date: 9/13/19
#Program Name: ping-log.py

#Run Python IDLE
#Ctrl + C to stop

import subprocess, time, sys

def ping():
    
    while True:

        stat = subprocess.call(["ping", server], stdout = pingStat)
        
        print()
        
        if stat == 0:
            print("SERVER STATUS: ", server, " is UP!")
        else:
            print("SERVER STATUS: ", server, " is DOWN!")
            
        #Adjust time here
        time.sleep(5)
        
#Input the ip address that you'd like to ping
server = input("Enter ip address: ")

#Outputs the status results to a file
with open("ping-log.txt", "w") as pingStat:
    sys.stdout = pingStat
    ping()
