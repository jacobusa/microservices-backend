FROM python:3.9
ENV PATH="/scripts:${PATH}"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*
# CMD ["python manage.py runserver 0.0.0.0:8000"]
RUN useradd user
RUN chown -R user:user /app
RUN chmod -R 755 /app
USER user
# RUN useradd -m user
# RUN chown -R user:user /app
# RUN chmod -R 755 /app
# USER user
CMD ["entrypoint.sh"]