
# Overview

### Setup:

Build image with Python 2 + webdav library

```docker build -t python_webdav .```

### Run operations over the ftp server:

```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav python backup.py```

Formatted command
```docker run \
-v ~/Desktop/python/webdav:/tmp \
--env-file=myenv.list \
python_webdav \
python backup.py
```

### Example of myenv.list

```
FTP_USER=*******
FTP_PASS=********
```



# Todo
- [ ] Backup recursively a basic folder
- [ ] Python script must receive an argument (Interface initial: UK, DE, ....)
- [ ] Investigate Restore development from prod or stage (put development in pristine state)
- [ ] Investigate control version for backups from prod.
- [ ] Investigate sync between dev-interfaces. It might speed up replication.
