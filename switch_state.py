import os
import easywebdav
import re
from generate_urls import *

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024


def read(webdav, remote_path):  
        response = webdav._send('GET', remote_path, 200, stream=True)  
                
        text = ''
        for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
            text+=chunk

        return text

interfacesUrl = getInterfacesUrls()
for interfaceUrl in interfacesUrl:
    print('#################################################################')
    print(interfaceUrl)
    print('===========')    
    webdav = easywebdav.connect(interfaceUrl, username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')

    switchPath = "/dav/cp/customer/development/models/custom/UrlFactory.php"
    if(webdav.exists(switchPath)):        
        filetext = read(webdav, switchPath)


        matchObj = re.match( r'.*public function isLive\(\).*?\n.*?return.*?;', filetext, re.I|re.S)



        if matchObj:
            print(matchObj.group(0))
        else:
            print('state not found')
    else:
        print('file not found')

