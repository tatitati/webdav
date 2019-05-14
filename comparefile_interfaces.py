import os
import sys, getopt
import easywebdav
from generate_urls import *
import filecmp
import difflib

#
# THIS FILE COMPARE A FILE THROUGH ALL THE DIFFERENT INTERFACES
#

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024

# Use case
# read_file.py --interface=whatever --environment=dev --file=afile



opts, _ = getopt.getopt(sys.argv[1:], [], ['interfaces=', 'environment1=', 'environment2=', 'file='])

interfaceUrls = []
environment1 = ''
environment2 = ''
pathfile1 = ''
pathfile2 = ''
for opt, arg in opts:
	if opt in ('--interfaces'):
		interfacesList = arg.split('|')
		print interfacesList
		for interface in interfacesList:
			interfaceUrls.append(getInterfacesUrls(interface))
	if opt in ('--environment1'):
		environment1 = arg		
	if opt in ('--environment2'):
		environment2 = arg
	if opt in ('--file'):			 		
		pathfile1 = getPath(environment1) + arg		
		pathfile2 = getPath(environment2) + arg			

def read(interfaceURL, webdav, environment, pathfile):	

	if(webdav.exists(pathfile)):
	    response = webdav._send('GET', pathfile, 200, stream=True)
	    text = ''
	    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
	        text+=chunk

	    return text

	else:
		print(interfaceURL + ": the file: " + pathfile + " doesnt exist")		
		return ""


webdav1 = easywebdav.connect(interfaceUrls[0], username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
filetext1 = read(interfaceUrls[0], webdav1, environment1, pathfile1)

for interfaceUrl in interfaceUrls[1:]:	
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print(interfaceUrls[0] + "        vs        " + interfaceUrl)
	print("\n\n\n\n")
	webdav2 = easywebdav.connect(interfaceUrl, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
	filetext2 = read(interfaceUrl, webdav2, environment2, pathfile2)
	if filetext2 != "":
		result = difflib.unified_diff(filetext1.strip().splitlines(), filetext2.strip().splitlines(), fromfile=interfaceUrls[0], tofile=interfaceUrl,  lineterm='', n=6)
		for line in result:
			print(line)




