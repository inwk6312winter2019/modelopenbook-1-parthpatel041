f=open("running-config.cfg",'r')
f=f.read()
f=f.split("\n")
new_list = list()
if_list = list()

def list_ifname_ip():
	for value in f:
		if "interface" in value:
			value=value.split()
			if_list.append(value[1])
		
