
## Setup:

1- Build image with Python 2 + webdav library

```docker build -t python_webdav .```

2- Create a file named m"yenv.list" with the next structure, this file and the python code will be mounted in runtime to speed up debug and modification in code:

```
FTP_USER=*******
FTP_PASS=********
```

## Use cases: 
### - Download an specific file from development (soon also folders):

```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav backup.py```

### - Diff between files in different interface and environment

```docker run -v ~\Desktop\webdav:/tmp --env-file=myenv.list python_webdav compare_file.py --interface1=uk --interface2=uk --environment1=dev --environment2=stg --file=models/custom/UrlFactory.php```

### - Display the content of a file (without download it):
```docker run -v ~/Desktop/docker/webdav:/tmp --env-file=myenv.list python_webdav read_file.py --interface=it --environment=stg --file=models/custom/UrlFactory.php```





# Todo
- [x] ~Functionality to know where is pointing each interface~
- [x] ~Create python image with webdav in linux to avoid problem with pycurl in windows~
- [x] ~Backup a basic file~
- [x] ~Functionality to specify environment, interface and path in the CLI to backup, read, ......~
- [ ] Backup recursively a folder from any environment :fire:
- [ ] Investigate Restore development from prod or stage (put development in pristine state)
- [ ] Investigate control version for backups from prod.
- [ ] Investigate sync between dev-interfaces. It might speed up replication.
