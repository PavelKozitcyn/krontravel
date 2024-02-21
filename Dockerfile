from python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./api/ ./
RUN pip3 install -r requirements.txt
COPY get_lazy.py .
RUN sed -i 's/from django.utils.translation import ugettext_lazy as _/from django.utils.translation import gettext_lazy as _/g' /usr/local/lib/python3.10/site-packages/taggit_serializer/serializers.py

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

RUN pip3 install gunicorn
CMD ["gunicorn", "api.wsgi", "-b", "0.0.0.0:8080"]