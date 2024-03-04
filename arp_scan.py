import sys
from scapy.all import srp, Ether, ARP

def arp_scan():
    # Creating an ARP request packet
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.0/24") #ip address

    # Sending the ARP request and receiving responses
    result, unanswered = srp(arp_request, timeout=0.01, verbose=0)

    # Displaying the results
    if result:
         print("MAC Address\t\tIP Address")
         print("-----------------------------------------")
         for sent, received in result:
            print(received.sprintf("%Ether.src%\t%ARP.psrc%"))
    else:
          print('no devices')

if __name__ == "__main__":
     arp_scan()
