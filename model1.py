f=open("running-config.cfg",'r')
f=f.read()
f=f.split("\n")
new_list = list()
if_list = list()
vlencheck = 0

def list_ifname_ip():
	for value in f:
		if "interface" in value:
			value=value.split()
			if_list.append(value[1])
                if "nameif" in value:
			value=value.split()
			if "no" in value[0]:
				if_list.append("null")
			else:
				if_list.append(value[1])
		if "ip address" in value:
			if vlancheck == 0:
				if_list.append("null")
			value=value.split()
                else:
	               if_list.append(value[2])
print(list_ifname_ip())
		
