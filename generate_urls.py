def getInterfacesUrls(interfacekey):

	mapInterface = {
		'com': 'asos.custhelp.com',
		'uk': 'asos-uk.custhelp.com', 
		'de': 'asos-de.custhelp.com',
		'sp': 'asos-sp.custhelp.com',
		'it': 'asos-it.custhelp.com',	
		'us': 'asos-us.custhelp.com',
		'eu': 'asos-eu.custhelp.com',
		'cn': 'asos-cn.custhelp.com',
		'kr': 'asos-kr.custhelp.com',
		'se': 'asos-se.custhelp.com'
	}

	return mapInterface[interfacekey]



def getPath(environment):
	mapPath = {
		'dev': '/dav/cp/customer/development/',
		'stg': '/dav/cp/generated/staging/source/', 
		'prod': '/dav/cp/generated/production/source/'		
	}

	return mapPath[environment]
