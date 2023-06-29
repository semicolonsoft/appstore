FROM python:3.8

WORKDIR /app
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt
COPY . /app
RUN chmod +x /app/entrypoint.sh
