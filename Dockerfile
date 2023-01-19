FROM python:3.9-slim
LABEL maintainer="dnghiem@pdx.edu"
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn --bind :$PORT --workers 1 --threads 8 app:app
