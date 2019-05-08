import os
import sys, getopt
import easywebdav
from generate_urls import *

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024

# Use case
# read_file.py --interface=whatever --environment=dev --file=afile

interfaceURL, environment, pathfile = parseArgs()

webdav = easywebdav.connect(interfaceURL, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')


def read(webdav, environment, pathfile):	

	if(webdav.exists(pathfile)):
	    response = webdav._send('GET', pathfile, 200, stream=True)
	    text = ''
	    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
	        text+=chunk

	    print(text)
	else:
		print("the file: " + pathfile + " doesnt exist")		

filetext = read(webdav, environment, pathfile)
