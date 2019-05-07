import os
import easywebdav

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024

webdav = easywebdav.connect('asos-uk.custhelp.com', username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')

switchPath = "/dav/cp/customer/development/models/custom/UrlFactory.php"


def read(webdav, remote_path):	
    response = webdav._send('GET', remote_path, 200, stream=True)
    text = ''
    for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
        text+=chunk

    return text

filetext = read(webdav, switchPath)
print(filetext)