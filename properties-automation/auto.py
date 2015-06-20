import sys
import re

filename=sys.argv[1]
line=int(sys.argv[2])
fo=open(filename,"r+")
for i in range(1,line) :
  fo.readline()
pos=fo.tell()
list=[]
while True :
  l=fo.readline()
  if not l : break
  list.append(l)
fo.seek(pos)
for arg in sys.argv[3:]:
 splits=arg.split(':',1)
 type=splits[1]
 name=splits[0]
 fo.write("\tprivate "+type+ " "+name+";\n")
 fo.write("\tpublic "+type+" get"+name.capitalize()+"(){\n")
 fo.write("\t\treturn "+name+";\n")
 fo.write("\t}\n")
 fo.write("\tpublic void set"+name.capitalize()+"("+type+" "+name+"){\n")
 fo.write("\t\tthis."+name+"="+name+";\n")
 fo.write("\t}\n")
 
for l in list :
  fo.write(l)
fo.close()