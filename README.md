Example


```docker build -t python_webdav .```
```docker run -v ~/Desktop/python/webdav:/tmp python_webdav python backup.py```
```docker run -v ~/Desktop/python/webdav:/tmp --env-file=myenv.list python_webdav python backup.py```