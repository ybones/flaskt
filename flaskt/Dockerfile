FROM flaskt:v1

WORKDIR /code

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r ./pre-flaskt/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["sh", "run.sh"]