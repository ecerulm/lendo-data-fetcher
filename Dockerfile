FROM python:3.13.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY fetch.py ./
COPY logging.yaml ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./fetch.py" ]
