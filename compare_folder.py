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
pathFolder1 = ''
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
		pathFolder = getPath(environment1) + arg

def read(webdav, environment, pathfile):	

	if(webdav.exists(pathfile)):
	    response = webdav._send('GET', pathfile, 200, stream=True)
	    text = ''
	    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
	        text+=chunk

	    return text

	else:
		print("the file: " + pathfile + " doesnt exist")		
		return ""

def getListFiles(webdav, path):	
	filesPath = []
	if webdav.exists(path):
		result = webdav.ls(path)
		
		for item in result:			
			if item.contenttype == "text/plain":	
				filepath = item.name.replace("/dav/cp/generated/production/source/", "")
				filepath = filepath.replace("/dav/cp/generated/stage/source/", "")
				filepath = filepath.replace("/dav/cp/customer/development/", "")
				filesPath.append(filepath)
	else:
		print("it doesnt exist")
		
		
	return filesPath


webdav1 = easywebdav.connect(interfaceUrl1, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
webdav2 = easywebdav.connect(interfaceUrl2, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
listFiles = getListFiles(webdav1, pathFolder)

print(listFiles)


for filePath in listFiles:
	file1 = getPath(environment1) + filePath
	file2 = getPath(environment2) + filePath
	
	print("comparing: " + file1 + "  vs  " + file2)
	filetext1 = read(webdav1, environment1, file1)
	filetext2 = read(webdav2, environment2, file2)

	result = difflib.unified_diff(filetext2.strip().splitlines(), filetext1.strip().splitlines(), fromfile='file1', tofile='file2',  lineterm='', n=6)
	for line in result:
		print(line)




