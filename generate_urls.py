import sys, getopt

def getInterfacesUrls(interfacekey):

	mapInterface = {
		'com': 'asos.custhelp.com',
		'uk': 'asos-uk.custhelp.com', 
		'de': 'asos-de.custhelp.com',
		'sp': 'asos-sp.custhelp.com',
		'it': 'asos-it.custhelp.com',	
		'fr': 'asos-fr.custhelp.com',	
		'us': 'asos-us.custhelp.com',
		'eu': 'asos-eu.custhelp.com',
		'cn': 'asos-cn.custhelp.com',
		'kr': 'asos-kr.custhelp.com',
		'se': 'asos-se.custhelp.com',
		'ru': 'asos-ru.custhelp.com'
	}

	return mapInterface[interfacekey]



def getPath(environment):
		
	mapPath = {
		'dev': '/dav/cp/customer/development/',
		'stg': '/dav/cp/generated/staging/source/', 
		'prod': '/dav/cp/generated/production/source/'		
	}
	
	if(environment not in mapPath):
		print("this environment doesnt exist. The available are: dev, stg, prod)")
		sys.exit(0)

	return mapPath[environment]

def getShortPath(environment):
		
	mapPath = {
		'dev': 'development/',
		'stg': 'staging/source/', 
		'prod': 'production/source/'		
	}
	
	if(environment not in mapPath):
		print("this environment doesnt exist. The available are: dev, stg, prod)")
		sys.exit(0)

	return mapPath[environment]

def parseArgs():
	opts, _ = getopt.getopt(sys.argv[1:], [], ['interface=', 'environment=', 'file='])

	interfaceUrl = ''
	environment = ''
	file = ''
	for opt, arg in opts:
		if opt in ('--interface'):
			interfaceUrl = getInterfacesUrls(arg)
		if opt in ('--environment'):
			environment = arg
		if opt in ('--file'):			 		
			pathfile = getPath(environment) + arg

	return [interfaceUrl, environment, pathfile]
