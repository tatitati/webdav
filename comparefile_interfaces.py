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



opts, _ = getopt.getopt(sys.argv[1:], [], ['interfaces=', 'environment=', 'file='])

interfaceUrls = []
environment = ''
pathfile = ''

for opt, arg in opts:
	if opt in ('--interfaces'):
		interfacesList = arg.split('|')
		print interfacesList
		for interface in interfacesList:
			interfaceUrls.append(getInterfacesUrls(interface))
	if opt in ('--environment'):
		environment = arg		
	if opt in ('--file'):			 		
		pathfile = getPath(environment) + arg				

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
filetext1 = read(interfaceUrls[0], webdav1, environment, pathfile)

for interfaceUrl in interfaceUrls[1:]:	
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print(interfaceUrls[0] + "        vs        " + interfaceUrl)
	print("\n\n\n\n")
	webdav2 = easywebdav.connect(interfaceUrl, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
	filetext2 = read(interfaceUrl, webdav2, environment, pathfile)
	if filetext2 != "":
		result = difflib.unified_diff(filetext1.strip().splitlines(), filetext2.strip().splitlines(), fromfile=interfaceUrls[0], tofile=interfaceUrl,  lineterm='', n=6)
		for line in result:
			print(line)




