han = open('mbox-short.txt')
for line in han:
  line = line.rstrip() 
  if not line.startswith("From ") :
    continue
  else :
    wds = line.split()
    print(wds[2])
  