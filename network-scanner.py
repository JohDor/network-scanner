import scapy.all as sp
import optparse

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    (options, arguments) = parser.parse_args()
    return options

def scan (ip):
    arpRequest = sp.ARP(pstd=ip)
    broadcast = sp.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answeredList = sp.srp(arpRequestBroadcast, timeout=, verbose=False)[0]
    clientsList = []
    for element in answeredList:
        clienDict = {"ip":element[1].prsc, "mac": element[1].hwsrc}
        clientsList.append(clienDict)
        print(element[1].prsc + "\t\t" + element[1].hwsrc)
    return clientsList

def  printResult(resultList):
    print("IP\t\t\tMAC Address\n-------------------------------------------------------------")
    for client in resultList:
        print(client["ip"] + "\t\t" + client["mac"])

options = getArguments()
scanResult = scan(options.target)
printResult(scanResult)
