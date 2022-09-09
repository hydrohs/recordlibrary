FROM alpine

COPY utils/ /bin

RUN add-pkg python3 py3-pip tzdata \
    && pip3 install django

ENV TZ=America/Halifax

ENTRYPOINT [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
