FROM python:2
RUN easy_install easywebdav

CMD ["python"]
# RUN pip install --no-cache-dir -y webdav
