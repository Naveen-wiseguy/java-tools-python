import sys
import re

filename=sys.argv[1]


fo=open(filename+".java","w+")
fo.write("\npublic class "+filename+"{")

fo.write("\n\n\tpublic "+filename+"()\n")
fo.write("{\n}\n")

for arg in sys.argv[2:]:
 splits=arg.split(':',1)
 type=splits[1]
 name=splits[0]
 fo.write("\tprivate"+type+ " "+name+";\n")
 
for arg in sys.argv[2:]:
 splits=arg.split(':',1)
 type=splits[1]
 name=splits[0]
 fo.write("\tpublic"+type+" get"+name.capitalize()+"(){\n")
 fo.write("\t\treturn "+name+";\n")
 fo.write("\t}\n")
 fo.write("\tpublic void set"+name.capitalize()+"("+type+" "+name+"){\n")
 fo.write("\t\tthis."+name+"="+name+";\n")
 fo.write("\t}\n")
 
fo.write("}")
fo.close()