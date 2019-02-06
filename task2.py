
f=open('running-config.cfg')
  newText=f.read().replace('192', '10')
  newText=f.read().replace('172', '10')
f=open('running-config.cfg', "w")
  f.write(newText)
