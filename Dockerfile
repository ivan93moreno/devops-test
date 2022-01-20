FROM python:3.10-alpine3.15

WORKDIR /code

COPY . .

RUN pip install --upgrade pip && \
    pip install -r ./requirements.txt

EXPOSE 8081
CMD [ "python", "./main.py" ]