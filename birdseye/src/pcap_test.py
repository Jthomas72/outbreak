#!/usr/bin/python
import subprocess
import sys
from array import array

def pcap_funct(packets, filter):
    pcapProcess = subprocess.Popen(["sudo","./birdseye/src/pcap", filter, packets], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    listOfIps = []
    i = 0
    while True:
        nextLine = pcapProcess.stdout.readline()
        listOfIps.insert(i, nextLine)
        if nextLine == '' and pcapProcess.poll() is not None:
            break
        sys.stdout.write(nextLine)
        sys.stdout.flush()
        i+=1
    print pcapProcess.returncode
    return listOfIps
#pcap_funct("10", "tcp")
