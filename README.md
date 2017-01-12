This is for creating OSPF for new firewall services.
This assumes the customer edge in managed by REANNZ and is on the MX and only caters to the current Frewall topology.
This is to help reduce building new firewall services.

topo.yaml is the current firewall topology

Provide the input for building the primary/secondary inside VLANs and the other details in the yaml format as shown below.

run python Firewall_OSPF.py <input yaml file>

sample output provided.

## Following is sample input file


# Three letter acronym for company name
tla :  gns

# description
des : lan

#VDOM
vdom : gns-gstlan2

# Vlan for inside interfaces
vlan1 : 28

# Vlan for outside interfaces
vlan2 :  2821

# Customer device name e.g 'gns01'
cdevice : gns01

# interface on customer device
cport : xe-0/0/21

# interface on AND that the customer port is connected to
dport : xe-0/0/2

# /31 for inside linknet
linknetin : 161.65.52.136/31

# /31 for outside linknet
linknetout : 161.65.52.148/31

# Customer prefix CIDR used for OSPF routing
prefix : 161.65.52.128/25

# is this the primary service, yes or no / true false
primary : false

# AND the customer device is connected to
and : and17

# which firewall are you configuring (anf14, anf16 or and17)
anf : anf17
