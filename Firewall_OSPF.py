#Written by Paul Gould paul.gould@reannz.co.nz on 11-Nov-2016
#Updated by Yeshaswini Ramesh yeshaswini.ramesh@reannz.co.nz  on 22-Nov-2016



from jinja2 import Environment, FileSystemLoader
import yaml
import codecs
import sys
import argparse
import netaddr

ENV = Environment(loader=FileSystemLoader('./'))
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def loopback(x):
	# takes a device name and returns it's loopback
	if str.lower(x[:3]) == "and" or str.lower(x[:3]) == "anf":
		z = "172.24." + str(int(x[3:]) + 32) + ".1"
		return z
	else:
		sys.exit("A device name is in the incorrect format")

# load yaml file into dictionary, either from CLI argument or default file.

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs='?', help="File with required variables, default is required_variables_FWOSPF.YAML, please use this as a template if you create your own", default="required_variables_FWOSPF.YAML")
args = parser.parse_args()
with open(args.file) as file:
    dict =  yaml.load(file)

topofile = open('topo.yaml')
topo = {}
topo = yaml.load(topofile)
# test to see if this is for a primary or secondary service and set metrics accordingly

if dict['primary'] == True:
	dict['metricout'] = 50
	dict['metricin'] = 50
elif dict['primary'] == False:
	dict['metricout'] = 100
	dict['metricin'] = 1000
	
else:
	sys.exit("Please set the primary field to yes / no, or true / false")
	
# lower case all dictionary values

for x in dict:
	dict[x] =  str.lower(str(dict[x]))
	
# Add linknet IP's to dictionary to be referred to when generating template
y = 0
for x in netaddr.IPNetwork(dict['linknetin']):
	dict['linknet'+str(y)] = str(x)
	y = y+1

for x in netaddr.IPNetwork(dict['linknetout']):
        dict['linknet'+str(y)] = str(x)
        y = y+1
	
# add the customer prefix to Dictionary

dict['mask'] = str(netaddr.IPNetwork(dict['prefix']).netmask)
print (dict['mask'])
dict['prefix'] = str(netaddr.IPNetwork(dict['prefix']).ip)
dict['andf'] = dict['anf'].replace('f','d')

# test to see if VPLS config is required, and use the template required for each

dpop =  dict['and']
fpop = dict['anf']
fw = {}
fw = topo[fpop]
if dpop[3:] == fpop[3:]:
	# Render template and print generated config to console
	template = ENV.get_template("OSPF_Template_no_VPLS2.0.txt")
	print template.render(config=dict,fwall=fw)
	
else:
	# generate config using VPLS template 
	dict['loopback'] = loopback(dict['and'])
	dict['loopbackf'] = loopback(fw['router'])
	#dict['andf'] = dict['anf'].replace('f','d')
	
	# Render template and print generated config to console
	template = ENV.get_template("OSPF_Template_VPLS.txt")
	print template.render(config=dict,fwall=fw)
