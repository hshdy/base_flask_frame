FROM python:3.6
COPY ./src ./src
WORKDIR /src

RUN mkdir -p ~/.pip/
RUN echo '[global]' >> ~/.pip/pip.conf
RUN echo 'trusted-host =  mirrors.aliyun.com' >> ~/.pip/pip.conf
RUN echo 'index-url = http://mirrors.aliyun.com/pypi/simple' >> ~/.pip/pip.conf

VOLUME /tmp

# COPY requirements.txt .
# COPY hello.py .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3"]

EXPOSE 55555

CMD ["app.py"]