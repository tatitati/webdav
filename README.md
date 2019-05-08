
# Overview

### Setup:

Build image with Python 2 + webdav library

```docker build -t python_webdav .```

### Download an specific file from development:

```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav backup.py```

### Display the state of the switch in all interfaces:
```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav switch_state.py```

### Display the content of a file without download it:
```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav read_file.py```


### Example of myenv.list

```
FTP_USER=*******
FTP_PASS=********
FTP_URL=*****
```



# Todo
- [x] ~Functionality to know where is pointing each interface~
- [x] ~Create python image with webdav in linux to avoid problem with pycurl in windows~
- [x] ~Backup a basic file~
- [ ] Functionality to specify environment, interface and path in the CLI to backup, read, ...... :fire:
- [ ] Backup recursively a folder from any environment
- [ ] Python script must receive an argument (Interface initial: UK, DE, ....)
- [ ] Investigate Restore development from prod or stage (put development in pristine state)
- [ ] Investigate control version for backups from prod.
- [ ] Investigate sync between dev-interfaces. It might speed up replication.
