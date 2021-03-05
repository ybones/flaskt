FROM hunger:v1

WORKDIR /code

COPY . /code/hunger

RUN python -m pip install --upgrade pip

RUN pip install -r ./hunger/docker-pre/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple