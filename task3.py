f=open("running-config.cfg",'r')
f=f.read()
f=f.split("\n")
final_list = list()
def all_list():
  access_list = []
  transit_access_in = []
  fw_managemant_access_in = []
  global_access = []
  for i in f:
    if "access_list_in" in i :
      i = i.strip()
      access_list_in.append(i) 
    if "transit_access_in" in i:
      i = i.strip()
      transit_access_in.append(i)
    if "fw_managemant_access_in" in i:
      i = i.strip()
      fw_managemant_access_in.append(i)
  print(access_list)
  print(transit_access_in)
  print(fw_managemant_access_in)
all_list()
