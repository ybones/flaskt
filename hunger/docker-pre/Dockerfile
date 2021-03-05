FROM python:3.8

COPY requirements.txt /home

RUN pip install --no-cache-dir --upgrade pip

RUN pip install -r /home/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
