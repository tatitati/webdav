import os
import sys, getopt
import easywebdav
from generate_urls import *

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024

# Use case
# read_file.py --interface=whatever --environment=dev --file=afile
opts, _ = getopt.getopt(sys.argv[1:], [], ['interface=', 'environment=', 'file='])

interface = ''
environment = ''
file = ''
for opt, arg in opts:
	if opt in ('--interface'):
		interface = arg
	if opt in ('--environment'):
		environment = arg
	if opt in ('--file'):
		pathfile = arg		


webdav = easywebdav.connect(getInterfacesUrls(interface), username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')


def read(webdav, environment, pathfile):	
	filePathInEnvironment = getPath(environment) + pathfile

	if(webdav.exists(filePathInEnvironment)):
	    response = webdav._send('GET', filePathInEnvironment, 200, stream=True)
	    text = ''
	    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
	        text+=chunk

	    print(text)
	else:
		print("the file: " + filePathInEnvironment + " doesnt exist")		

filetext = read(webdav, environment, pathfile)
