FROM scheduler:v1

WORKDIR /code/

COPY . /code/scheduler

RUN python -m pip install --upgrade pip

RUN pip install -r ./scheduler/docker-pre/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple