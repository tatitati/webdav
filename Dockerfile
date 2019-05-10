FROM python:2
RUN pip install easywebdav
WORKDIR "/tmp"
ENTRYPOINT ["python"]
# RUN pip install --no-cache-dir -y webdav
