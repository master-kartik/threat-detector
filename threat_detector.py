import sys
from arp_scan import arp_scan
print('Hello, Welcome to Threat Detector')
print("current available choices : \n 1. ARP_SCAN \n 2. Exit")
x = int(input("enter the functionality you want to use : "))
while (x!=2):
    if (x==1):
        arp_scan()
        x = int(input("enter the functionality you want to use : "))
    else:
        print("invalid input")
        x = int(input("enter the functionality you want to use : "))
        

exit()