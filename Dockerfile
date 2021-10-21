FROM python:3.8-slim
ADD . /UserProfileApp
WORKDIR /UserProfileApp

RUN python -m pip install --upgrade pip
RUN apt update && apt install gcc libpq-dev python3-dev -y
RUN pip install -r requirements.txt

# Installing uwsgi server
RUN pip install uwsgi
EXPOSE 8000


CMD cd UserProfileApp && uwsgi --http "0.0.0.0:8000" --wsgi-file UserProfileApp/wsgi.py --master --enable-threads --check-static .