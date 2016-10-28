# GOAL: input hosts, output unique networks found, and lowest IP for each.
#
# PREREQS: pip install pssh, pip install netifaces #on all clients, python 2.x, socket.
#import pssh
import sys

myhosts = []
try:
    myhosts = raw_input(' Enter your space-delimited host list: ')
except:
    print ("Bad input, try again...")

# PSSH - CREATE DICT WITH HOSTS AND NETWORK INFO FOR EACH HOST via pssh
output_dict={}
output[]
for hosts in myhosts:
    client = ParallelSSHClient(hosts)
    output = client.run_command('/opt/local/bin/run_netifaces.py', sudo=False)
    output_dict[x] = output

# CODE TO ITERATE THRU DICT values, LIST AND SORT & UNIQ ALL NETWORKS.
network_dict{}
for key,val in output_dict():

# CODE TO CREATE NEW DICT WITH FINAL OUTPUT OF EACH NETWORK AND THE LOWEST IP FOR EACH.
final_dict{}

sys.exit(0)

###############################
# /opt/local/bin/run_netifaces.py
# Function iteraters thru list of interfaces using netifaces and dump ip, netmask and subnet.
# THE FOLLOW GOES INTO A SCRIPT ON EACH CLIENT IN /opt/local/bin/run_netifaces.py TO RUN AS A NON ROOT USER.
# SCRIPT ASSUMES python 2 IS IN THE PATH.

import netifaces
import sys


def ip4_addresses():
    ip_dict = {}
    for interface in interfaces():
        # NEED CODE HERE TO RETURN MORE GRANULAR NETWORK INFO...
        ip_dict[interface] = netifaces.ifaddresses(interface)
    return ip_dict

try:
    ip4_addresses(mylist)
    print (mylist)
except:
    print ("Error!")
    sys.exit(1)

sys.exit(0)
