#!/bin/python
import os
from time import sleep
import commands
import sys

#vars
st1 = sys.argv[1] 
e = ""
b = ""
p1 = ""
p2 = ""
p3 = ""
p4 = ""
#end of vars

print """         Coded By M0NST4R
########  ######## ######## ##    ## 
##     ##    ##       ##    ###   ## 
##     ##    ##       ##    ####  ## 
########     ##       ##    ## ## ## 
##   ##      ##       ##    ##  #### 
##    ##     ##       ##    ##   ### 
##     ##    ##       ##    ##    ## 
 Redirector Of Tor For All Traffic Network"""

print 
print 

if st1 == "--help":
 print """USAGE:
 python RTTN.py start for ON
 python RTTN.py stop for OFF"""

#Functions
def check():
    output1 = commands.getoutput('netstat -l')
    output = commands.getoutput('ps -A')
    if 'tor' and 'privoxy' in output:
        global e
        e = "Running"
    else:
        e = "Not Running"
    if 'localhost:9051' in output1:
        global b
        b = "Running"
    else:
        b = "Not Running"
def trafic():
    output = commands.getoutput('service tor status')
    if 'inactive' in output:
        print "No Running"
    else:
        os.system("iptables -t nat -F OUTPUT")
        os.system("iptables -t nat -A OUTPUT -m state --state ESTABLISHED -j RETURN")
        os.system("iptables -t nat -A OUTPUT -m owner --uid debian-tor  -j RETURN")
        os.system("iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 9061")
        os.system("iptables -t nat -A OUTPUT -p tcp --dport 53 -j REDIRECT --to-ports 9061")
        os.system("iptables -t nat -A OUTPUT -d 10.66.0.0/255.255.0.0 -p tcp -j REDIRECT --to-ports 9051")
        os.system("iptables -t nat -A OUTPUT -d 127.0.0.1/8    -j RETURN")
        os.system("iptables -t nat -A OUTPUT -d 192.168.0.0/16 -j RETURN")
        os.system("iptables -t nat -A OUTPUT -d 172.16.0.0/12  -j RETURN")
        os.system("iptables -t nat -A OUTPUT -d 10.0.0.0/8     -j RETURN")
        os.system("iptables -t nat -A OUTPUT -p tcp -j REDIRECT --to-ports 9051")
        os.system("iptables -t filter -F OUTPUT")
        os.system("iptables -t filter -A OUTPUT -m state --state ESTABLISHED -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -m owner --uid debian-tor  -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -p udp --dport 9061 -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -p tcp --dport 9061 -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -d 10.66.0.0/255.255.0.0 -p tcp -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -d 127.0.0.1/8    -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -d 192.168.0.0/16 -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -d 172.16.0.0/12  -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -d 10.0.0.0/8     -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -p tcp -j ACCEPT")
        os.system("iptables -t filter -A OUTPUT -p udp -j REJECT")
        os.system("iptables -t filter -A OUTPUT -p icmp -j REJECT")
def check_port():
    output = commands.getoutput('netstat -l')
    if 'localhost:9051' in output:
        global p1
        p1 = "Open"
    else:
        p1 = "Not Open"
    if 'localhost:9051' in output:
        global p2
        p2 = "Open"
    else:
        p2 = "Not Open"
    if 'localhost:9051' in output:
        global p3
        p3 = "Open"
    else:
        p3 = "Not Open"
    if 'localhost:9051' in output:
        global p4
        p4 = "Open"
    else:
        p4 = "Not Open"  
#end of functions

user = os.geteuid()

if user != 0:
    print "Not is root brow!"
else:
    if st1 == "start":
        os.system("clear")
        print "Starting tor..."
        os.system("service tor start")
        sleep (0.5)
        print "Starting privoxy.."
        os.system("service privoxy start")
        sleep (0.5)
        print "Starting RTTN..."
        trafic()
        sleep(0.5)

        check()
        check_port()

        os.system("clear")

        print "[+] Tor =====> %s" % e
        sleep(0.4)
        print "[+] Privoxy =====> %s" % e
        sleep(0.4)
        print "[+] RTTN =====> %s" % b
        sleep(0.3)
        print "[+] PORT 127.0.0.1:9050 SOCKS [+] %s" % p1
        sleep(0.2)
        print "[+] PORT 127.0.0.1:8118 HTTP [+]  %s" % p2
        sleep(0.2)
#Port Of Trafic Tor On Your Network
        print "[+] PORT 127.0.0.1:9051 TRANS_PORT [+] %s" % p3
        sleep(0.2) 
        print "[+] PORT 127.0.0.1:9061 DNS PORT [+]  %s" % p4

if st1 == "stop":                                        
   os.system("clear")
   print "Stopping RTTN..."
   os.system("iptables -t nat -F OUTPUT")
   os.system("iptables -t filter -F OUTPUT")
   sleep(0.5)
   print "Stopping Tor..."
   os.system("service tor stop")
   sleep(0.5)
   print "Stopping Privoxy..."
   os.system("service privoxy stop")
