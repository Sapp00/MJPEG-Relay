FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir configparser requests pillow

EXPOSE 80

COPY . .

ENTRYPOINT ["python", "web.py"]