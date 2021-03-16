FROM python:3.9
# ENV PATH="/scripts:${PATH}"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

# COPY ./scripts /scripts
# RUN chmod +x /scripts/*

RUN useradd user
RUN chown -R user:user /app
RUN chmod -R 755 /app
USER user

# CMD ["entrypoint.sh"]
# CMD ["uwsgi", "app.ini"]
# ENTRYPOINT [ "set -e" ]
# CMD ["uwsgi --http :8001 --master  --enable-threads --module main.py"]
