FROM python:3.9-slim

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput --clear


EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "the_eye.wsgi"]