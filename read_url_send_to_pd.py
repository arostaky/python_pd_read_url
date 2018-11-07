import urllib
import os
#link = "http://www.somesite.com/details.pl?urn=2344"
link = "https://jsonplaceholder.typicode.com/todos/1"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)
#os.system("echo '0 " + str(myfile) + ";' | pdsend 3000 localhost udp")
os.system("echo '0 " + str(myfile) + ";' | /Applications/Pd-extended.app/Contents/Resources/bin/pdsend 3001 localhost udp")