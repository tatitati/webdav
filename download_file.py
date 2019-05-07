import os
import easywebdav


print("this is my script updated")
print(os.environ['FTP_USER'])

webdav = easywebdav.connect('asos-uk.custhelp.com', username=os.environ['FTP_USER'], password=os.environ['FTP_PASS'], protocol='https')
list = webdav.ls("/dav/cp/customer/development")

# print(list)
exists = webdav.exists("/dav/cp/customer/development/models/custom/codmodel.php")
if(exists): 
	webdav.download("/dav/cp/customer/development/models/custom/codmodel.php", "/tmp/backups/UK/codmodel.php")
