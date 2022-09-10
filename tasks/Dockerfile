FROM python:3.7
ENV WORKDIR /app
RUN useradd -U appuser
RUN install -g appuser -o appuser -d ${WORKDIR}
WORKDIR ${WORKDIR}

COPY requirements.txt ${WORKDIR}/requirements.txt
RUN pip3 install -r requirements.txt

USER appuser
COPY app.py ${WORKDIR}/app.py
CMD celery -A app worker --loglevel=info
