#!/usr/bin/python

#Here is a basic script to knocking port


from time import sleep
import socket 
import os


os.system('clear')
print "Launching OpenPortTest, this tools is made by Jugulaire\n"
sleep(1)

common_port ={
        1 : ' TCP Port Service Multiplexer (TCPMUX) ',
        5 :  'Remote Job Entry (RJE)',
        7 :  'ECHO',
        9 : 'Wake up on lan',
        18 : 'Message Send Protocol (MSP)',
        20 : 'FTP -- Data',
        21 : 'FTP -- Control',
        22 : 'SSH Remote Login Protocol',
        23 : 'Telnet',
        25 : 'Simple Mail Transfer Protocol (SMTP)',
        29 : 'MSG ICP',
        37 : 'Time',
        42 : 'Host Name Server (Nameserv)',
        43 : 'WhoIs',
        49 : 'Login Host Protocol (Login)',
        53 : 'Domain Name System (DNS)',
        67 : 'DHCP/BOOTP',
        68 : 'DHCP/BOOTP',
        69 : 'Trivial File Transfer Protocol (TFTP)',
        70 : 'Gopher Services',
        79 : 'Finger',
        80 : 'HTTP',
        102 : 'MS Exchange',
        103 : 'X.400 Standard',
        108 : 'SNA Gateway Access Server',
        109 : 'POP2',
        110 : 'POP3',
        115 : 'Simple File Transfer Protocol (SFTP)',
        118 : 'SQL Services',
        119 : 'Newsgroup (NNTP)',
        137 : 'NetBIOS Name Service',
        139 : 'NetBIOS Datagram Service',
        143 : 'Interim Mail Access Protocol (IMAP)',
        150 : 'NetBIOS Session Service',
        156 : 'SQL Server',
        161 : 'SNMP',
        179 : 'Border Gateway Protocol (BGP)',
        190 : 'Gateway Access Control Protocol (GACP)',
        194 : 'Internet Relay Chat (IRC)',
        197 : 'Directory Location Service (DLS)',
        389 : 'Lightweight Directory Access Protocol (LDAP)',
        396 : 'Novell Netware over IP',
        443 : 'HTTPS',
        444 : 'Simple Network Paging Protocol (SNPP)',
        445 : 'Microsoft-DS',
        458 : 'Apple QuickTime',
        546 : 'DHCP Client',
        547 : 'DHCP Server',
        563 : 'SNEWS',
        569 : 'MSN',
        1080: 'Socks'
    }


ip = raw_input("Enter target IP iadress : \n")
print "> Starting port testing on", ip , "\n"
sleep(1)
nb = 0
open_port = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
for key in range(65536):
    if not(sock.connect_ex((ip,key))):
        open_port.append(key)
        nb+=1
    if key == ((65536/100)*25):
        print "==> 25% finished with",nb,"port(s) find\n"
    if key == ((65536/100)*50):
        print "=====> 50% finished with",nb,"port(s) find\n"
    if key == ((65536/100)*80):
        print "========> 80 finished with",nb,"port(s) find\n"
print "Finished with",nb, "opened port(s)\n" 

for port in open_port:
    for key, value in common_port.items():
        if port == key:
            print "=> Port",port,"used in",value,"is open\n" 
print "=> Port",port,"is opened\n"
sock.close()
