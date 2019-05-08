import os
import sys, getopt
import easywebdav
from generate_urls import *
import filecmp
import difflib

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024

# Use case
# read_file.py --interface=whatever --environment=dev --file=afile



opts, _ = getopt.getopt(sys.argv[1:], [], ['interface1=', 'environment1=', 'interface2=', 'environment2=', 'file='])

interfaceUrl1 = ''
environment1 = ''
interfaceUrl2 = ''
environment2 = ''
pathfile1 = ''
pathfile2 = ''
for opt, arg in opts:
	if opt in ('--interface1'):
		interfaceUrl1 = getInterfacesUrls(arg)
	if opt in ('--environment1'):
		environment1 = arg		
	if opt in ('--interface2'):
		interfaceUrl2 = getInterfacesUrls(arg)		
	if opt in ('--environment2'):
		environment2 = arg
	if opt in ('--file'):			 		
		pathfile1 = getPath(environment1) + arg		
		pathfile2 = getPath(environment2) + arg			

def read(webdav, environment, pathfile):	

	if(webdav.exists(pathfile)):
	    response = webdav._send('GET', pathfile, 200, stream=True)
	    text = ''
	    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
	        text+=chunk

	    return text

	else:
		print("the file: " + pathfile + " doesnt exist")		
		sys.exit(0)


webdav1 = easywebdav.connect(interfaceUrl1, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
filetext1 = read(webdav1, environment1, pathfile1)

webdav2 = easywebdav.connect(interfaceUrl2, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
filetext2 = read(webdav2, environment2, pathfile2)

result = difflib.unified_diff(filetext1.strip().splitlines(), filetext2.strip().splitlines(), fromfile='file1', tofile='file2',  lineterm='', n=6)
for line in result:
	print(line)




