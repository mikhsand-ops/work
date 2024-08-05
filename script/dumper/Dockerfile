FROM jessica.chandrawisesa.com:5443/hellopy
COPY ./app /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt --upgrade

ENTRYPOINT [ "python3", "dump.py"]

